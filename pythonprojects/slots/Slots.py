import Linkedlist
import Symbols
import Board

ketchup = Symbols.Symbol("k", 2, True)
maio = Symbols.Symbol("m", 1.9)
vinegar = Symbols.Symbol("v", 1.8)
gorchica = Symbols.Symbol("g", 1.7)
barbeque = Symbols.Symbol("b", 1.6)
ranch = Symbols.Symbol("r", 1.5)  # Symbols.Symbol creation the theme is sauces
tabasco = Symbols.Symbol("t", 1.4)  # odd are in players favor by small
garlic_sauce = Symbols.Symbol("s", 1.3)
olive_oil = Symbols.Symbol("o", 1.2)
sour_cream = Symbols.Symbol("c", 1.1)
money = 0
bet = 0
reel1 = Linkedlist.CircularlinkedList()  # creating a list with all them
for i in (ketchup, maio, gorchica, barbeque, ranch, tabasco, garlic_sauce, olive_oil, vinegar, sour_cream):
    reel1.add(i)
display = Board.Board(reel1)  # creating a board with all them

isValid = False
while not isValid:
    try:
        money = int(input("Enter starting amount money:"))  # imagine putting money into the game
        isValid = True
    except:
        print("Enter valid money!")

while 1:
    isValid = False
    while not isValid:
        try:
            bet = float(input("Place your bet to spin the wheel or press 0 to exit: \n"))
            isValid = True
        except:
            print("Enter valid bet!")

    # bet on current spin, for testing mode make that 1
    if bet != 0 and money >= 0:
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
        break  # if bet is 0 or we have no money we stop the machine
