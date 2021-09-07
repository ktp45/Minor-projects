class resulter:
    def __init__(self, wins=1, lines=[], board=[]):
        self.wins = wins
        self.winning_lines = lines
        self.board = board

    def get_wins(self):
        return self.wins

    def get_lines(self):
        return self.winning_lines

    def get_board(self):
        return self.board
