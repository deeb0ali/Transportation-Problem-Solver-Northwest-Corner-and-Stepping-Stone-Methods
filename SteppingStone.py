import numpy as np

class SteppingStone:
    def __init__(self, cost, demand, supply):
        self.cost = cost
        self.demand = demand
        self.supply = supply
        self.n = len(supply)
        self.m = len(demand)
        self.very_large_number = np.inf
        self.route = [[0]*self.m for _ in range(self.n)]
        self.dual = [[-1]*self.m for _ in range(self.n)]
        self.pivot_n = -1
        self.pivot_m = -1

    def north_west(self):
        u = v = 0
        a_s = [0] * self.m
        a_d = [0] * self.n
        while u <= self.n - 1 and v <= self.m - 1:
            if self.demand[v] - a_s[v] < self.supply[u] - a_d[u]:
                z = self.demand[v] - a_s[v]
                self.route[u][v] = z
                a_s[v] += z
                a_d[u] += z
                v += 1
            else:
                z = self.supply[u] - a_d[u]
                self.route[u][v] = z
                a_s[v] += z
                a_d[u] += z
                u += 1

    def not_optimal(self):
        n_max = -self.very_large_number
        self.get_dual()
        for u in range(self.n):
            for v in range(self.m):
                x = self.dual[u][v]
                if x > n_max:
                    n_max = x
                    self.pivot_n = u
                    self.pivot_m = v
        return n_max > 0

    def get_dual(self):
        for u in range(self.n):
            for v in range(self.m):
                self.dual[u][v] = -0.5  # null value
                if self.route[u][v] == 0:
                    a_path = self.find_path(u, v)
                    z = -1
                    x = 0
                    for w in a_path:
                        x += z * self.cost[w[0]][w[1]]
                        z *= -1
                    self.dual[u][v] = x

    def find_path(self, u, v, path=None):
        if path is None:
            path = []
        elif len(path) > 3 and path[0] == [u, v] and len(path) % 2 == 0:
            return path
        elif [u, v] in path:
            return None 

        path = path + [[u, v]]

        # if the current cell is used, look for unused cells
        if self.route[u][v] != 0:
            for i in range(self.m):
                if self.route[u][i] == 0:  
                    new_path = self.find_path(u, i, path)
                    if new_path:
                        return new_path

            for i in range(self.n):
                if self.route[i][v] == 0:
                    new_path = self.find_path(i, v, path)
                    if new_path:
                        return new_path

        # if the current cell is unused, look for used cells
        else:
            for i in range(self.m):
                if i != v and self.route[u][i] != 0:
                    new_path = self.find_path(u, i, path)
                    if new_path:
                        return new_path

            for i in range(self.n):
                if i != u and self.route[i][v] != 0:
                    new_path = self.find_path(i, v, path)
                    if new_path:
                        return new_path
        return None


    def look_horizontally(self, a_path, u, v, u1, v1):
        for i in range(self.m):
            if i != v and self.route[u][i] != 0:
                if i == v1:
                    a_path.append([u, i])
                    return True  # complete circuit
                if self.look_vertically(a_path, u, i, u1, v1):
                    a_path.append([u, i])
                    return True
        return False  # not found

    def look_vertically(self, a_path, u, v, u1, v1):
        for i in range(self.n):
            if i != u and self.route[i][v] != 0:
                if self.look_horizontally(a_path, i, v, u1, v1):
                    a_path.append([i, v])
                    return True
        return False  # not found

    def better_optimal(self):
        a_path = self.find_path(self.pivot_n, self.pivot_m)
        z = min([self.route[a_path[i][0]][a_path[i][1]] for i in range(1, len(a_path), 2)])
        for i in range(1, len(a_path), 2):
            self.route[a_path[i][0]][a_path[i][1]] -= z
            self.route[a_path[i - 1][0]][a_path[i - 1][1]] += z

    def print_out(self):
        return '\n'.join([' '.join(map(str, self.route[i])) for i in range(self.n)]) + '\n'

    def solve(self):
        try:
            assert np.array(self.demand).sum()==np.array(self.supply).sum() # The problem should be balanced
        except:
            return "Problem is not balanced !"

        self.north_west()
        output = "Initial Allocation:\n" + self.print_out() + "\n"

        total_cost = 0

        try : # Try enhancing the solution
            while self.not_optimal():
                output += 'PIVOTING ON\n' + str(self.pivot_n) + " " + str(self.pivot_m) + "\n"
                self.better_optimal()
                output += "Updated Allocation:\n" + self.print_out() + "\n"
        except:
            pass

        for i in range(self.n):
            for j in range(self.m):
                total_cost += self.route[i][j] * self.cost[i][j]

        output += "Total Cost: " + str(total_cost) + "\n"
        output += "FINISHED"
        return output


if __name__=='__main__':

    cost =  [[9, 3, 3, 3], [3, 6, 10, 8], [9, 2, 8, 5]]
    supply =  [133, 133, 134]
    demand =  [100, 100, 100, 100]
    
    stepping_stone = SteppingStone(cost, demand, supply)
    result = stepping_stone.solve()
    print(result)
