class Resulter:  # class saving results of every slot machine spit
    def __init__(self, wins=1, lines=None, board=None):
        self.wins = wins
        self.winning_lines = lines
        self.board = board

    def get_wins(self): # getters for encapsulation
        return self.wins

    def get_lines(self):
        return self.winning_lines

    def get_board(self):
        return self.board
