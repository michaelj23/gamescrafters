from Solver import Solver
from fourtozero import initial_position, primitive, gen_moves, do_move

fourtozero_solver = Solver(initial_position, primitive, gen_moves, do_move)
print(fourtozero_solver.solve())
