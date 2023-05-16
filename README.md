# Transportation Problem Solver: Northwest Corner and Stepping Stone Methods

This repository contains a solution for transportation problems using the Northwest Corner Method and the Stepping Stone Method, implemented in a user-friendly Graphical User Interface (GUI). Transportation problems arise in various industries, requiring the optimal allocation of goods from suppliers to customers while minimizing transportation costs.

The GUI allows users to input problem parameters, visualize the step-by-step solution process, and obtain the optimal allocation and total transportation cost. The Northwest Corner Method is used for initial allocation, while the Stepping Stone Method iteratively improves the solution.

## SteppingStone Class

The `SteppingStone` class is a Python implementation of the Stepping Stone Method for solving transportation problems. It provides the necessary methods and functionality to perform the initial allocation, identify the optimality of the solution, find improvement paths, and update the allocation iteratively.

Key methods include:

- `north_west()`: Performs the initial allocation using the Northwest Corner Method.
- `not_optimal()`: Determines whether the current solution is optimal or not.
- `get_dual()`: Calculates the dual variables based on the current allocation.
- `find_path()`: Finds an improvement path for the Stepping Stone Method.
- `better_optimal()`: Improves the current allocation by updating the quantities along the improvement path.
- `print_out()`: Generates a printable representation of the allocation matrix.
- `solve()`: Performs the overall solution process.

## Graphical User Interface (GUI)

The GUI provides a user-friendly platform for solving transportation problems using the Northwest Corner Method and the Stepping Stone Method. Key components include:

- **Input Parameters**: Users can enter the number of suppliers ($n$) and customers ($m$), and the supply ($s_i$), demand ($d_j$), and cost ($c_{ij}$) values.
- **Initialization**: The GUI includes an "Initialize" button that populates the supply and demand fields with balanced values, and the cost fields with random values.
- **Solution Process**: Upon clicking the "Solve" button, the GUI triggers the solution process.
- **Output Display**: The GUI displays the allocation matrix, cost matrix, and the final solution.

## Usage

1. Clone this repository.
2. Run `python gui.py`.
3. Input the problem parameters in the GUI.
4. Click "Initialize" to generate a balanced problem.
5. Click "Solve" to start the solution process.
6. Review the output in the text display.

## Contributing

Contributions are welcome. Please submit a pull request or create an issue to discuss the changes you propose.

## License

This project is licensed under the terms of the MIT License.
