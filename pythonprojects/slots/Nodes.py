import Symbols


class Node(Symbols.Symbol):  # nodes part of the linked list
    def __init__(self, d=Symbols.Symbol(), n=None):
        Symbols.Symbol.__init__(self, d.name, d.multiplier, d.isWild)
        self.next_node = n

    def __str__(self):
        return '(' + str(self.name) + ')'

    def eq(self, other):  # comparison between two nodes, since we need the universal node to be equal to all others
        if self.isWild or other.isWild:
            return True
        return self.multiplier == other.multiplier

    def eq3(self, sec, th):  # comparison between three nodes, which generates winnings
        if self.eq(sec) and self.eq(th) and sec.eq(th):
            if (self.isWild or sec.isWild or th.isWild) and not (
                    self.isWild and sec.isWild and th.isWild):  # if there is a wild
                for j in (self, sec, th):
                    if not j.isWild:
                        return pow(j.multiplier, 3)  # we need the not wild multiplier and we pow it the times we have that Symbols
            else:
                return pow(self.multiplier, 3)
        else:
            return 0

    def eq4(self, sec, th, fo):  # comparison between four nodes, which generates winnings
        if self.eq3(sec, th) > 1 and self.eq(fo) and sec.eq(fo) and th.eq(fo):
            if (self.isWild or sec.isWild or th.isWild or fo.isWild) and not (
                    self.isWild and sec.isWild and th.isWild and fo.isWild):  # if there is a wild
                for j in (self, sec, th, fo):
                    if not j.isWild:
                        return pow(j.multiplier, 4)  # we need the not wild multiplier and we pow it the times we have that Symbol
            else:
                return pow(self.multiplier, 4)
        else:
            return 0

    def eq5(self, sec, th, fo, fi):  # comparison between five nodes, which generates winnings
        if self.eq4(sec, th, fo) > 1 and self.eq(fi) and sec.eq(fi) and th.eq(fi) and fo.eq(fi):
            if (self.isWild or sec.isWild or th.isWild or fo.isWild or fi.isWild) and not (
                    self.isWild and sec.isWild and th.isWild and fo.isWild and fi.isWild):  # if there is a wild
                for j in (self, sec, th, fo, fi):
                    if not j.isWild:
                        return pow(j.multiplier, 5)  # we need the not wild multiplier and we pow it the times we have that Symbol
            else:
                return pow(self.multiplier, 5)
        else:
            return 0
