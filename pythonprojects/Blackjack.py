import random


class Cards:  # each card has name, suit and power on black jack
    def __init__(self, name="", bjpower=0, suit=6):
        self.name = name
        self.bjpower = bjpower
        self.suit = suit

    def get_name(self):  # setters and getters to keep the encapsulation
        return self.name

    def get_bjpower(self):
        return self.bjpower

    def get_suit(self):
        return self.suit

    def __str__(self):  # overload to print member from cards
        if self.suit == 1:  # C for Clubs, D for Diamonds, H for Hearts and S for Spades
            return '%s%s' % (self.name, "-C")
        if self.suit == 2:
            return '%s%s' % (self.name, "-D")
        if self.suit == 3:
            return '%s%s' % (self.name, "-H")
        return '%s%s' % (self.name, "-S")

    def __repr__(self):  # overload to print member in a list from cards
        if self.suit == 1:
            return '%s%s' % (self.name, "-C")
        if self.suit == 2:
            return '%s%s' % (self.name, "-D")
        if self.suit == 3:
            return '%s%s' % (self.name, "-H")
        return '%s%s' % (self.name, "-S")


def make_deck(num, temp_deck=None):  # deck generating function
    if temp_deck is None:
        temp_deck = []
    for x in range(num):  # num, which is the total cards,should be dividable by 52, that would make num/52 decks in one
        if x % 13 == 0:  # method based on residue on division by 13
            temp = Cards("K", 10, x % 4)
        elif x % 13 == 1:
            temp = Cards("A", 1, x % 4)
        elif x % 13 == 10:
            temp = Cards("T", 10, x % 4)
        elif x % 13 == 11:
            temp = Cards("J", 10, x % 4)
        elif x % 13 == 12:
            temp = Cards("Q", 10, x % 4)
        else:
            temp = Cards(str(x % 13), x % 13, x % 4)
        temp_deck.append(temp)
    return temp_deck


def calc_score(hand=None):  # function that calculates the Blackjack score of a hand
    num_aces = 0
    score = 0
    for i in hand:
        if i.get_bjpower() != 1:  # ace is 11 or 1 if the score is above 21
            score += i.get_bjpower()
        else:
            num_aces += 1
            score += 11
    while num_aces > 0 and score > 21:  # score reduction if it is above 21
        num_aces -= 1
        score -= 10
    return score


def print_hand(hand=None):  # hand and score of the hand printer
    print(hand)
    print("Hand score is:", calc_score(hand))


def print_both(hand1=None, hand2=None):  # for printing both player's and dealer's hands
    print("Dealer's Hand:")
    print_hand(hand1)
    print("Player's Hand:")
    print_hand(hand2)


def is_pair(hand=None):  # binary check for pair in hand since the is a pair bet
    if hand[1] == hand[0]:
        print("You have a pair!")
        return True
    print("You have lost your pair bet!")
    return False


def print_statement(dealer_hand=None):  # interface statement print
    if dealer_hand[0].get_name() == 'A':  # if the dealer has ace players can bet on insurance 2 to 1
        return "Press 1-Hit ; 2-Stand ; 3-Double ; 4-Insurance:\n"  
    else:  # otherwise they can surrender and get half of their money
        return "Press 1-Hit ; 2-Stand ; 3-Double ; 4-Surrender:\n"  


def war(dealer_hand=None, player_hand=None):  # Blackjack war func
    print_hand(dealer_hand)
    print_hand(player_hand)
    if calc_score(player_hand) > calc_score(
            dealer_hand):  # the war is won only if the first player card is bigger than the dealer
        print("You win the war!")
        return True
    else:
        print("You have lost the war!")
        return False


def draw(hand=None, deck=None):  # function that draws card from the deck and adds it to the person's hand
    hand.append(deck[-1])
    deck.pop()


def draw_both(dealer_hand=None, player_hand=None, deck=None):  # same as above but for both players
    draw(dealer_hand, deck)
    draw(player_hand, deck)


def player_decision(dealer_hand=None, player_hand=None, deck=None):
    decision = 0  # function doing things depending on player's choices
    insurance_or_surrender = False
    is_double = False
    while decision != 2 and decision != 3:
        decision = int(input(print_statement(dealer_hand)))
        if decision == 1:  # if the player hits he takes card
            draw(player_hand, deck)
            print_both(dealer_hand, player_hand)
        if decision == 3:  # if the player doubles, he hits once with doubled bet
            is_double = True
            draw(player_hand, deck)
            print_both(dealer_hand, player_hand)
        if decision == 4:  # if the player wants an Insurance, he bets money on it
            insurance_or_surrender = True
            print_both(dealer_hand, player_hand)
        if calc_score(player_hand) >= 21:
            decision = 2
    return [insurance_or_surrender, is_double]


