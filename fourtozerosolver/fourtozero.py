from Solver import DWULT

def initial_position():
	return 4

def primitive(pos):
	return DWULT['UNDECIDED'] if pos else DWULT['LOSS']

def gen_moves(pos):
	return [move for move in [-1, -2] if pos + move >= 0]

def do_move(pos, move):
	return pos + move;
