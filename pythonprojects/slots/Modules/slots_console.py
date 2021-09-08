from Linkedlist import CircularlinkedList
from Symbols import Symbol
from Board import Board

ketchup = Symbol("k", 2, True)
maio = Symbol("m", 1.9)
vinegar = Symbol("v", 1.8)
gorchica = Symbol("g", 1.7)
barbeque = Symbol("b", 1.6)
ranch = Symbol("r", 1.5)  # Symbol creation the theme is sauces
tabasco = Symbol("t", 1.4)  # odd are in players favor by small
garlic_sauce = Symbol("s", 1.3)
olive_oil = Symbol("o", 1.2)
sour_cream = Symbol("c", 1.1)
money = 0
bet = 0
reel1 = CircularlinkedList()  # creating a list with all them
for i in (ketchup, maio, gorchica, barbeque, ranch, tabasco, garlic_sauce, olive_oil, vinegar, sour_cream):
    reel1.add(i)
display = Board(reel1)  # creating a board with all them

isValid = False
while not isValid:
    try:
        money = int(input("Enter starting amount money:"))  # imagine putting money into the game
        isValid = True
    except TypeError or ValueError:
        print("Enter valid money!")

while 1:
    isValid = False
    while not isValid:
        try:
            bet = float(input("Place your bet to spin the wheel or press 0 to exit: \n"))
            isValid = True
        except TypeError or ValueError:
            print("Enter valid bet!")

    # bet on current spin, for testing mode make that 1
    if bet != 0 and money > 0 and bet <= money:
        display.random_spin_board()  # spin the board
        first = display.line1()
        second = display.line2()
        third = display.line3()
        display.print_board()  # print it
        total = bet * first + bet * second + bet * third  # total winnings if they exist
        if total > 0:
            if first > 0:
                print("Line 1:", bet * first)
            if second > 0:
                print("Line 2:", bet * second)  # shows player which line is the lucky one
            if third > 0:
                print("Line 3:", bet * third)
            print("You win: ", total)
            money += total
        else:
            print("You lose!")
            money -= bet  # losing money
        print("Current money: ", money)
    else:
        break  # if bet is 0 or there are no money stop the machine
