from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel, QGridLayout, QTextEdit
import sys
from SteppingStone import SteppingStone
import random 

class SteppingStoneGUI(QWidget):
    def __init__(self, n, m):
        super().__init__()

        self.n = n
        self.m = m

        self.costEdits = [[QLineEdit(self) for _ in range(m)] for _ in range(n)]
        self.supplyEdits = [QLineEdit(self) for _ in range(n)]
        self.demandEdits = [QLineEdit(self) for _ in range(m)]

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        grid = QGridLayout()

        # Create labels and line edits for demand
        for i in range(self.m):
            grid.addWidget(QLabel('D' + str(i+1), self), 0, i+2)
            grid.addWidget(self.demandEdits[i], 1, i+2)

        # Create labels and line edits for supply and costs
        for i in range(self.n):
            grid.addWidget(QLabel('S' + str(i+1), self), i+2, 0)
            grid.addWidget(self.supplyEdits[i], i+2, 1)
            for j in range(self.m):
                grid.addWidget(self.costEdits[i][j], i+2, j+2)

        # Create buttons and text edit for output
        self.initButton = QPushButton('Initialize', self)
        self.initButton.clicked.connect(self.initialize)
        self.solveButton = QPushButton('Solve', self)
        self.solveButton.clicked.connect(self.solve)
        self.outputEdit = QTextEdit(self)

        layout.addLayout(grid)
        layout.addWidget(self.initButton)
        layout.addWidget(self.solveButton)
        layout.addWidget(self.outputEdit)
        self.setLayout(layout)

    def initialize(self):
        # Calculate the target sum based on the maximum of self.n and self.m
        target_sum = max(self.n, self.m) * 100

        # Calculate the equal distribution for supply and demand (excluding the last QLineEdit)
        supply_value = target_sum // self.n if self.n >= 1 else 0
        demand_value = target_sum // self.m if self.m >= 1 else 0

        # Initialize supply and demand with the equal distribution
        for i, edit in enumerate(self.supplyEdits):
            edit.setText(str(supply_value))
        if ( supply_value*self.n != target_sum):
            self.supplyEdits[-1].setText( str(int(self.supplyEdits[-1].text()) + (target_sum - supply_value*self.n )) )

        for i, edit in enumerate(self.demandEdits):
            edit.setText(str(demand_value))

        if ( demand_value*self.m != target_sum):
            self.demandEdits[-1].setText( str(int(self.demandEdits[-1].text()) + (target_sum - demand_value*self.m )) )

        # Initialize cost with random values
        for row in self.costEdits:
            for edit in row:
                c = random.randint(1,10)
                edit.setText(str(c))  # Use any number here

    def solve(self):
        # Get supply, demand, and costs from line edits
        supply = [int(edit.text()) for edit in self.supplyEdits]
        demand = [int(edit.text()) for edit in self.demandEdits]
        cost = [[int(edit.text()) for edit in row] for row in self.costEdits]

        # Create SteppingStone instance and solve
        print ( supply)
        print(demand)
        print(cost)
        stepping_stone = SteppingStone(cost, demand, supply)
        result = stepping_stone.solve()

        # Print result in output edit
        self.outputEdit.setText(result)

def main():
    app = QApplication(sys.argv)

    # Create and show SteppingStoneGUI
    n = int (input('number of supplies: '))
    m = int (input('number of demands: ') )
    gui = SteppingStoneGUI(n,m)
    gui.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
