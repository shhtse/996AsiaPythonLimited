"""
====================================               ===============               =======================================
=========                           [  Multi-player with Betting Version ]                                     =========
=      [Main Classes]                             [Purpose]                                  [Related Function]        =
= ____________________________________________________________________________________________________________________ =
= |  1) Players          |       Constructing a player list to make for loop              |    class Players()        |=
= |     > Player         |          > function appending player list                      |      > class Player ()    |=
= |                      |                                                                |                           |=
= |______________________|_______________________________________________________________ |___________________________|=
= |  2) Deck             |       Constructing a card list through class Card(suit, value) |    class Deck()           |=
= |                      |       - shuffle                                                |    -shuffle(self)         |=
= |                      |       - drawings                                               |    -draw(self)            |=
= |     > Card           |           > function appending card list                       |                           |=
= |                      |                                                                |                           |=
= |______________________|_______________________________________________________________ |___________________________|=
= |  3) Hand             |       Pair up with class Players() applying every player       |    class Hand()           |=
= |                      |       - append card:                                           |    - add_card(self, card) |=
= |                      |       - adding point:                                          |    - add_pt(self)         |=
= |                      |       - showing card & point:                                  |    - show(self)           |=
= |______________________|_______________________________________________________________ |___________________________|=
= |  4) Chips            |                                                                |                           |=
= |______________________|________________________________________________________________|___________________________|=
= |  5) Game             |       Game Flow:                                               |     class Game()          |=
= |                      |       - starting the game                                      |    - start(self)          |=
= |                      |       - Drawing card twice                                     |    - draw_twice(self)     |=
= |                      |       - Checking Neutral BlackJack                             |    - checking_bj(self)    |=
= |                      |       - Stand and hit                                          |    - hit_and_stand(self)  |=
= |                      |       - Point Judgement                                        |    - point_judgement(self)|=
= |                      |       - Play Again                                             |    - play_again(self)     |=
= |______________________|________________________________________________________________|___________________________|=
=========                                                                                                      =========
====================================               ===============               =======================================
"""
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.chips = Chips()

    def __repr__(self):    # important
        return self.name

class Players:
    def __init__(self):
        n = 0
        while n < 5:
            try:
                self.players = [Player(input("name: ")) for i in range(int(input("player no.")))]
                self.move = self.players[:]
                self.survive = self.players[:]
                break

            except:
                print("\nplease enter number")
                n += 1
                if n == 2:
                    print("do you understand English?")
                if n == 3:
                    print("are you kidding me?")
                if n == 5:
                    print("Pass an IQ test first if you want to join the game")

    def __repr__(self):
        return self.players

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        self.fv = self.suit + self.value
        return self.fv

class Deck:
    def __init__(self):
        suit = ["♠", "♥", "♣", "♦"]
        face = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(s, f) for s in suit for f in face]

    def card_shuffle(self):
        if len(self.cards) > 0:
            random.shuffle(self.cards)

    def card_drawing(self):
        if len(self.cards) > 0:
            draw = self.cards.pop()
            return draw

class Hand:
    def __init__(self):
        self.point = 0
        self.card = []

    def append_card(self, card):
        self.card.append(card)

    def append_pt(self):
        self.point = 0
        own_A = False
        for card in self.card:
            if card.value.isnumeric():
                self.point += int(card.value)
            else:
                if card.value == "A":
                    self.point += 11
                    own_A = True

                else:
                    self.point += 10

        if own_A and self.point > 21:
            self.point -= 10
        return self.point

    def show(self, player):
        print(str(player) + ":   Card:  " + str(self.card) + "   Total Point: " + str(self.append_pt()))

class Chips:
    def __init__(self):
        self.chips = 1000
        self.bonus = Bonus()

class Bonus:
    def __init__(self):
        self.bonus = 0

    def add_bonus(self, chips):
        self.bonus += chips

    def del_bonus(self, chips):
        self.bonus -= chips

    def bonus_sharing(self, round_winner_list):   # Link to self.chips
        print("Current bonus" + str(self.bonus))
        average = self.bonus/len(round_winner_list)
        self.bonus -= self.bonus
        print("winner :" +str(round_winner_list))
        print("Each winning " + str(average) + "chips!")
        return average

