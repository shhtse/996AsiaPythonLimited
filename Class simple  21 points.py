"""
====================================               ===============               =======================================
=========                                                                                                      =========
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
= |  4) Game             |       Game Flow:                                               |     class Game()          |=
= |                      |       - starting the game                                      |    - start(self)          |=
= |                      |       - Drawing card twice                                     |    - draw_twice(self)     |=
= |                      |       - Checking Neutral BlackJack                             |    - checking_bj(self)    |=
= |                      |       - Stand and hit                                          |    - hit_and_stand(self)  |=
= |                      |       - Point Judgement                                        |    - point_judgement(self)|=
= |                      |       - Play Again                                             |    - play_again(self)     |=
= |______________________|________________________________________________________________|___________________________|=
=                                                                                                                      =
=========                                                                                                      =========
====================================               ===============               =======================================
"""

import random

class Player:
    def __init__(self, name=""):
        self.name = name
        self.hand = Hand()

    def __repr__(self):
        return self.name

class Players:
    def __init__(self):
        self.player = [Player("Player" + str(i)) for i in range(5)]
        self.move = self.player[:]

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return " ".join((self.suit, self.value))

class Deck:
    def __init__(self):
        suit = ["♠", "♥", "♣", "♦"]
        face = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(s, f) for s in suit for f in face]

    def shuffle(self):
        if len(self.cards) > 0:
            random.shuffle(self.cards)

    def draw(self):
        if len(self.cards) > 0:
            draw = self.cards.pop()
            return draw

class Hand():
    def __init__(self):
        self.point = 0
        self.card = []

    def add_card(self, card):
        self.card.append(card)

    def add_pt(self):
        self.point = 0
        own_Ace = False
        for card in self.card:
            if card.value.isnumeric():
                self.point += int(card.value)
            else:
                if card.value == "A":
                    self.point += 11
                else:
                    self.point += 10

        if own_Ace and self.point > 21:
            self.point -= 10
        return self.point

    def show(self, player):
            print(player, "Card:  ", self.card, "Point:  ", self.add_pt())

class Game:
    def __init__(self):
        pass

    def start(self):
        loop = True
        while loop:
            # call class function
            self.deck = Deck()
            self.player = Players()
            self.deck.shuffle()
            print("\nPlayer in Black Jack: " + str(self.player.player))
            self.draw_twice()
            self.checking_bj()
            self.hit_and_stand()
            self.point_judgement()
            self.play_again()

    def draw_twice(self):
        for i in range(2):
            for player in self.player.player:
                if player == self.player.player[0]:
                    print("\n")
                player.hand.add_card(self.deck.draw())
                player.hand.show(player)
        # check for neutral BlackJack

    def checking_bj(self):
        for player in self.player.player:
            if player.hand.point == 21:
                print(str(player) + "won a neutral BlackJack! Congrats!")
                self.play_again()


    def hit_and_stand(self):
        while len(self.player.move) > 0:
            for player in self.player.move:
                if player == self.player.player[0]:
                    ask = input("\nHit or Stand? ").lower()
                    if ask == "h":
                        player.hand.add_card(self.deck.draw())
                        print(str(player) + "  Hit" + " Card :" + str(player.hand.card) + " Total Point:  " +
                                   str(player.hand.add_pt()))

                    elif ask == "s":
                        print(str(player) + "  Stand")
                        self.player.move.remove(player)

                    else:
                        print("sorry")

                elif player != self.player.player[0]:
                    if player.hand.point < 17:
                        player.hand.add_card(self.deck.draw())
                        print(str(player) + "  Hit" + " Card :" + str(player.hand.card) + " Total Point:  " +
                            str(player.hand.add_pt()))

                    else:
                        print(str(player) + " Stand")
                        self.player.move.remove(player)

    def point_judgement(self):
        max_pt = []
        for player in self.player.player:
            if player.hand.point > 21:
                print(str(player) + "  Busted !")
                continue
            max_pt.append(player.hand.point)
        for player in self.player.player:
            if player.hand.point == max(max_pt):
                print("winner is/are :", str(player))

    def play_again(self):
        while True:
            again = input("\nWould you like to play again?")
            if again == "y":
                self.start()

            elif again == "n":
                print("See You")
                quit()
            else:
                print("sorry, please try again!!")

g = Game()
g.start()