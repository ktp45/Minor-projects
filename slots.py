from secrets import randbelow
class Symbol: # each symbol has name, in-game multiplier and can be the universal symbol (wild)
    def __init__(self, name=" ",multiplier=0.,isWild=False):
        self.name = name
        self.multiplier = multiplier
        self.isWild = isWild

    def __str__(self): # we want to print just the symbols name
        return self.name

class Node(Symbol): # nodes part of the linked list
    def __init__(self, d=Symbol(), n=None):
        Symbol.__init__(self,d.name,d.multiplier,d.isWild)
        self.next_node = n

    def __str__(self):
        return '(' + str(self.name) + ')'

    def eq(self,other): # comparison between two nodes, since we need the universal node to be equal to all others
        if self.isWild or other.isWild:
         return True
        return self.multiplier==other.multiplier

    def eq3(self,sec,th): # comparison between three nodes, which generates winnings
        if self.eq(sec) and self.eq(th) and sec.eq(th):
            if (self.isWild or sec.isWild or th.isWild) and not(self.isWild and sec.isWild and th.isWild): # if there is a wild
             for j in (self, sec,th):
                if not j.isWild:
                    return pow(j.multiplier,3) # we need the not wild multiplier and we pow it the times we have that symbol
            else:
                return pow(self.multiplier,3)
        else:
            return 0
    def eq4(self,sec,th,fo): # comparison between four nodes, which generates winnings
        if self.eq3(sec,th)>1 and self.eq(fo) and sec.eq(fo) and th.eq(fo):
            if (self.isWild or sec.isWild or th.isWild or fo.isWild) and not (self.isWild and sec.isWild and th.isWild and fo.isWild): # if there is a wild
                 for j in (self, sec, th, fo):
                    if not j.isWild:
                        return pow(j.multiplier, 4) # we need the not wild multiplier and we pow it the times we have that symbol
            else:
                return pow(self.multiplier, 4)
        else:
            return 0
    def eq5(self,sec,th,fo,fi): # comparison between five nodes, which generates winnings
        if self.eq4(sec,th,fo)>1 and self.eq(fi) and sec.eq(fi) and th.eq(fi) and fo.eq(fi):
            if (self.isWild or sec.isWild or th.isWild or fo.isWild or fi.isWild) and not (self.isWild and sec.isWild and th.isWild and fo.isWild and fi.isWild): # if there is a wild
                 for j in (self, sec, th, fo, fi):
                    if not j.isWild:
                        return pow(j.multiplier, 5)  # we need the not wild multiplier and we pow it the times we have that symbol
            else:
                return pow(self.multiplier, 5)
        else :
            return 0

class CircularlinkedList: # list of nodes, in which the last one points to the first
    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def get_root(self): # bunch of get functions for ease of access
        return self.root

    def get_root_multi(self):
        return self.root.data.get_multiplier()

    def get_second(self): # returns second node
        return self.root.next_node

    def get_third(self): # returns third node
        this_node= self.root.next_node
        this_node=this_node.next_node
        return this_node

    def get_size(self):
        return self.size

    def add(self, d=Symbol()):
        if self.size == 0: # if empty create new
            self.root = Node(d)
            self.root.next_node = self.root
        else: # else put it second
            new_node = Node(d, self.root.next_node)
            self.root.next_node = new_node
        self.size += 1

    def spin(self, times): # function which rotates the list num of times
        if self.root is None:  #check if list is empty
            return
        if times == 0 or times % self.get_size() == 0: # check if we had to rotate
            return
        prev_node = None # works as a temporary node to store the current
        count = 0
        while count < times and self.root is not None:
            if prev_node is not None:
                prev_node=prev_node.next_node
            else:
                prev_node=self.root #prev_node becomes the current and the current becomes its next
            self.root = self.root.next_node
            count += 1


    def copy(self,source): # copy function from another list
        self.root=source.root
        self.size=source.size
        this_node = self.root
        source_node = source.root
        while source_node.next_node!=source.root: # copy until we get to the last one which points to its root
            source_node=source_node.next_node
            this_node.next_node=source_node
            this_node=this_node.next_node
        this_node.next_node=self.root #make it circular by pointing the last to the first

