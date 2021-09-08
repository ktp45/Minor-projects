from secrets import randbelow
from Linkedlist import CircularlinkedList


class Board:  # the slots machine display made by 5 columns each an equal list
    def __init__(self, list1=CircularlinkedList()):
        self.l1 = CircularlinkedList()
        self.l2 = CircularlinkedList()
        self.l3 = CircularlinkedList()
        self.l4 = CircularlinkedList()
        self.l5 = CircularlinkedList()
        for ii in (self.l1, self.l2, self.l3, self.l4, self.l5):
            ii.copy(list1)

    def print_board(self):
        print(self.l1.get_root(), " ", self.l2.get_root(), " ", self.l3.get_root(), " ", self.l4.get_root(), " ",
              self.l5.get_root())
        print(self.l1.get_second(), " ", self.l2.get_second(), " ", self.l3.get_second(), " ", self.l4.get_second(),
              " ", self.l5.get_second())
        print(self.l1.get_third(), " ", self.l2.get_third(), " ", self.l3.get_third(), " ", self.l4.get_third(), " ",
              self.l5.get_third())

    def random_spin_board(self):  # spins all by a random number
        for ii in (self.l1, self.l2, self.l3, self.l4, self.l5):
            ii.spin(randbelow(1000))

    def line1(self):  # checks if on line 1 on the display, there are and equal symbols and returns price
        temp = self.l1.get_root()  # starting symbol of the line
        five_equal = temp.eq5(self.l2.get_second(), self.l3.get_third(), self.l4.get_second(),
                              self.l5.get_root())  # call to the node function
        four_equal = temp.eq4(self.l2.get_second(), self.l3.get_third(), self.l4.get_second())
        three_equal = temp.eq3(self.l2.get_second(), self.l3.get_third())
        if five_equal > 0:
            return five_equal
        elif four_equal > 0:
            return four_equal
        else:
            return three_equal  # if there are four or five there are also 3 equal so its called last the three function

    def line2(self):  # same as line 1
        temp = self.l1.get_second()
        five_equal = temp.eq5(self.l2.get_second(), self.l3.get_second(), self.l4.get_second(), self.l5.get_second())
        four_equal = temp.eq4(self.l2.get_second(), self.l3.get_second(), self.l4.get_second())
        three_equal = temp.eq3(self.l2.get_second(), self.l3.get_second())
        if five_equal > 0:
            return five_equal
        elif four_equal > 0:
            return four_equal
        else:
            return three_equal

    def line3(self):  # same as line 1
        temp = self.l1.get_third()
        five_equal = temp.eq5(self.l2.get_second(), self.l3.get_root(), self.l4.get_second(), self.l5.get_third())
        four_equal = temp.eq4(self.l2.get_second(), self.l3.get_root(), self.l4.get_second())
        three_equal = temp.eq3(self.l2.get_second(), self.l3.get_root())
        if five_equal > 0:
            return five_equal
        elif four_equal > 0:
            return four_equal
        else:
            return three_equal

    def get_board_in_list(self):
        line = []
        for i in (self.l1.get_root(),self.l2.get_root(),self.l3.get_root(),self.l4.get_root(),self.l5.get_root()):
            line.append(i.get_name())
        for i in (self.l1.get_second(),self.l2.get_second(),self.l3.get_second(),self.l4.get_second(),self.l5.get_second()):
            line.append(i.get_name())
        for i in (self.l1.get_third(), self.l2.get_third(), self.l3.get_third(), self.l4.get_third(), self.l5.get_third()):
            line.append(i.get_name())

        return line
