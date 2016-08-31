def init_state():
	return 4

def primitive(state):
	return 'U' if state else 'L'

def gen_moves(state):
	return [move for move in [-1, -2] if state + move >= 0]

def do_move(state, move):
	return state + move;

def solver(init_state, primitive, gen_moves, do_move):
	memo = {}

	def solve(cur_state):
		if cur_state in memo:
			return memo[cur_state]
		result = primitive(cur_state)
		if result == 'U':
			result = 'W' if len([state for state in [do_move(cur_state, move) for move in gen_moves(cur_state)] if solve(state) == 'L']) else 'L'
		memo[cur_state] = result
		return result

	return solve(init_state())

print(solver(init_state, primitive, gen_moves, do_move))