# Maze Solver

This project presents an implementation of algorithms to find the best path to solve mazes represented as binary images. The implemented algorithms are BFS (Breadth-First Search) and DFS (Depth-First Search). The project utilizes the PIL (Python Imaging Library) for image processing.

## Requirements

- Python 3.x
- PIL (Python Imaging Library)

## Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/moraleseoscar/Maze-Solver.git
   ```

2. Install dependencies:

   ```bash
   pip install pillow
   ```

3. Run the main script:

   ```bash
   python maze_solver.py
   ```

4. Choose the desired algorithm when prompted.

## Implementation Details

- **BFS (Breadth-First Search)**: This algorithm exhaustively searches the maze, expanding uniformly all nodes at the current level before moving to the next level.
  
- **DFS (Depth-First Search)**: This algorithm explores as far as possible along each branch before backtracking.

## Example Result

[![TuringResult.png](https://i.postimg.cc/xdQ3rJ4w/Example.png)](https://postimg.cc/mPdHCDRj)
