from Linkedlist import CircularlinkedList
from Symbols import Symbol
from Board import Board
from results_container import Resulter


def main_game(bet=0, money=0):
    ketchup = Symbol("k", 4, True)
    maio = Symbol("m", 1.9)
    vinegar = Symbol("v", 1.8)
    gorchica = Symbol("g", 1.7)
    barbeque = Symbol("b", 1.6)
    ranch = Symbol("r", 1.5)  # Symbols.Symbol creation the theme is sauces
    tabasco = Symbol("t", 1.4)  # odd are in players favor by small
    garlic_sauce = Symbol("s", 1.3)
    olive_oil = Symbol("o", 1.2)
    sour_cream = Symbol("c", 1.1)
    reel1 = CircularlinkedList()  # creating a list with all them
    for i in (ketchup, maio, gorchica, barbeque, ranch, tabasco, garlic_sauce, olive_oil, vinegar, sour_cream):
        reel1.add(i)
    display = Board(reel1)  # creating a board with all them
    winning_lines = []  # saves each line's winning

    if bet != 0 and money > 0:
        display.random_spin_board()  # spin the board
        first = display.line1()
        second = display.line2()
        third = display.line3()
        display.print_board()  # print it
        total = bet * first + bet * second + bet * third  # total winnings if they exist

        if total > 0:
            if first > 0:
                print("Line 1:", bet * first)  # there are still things printed in the console for testing
                winning_lines.append(bet * first)
            else:
                winning_lines.append(0)  # 0 meaning there are no winnings on that line
            if second > 0:
                print("Line 2:", bet * second)  # shows player which line is the lucky one
                winning_lines.append(bet * second)
            else:
                winning_lines.append(0)  # 0 meaning there are no winnings on that line
            if third > 0:
                print("Line 3:", bet * third)
                winning_lines.append(bet * third)
            else:
                winning_lines.append(0)  # 0 meaning there are no winnings on that line
                print("You win: ", total)
                money += total
        else:
            print("You lose!")
            for i in range(0, 3):
                winning_lines.append(0)  # three 0 meaning there are no winnings on any line
            money -= bet  # losing money
        print("Current money: ", money)
        board_in_list = display.get_board_in_list()
        result = Resulter(total, winning_lines, board_in_list)
        return result
