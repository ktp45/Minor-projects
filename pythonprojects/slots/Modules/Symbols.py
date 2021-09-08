class Symbol:  # each symbol has name, in-game multiplier and can be the universal symbol (wild)
    def __init__(self, name=" ", multiplier=0, isWild=False):
        self.name = name
        self.multiplier = multiplier
        self.isWild = isWild