def dealer_draw(dealer_hand=None, deck=None):  # The dealer must draw at 16 and stand on 17
    while calc_score(dealer_hand) <= 16:
        draw(dealer_hand, deck)


def win_definer(player_hand=None, dealer_hand=None):
    if calc_score(dealer_hand) > 21 or (
            calc_score(dealer_hand) < calc_score(player_hand) and calc_score(dealer_hand) < 21):
        return 1  # player wins if the dealer busts or he has more points than the dealer
    if calc_score(player_hand) == calc_score(dealer_hand) <= 21:
        return 0  # if the points are even and below 21, there is a tie
    else:
        return 69  # in all other cases the player loses


def cheat(deck=None):  # function showing the deck if the cheat bet is activated
    print("Cheat code activated:")
    for j in range(len(deck)):
        print(deck[j], end=' ')
        if j % 31 == 30 or j == len(deck) - 1:
            print()


def main_loop(number_decks=0, money=0):  # main operating function
    deck = make_deck(52 * number_decks)  # depending on player's choice there are that many decks
    random.shuffle(deck)
    while money >= 0 and len(deck) > 0:
        print("Current money: ", money)
        bet = int(input("Place your bet: \n"))
        if bet == 69 or bet == 420:  # the cheat bets
            cheat(deck)
        if bet != 0 and bet <= money:
            war_bet = int(input("Do you want to put money on war, write how much, 0 if none:\n"))
            pair_bet = int(input("Do you want to put money on pair, write how much, 0 if none:\n"))
            money -= war_bet + pair_bet + bet
            ins_bet = 0  # the player puts his bets
            winner = False
            player_hand = []
            dealer_hand = []
            while not winner:
                if len(deck) <= 38: 
                    decks = make_deck(52 * number_decks)  # so if there are under 38 the deck is remade
                    random.shuffle(decks)
            # if the player has 21 aces and the dealer 17 aces, there will be 38 cards which is the maximum in 1 game
                
                draw_both(player_hand, dealer_hand, deck)

                if war_bet > 0:  # if the player has bet on war there is war
                    if war(dealer_hand, player_hand):
                        decision = input("Press y if you want to play the profit, any key to take it.\n")
                        if decision == 'y':  # player has choice between betting the profit or taking it
                            bet += war_bet
                            money += war_bet
                        else:
                            money += war_bet * 2
                draw(player_hand, deck)

                if pair_bet > 0:  # same as war bet
                    if is_pair(player_hand):
                        money += pair_bet * 6
                print_both(dealer_hand, player_hand)

                if calc_score(player_hand) == 21 and dealer_hand[0].get_bjpower != (1 or 10):
                    print("Blackjack! You win!")  
                    money += bet * 2.5
                    break  # if the player has 21 and dealer has no chance of having 21 in 2 cards there is a Blackjack

                decision = player_decision(dealer_hand, player_hand,
                                           deck)  # the house wins because the player has a choice
                if decision[1]:
                    money -= bet
                    bet *= 2
                    print(bet)
                if decision[0] and dealer_hand[0].get_name() == 'A':
                    ins_bet = bet
                    money -= bet
                elif decision[0]:  # surrender option
                    print("You Surrendered!")
                    money += bet / 2
                    break

                if calc_score(player_hand) > 21:
                    print("Bust! You lose!")
                    break

                dealer_draw(dealer_hand, deck)
                print_both(dealer_hand, player_hand)

                if ins_bet != 0 and calc_score(dealer_hand) == 21:
                    print("Insurance pays 2 to 1:")  # even if the player is above 21 insurance still exists
                    money += ins_bet * 2
                elif ins_bet != 0:
                    print("You've lost your insurance bet")

                if win_definer(player_hand, dealer_hand) == 1:  # check who wins and pay winnings
                    money += bet * 2
                    print("You win!")
                    winner = True
                elif win_definer(player_hand, dealer_hand) == 0:
                    money += bet * 2
                    print("Tie")
                    winner = True
                else:
                    print("You lose!")
                    winner = True


budget = int(input("Enter starting money:\n"))
num_decks = int(input("How many decks you want to play with? \n"))
main_loop(num_decks, budget)

        
