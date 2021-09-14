from models.puzzle import Puzzle
from models.solver import Solver

board = [
  [1,2,3],
  [4,5,0],
  [6,7,8]
]

puzzle = Puzzle(board)
solver = Solver(puzzle)

solution_path = solver.solve()
steps = 0

for node in solution_path:
    print(node.action)
    node.puzzle.print_puzzle()

    steps += 1

print("Total number of steps: " + str(steps))