class Board: # the slots machine display made by 5 columns each an equal list
    def __init__(self, list1=CircularlinkedList()):
        self.l1 = CircularlinkedList()
        self.l2 = CircularlinkedList()
        self.l3 = CircularlinkedList()
        self.l4 = CircularlinkedList()
        self.l5 = CircularlinkedList()
        for ii in (self.l1, self.l2, self.l3, self.l4, self.l5):
            ii.copy(list1)

    def print_board(self):
        print (self.l1.get_root(), " ", self.l2.get_root(), " ", self.l3.get_root(), " ", self.l4.get_root(), " ", self.l5.get_root())
        print(self.l1.get_second(), " ", self.l2.get_second(), " ", self.l3.get_second(), " ", self.l4.get_second(), " ", self.l5.get_second())
        print(self.l1.get_third(), " ", self.l2.get_third(), " ", self.l3.get_third(), " ", self.l4.get_third(), " ", self.l5.get_third())

    def random_spin_board(self): # spins all by a random number
        for ii in (self.l1, self.l2, self.l3, self.l4, self.l5):
            ii.spin(randbelow(1000))

    def line1(self): # checks if on line 1 on the display, there are and equal symbols and returns price
        temp = self.l1.get_root() #starting symbol of the line
        five_equal = temp.eq5(self.l2.get_second(), self.l3.get_third(), self.l4.get_second(), self.l5.get_root())#call to the node function
        four_equal = temp.eq4(self.l2.get_second(), self.l3.get_third(), self.l4.get_second())
        three_equal = temp.eq3(self.l2.get_second(), self.l3.get_third())
        if five_equal > 0:
            return five_equal
        elif four_equal > 0:
            return four_equal
        else:
            return three_equal #if there are four or five there are also 3 equal so we call last the three function

    def line2(self): # same as line 1
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

    def line3(self): # same as line 1
        temp=self.l1.get_third()
        five_equal =temp.eq5(self.l2.get_second(),self.l3.get_root(),self.l4.get_second(),self.l5.get_third())
        four_equal=temp.eq4(self.l2.get_second(),self.l3.get_root(),self.l4.get_second())
        three_equal=temp.eq3(self.l2.get_second(),self.l3.get_root())
        if five_equal > 0:
            return five_equal
        elif four_equal > 0:
            return four_equal
        else:
            return three_equal

ketchup= Symbol("k",2,True)
maionese = Symbol("m",1.9)
vinegar= Symbol("v",1.8)
gorchica = Symbol("g",1.7)
barbeque = Symbol("b",1.6)
ranch = Symbol("r",1.5) #symbol creation the theme is sauces
tabasco = Symbol("t",1.4)#odd are in players favor by small
garlic_sauce = Symbol("s",1.3)
olive_oil = Symbol("o",1.2)
sour_cream = Symbol("c",1.1)
reel1 = CircularlinkedList() # creating a list with all them
for i in (ketchup, maionese, gorchica, barbeque, ranch, tabasco, garlic_sauce, olive_oil, vinegar, sour_cream):
    reel1.add(i)
display=Board(reel1) # creating a board with all them

money = int(input("Enter starting amount money:")) # imagine putting money into the game
while 1:
    bet =float(input("Place your bet to spin the wheel or press 0 to exit: \n")) #bet on current spin, for testing mode make that 1
    if bet!=0 and money>=0:
        display.random_spin_board() # spin the board
        first=display.line1()
        second=display.line2()
        third=display.line3()
        display.print_board() # print it
        total = bet*first+bet*second+bet*third # total winnings if they exist
        if total > 0:
            if first > 0 : print ("Line 1:",bet * first)
            if second > 0: print("Line 2:", bet * second) # shows player which line is the lucky one
            if third > 0: print("Line 3:", bet * third)
            print("You win: ",total)
            money+=total
        else:
            print("You lose!")
            money -= bet # losing money
        print("Current money: ", money)
    else:
        break #if bet is 0 or we have no money we stop the machine