class Game:
    def __init__(self):
        self.max_pt = []

    def start(self):  # Game Flow
        while True:
            self.deck = Deck()
            self.bonus = Bonus()
            self.p = Players()   # don't forget to add self.
            print("Participants in Game: " + str(self.p.players))
            self.fee()
            self.double_draw()
            self.check_bj()
            self.bet_hit_or_stand()
            self.round_winner()
            self.again()

    def fee(self):
        print("\nCollecting the participant fee")
        for player in self.p.players:
            fee = 50
            if player.chips.chips > fee:
                player.chips.chips -= fee
                self.bonus.add_bonus(fee)
                print(str(player) + "participate the game")
            else:
                print(str(player) + "quit the game")
                self.p.players.remove(player)
        print(self.bonus.bonus)

    def double_draw(self):
        for i in range(2):
            for player in self.p.players:
                if player == self.p.players[0]:
                    print("\nDistributing cards...")
                self.deck.card_shuffle()
                player.hand.append_card(self.deck.card_drawing())
                player.hand.show(player)

    def check_bj(self):
        for player in self.p.players:
            if player.hand.point == 21:
                print(str(player) + "gets a neutral Black Jack, congrats!!")
                self.again()

    def bet_hit_or_stand(self):
        while len(self.p.move) > 0:
            try:
                for player in self.p.move:
                    bet = input("\n" + str(player) + "   Would you like to bet?").lower()
                    if bet == "y":
                        types = input("\nWhich types of bet would you choose  ?   All-in/ Split/ Double Down/ Free-Bet").lower()

                        if types == "all-in":
                            while True:
                                try:
                                    if player.chips.chips > 0:
                                        all = player.chips.chips
                                        self.bonus.add_bonus(all)
                                        player.chips.chips -= all
                                        print(str(player) + "   bets   " + str(all))
                                        print(self.bonus.bonus)
                                        break
                                except:
                                    print("try again")

                        elif types == "split":
                            pass

                        elif types == "double-down":
                            pass

                        elif types == "free-bet":
                            while True:
                                try:
                                    amount = int(input("enter chips no."))
                                    if amount > player.chips.chips:
                                        player.chips.chips -= amount
                                        self.bonus.add_bonus(amount)
                                        print(str(player) + "  bets   " + str(amount))
                                        print(self.bonus.bonus)
                                        break
                                except:
                                    print("try again")

                    elif bet != "y":
                        print(str(player) + " not bet")

                    hit = input("\n" + str(player) + "   hit or stand or surrender?").lower()
                    if hit == "h":
                        player.hand.append_card(self.deck.card_drawing())
                        print(str(player) + "  Hit :   Card:  " + str(player.hand.card) + "   Total Point: " + str(player.hand.append_pt()))

                    elif hit == "s":
                        print(str(player) + "  Stand :   Card:  " + str(player.hand.card) + "   Total Point: " + str(player.hand.append_pt()))
                        self.p.move.remove(player)

                    elif hit == "sur":
                        print(str(player) + "  Surrender :   Card:  " + str(player.hand.card) + "   Total Point: " + str(player.hand.append_pt()))
                        self.p.move.remove(player)

                    else:
                        print(str(player) +"  sorry! I will not give u another choice")
            except:
                print("sorry! Try again")

    def round_winner(self):
        for player in self.p.players:
            if player.hand.point > 21:
                print(str(player) + "  Bust !!")
            else:
                self.max_pt.append(player)

        self.bonus.bonus_sharing(self.max_pt)

    def again(self):
        while True:
            again = input("Start a new game?").lower()

            if again == "y" or "yes":
                self.start()

            elif again == "n" or "no":
                print("See You")
                quit()

            else:
                print("try again!")

# call function
g = Game()
g.start()