DWULT = {
    'DRAW': 'D',
    'WIN': 'W',
    'UNDECIDED': 'U',
    'LOSS': 'L',
    'TIE': 'T'
}

class Solver:
    def __init__(self, initial_position, primitive, gen_moves, do_move):
        self.initial_position = initial_position
        self.primitive = primitive
        self.gen_moves = gen_moves
        self.do_move = do_move
        self.memo = {}

    def solve_position(self, cur_pos):
        if cur_pos in self.memo:
            return self.memo[cur_pos]
        result = self.primitive(cur_pos)
        if result == DWULT['UNDECIDED']:
            moves = self.gen_moves(cur_pos)
            new_positions = [self.do_move(cur_pos, move) for move in moves]
            losing_children = [pos for pos in new_positions if self.solve_position(pos) == DWULT['LOSS']]
            # ties and draws not handled yet
            result = DWULT['WIN'] if len(losing_children) else DWULT['LOSS']
        self.memo[cur_pos] = result
        return result

    def solve(self):
        return self.solve_position(self.initial_position())
