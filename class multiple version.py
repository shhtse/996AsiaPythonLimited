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
import time

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
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
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
        print("winner :" + str(round_winner_list))
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
        print("\nCollecting the participant fee:...")
        print("侯賽因: 任何人有50 chips 都可以參加既今次黑色積克比賽")
        for player in self.p.players:
            fee = 50
            if player.chips.chips > fee:
                player.chips.chips -= fee
                self.bonus.add_bonus(fee)
                print(str(player) + "participate the game")
            else:
                print(str(player) + "quit the game")
                self.p.players.remove(player)


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
                        types = input("\nWhich types of bet would you choose  ?   All-in/ Split/ Double-Down/ Free-Bet").lower()
                        if types == "all-in":
                            while True:
                                try:
                                    if player.chips.chips > 0:
                                        all = player.chips.chips
                                        self.bonus.add_bonus(all)
                                        player.chips.chips -= all
                                        print(str(player) + "   bets   " + str(all))
                                        break
                                except:
                                    print("try again")

                        elif types == "split":
                            print("Public Security guides came near")
                            time.sleep(1)
                            print("\033[31;1m 同志 ,你涉嫌分裂国家 颠复国家政权, 跟我们回去接受阳光司法\033[0m")
                            time.sleep(2)
                            print("\n" + str(player) + " is arrested and quit the game")
                            time.sleep(1)
                            self.p.move.remove(player)
                            self.p.players.remove(player)
                            time.sleep(1)
                            print(str(player) + "'s chips is confiscated")
                            time.sleep(1)
                            print("Dealer: Country Safety is prior than everything, include money!")
                            time.sleep(1)
                            print("\n\nRemaining player:" + str(self.p.players))
                            continue

                        elif types == "double-down":
                            print("When you reply, 侯賽因問:船駛到了公海 ?")
                            time.sleep(1)
                            print("侯賽因: 這裡是公海, 我殺人都不用坐監")
                            time.sleep(1)
                            print(player, "quit the game and go to heaven")
                            time.sleep(1)
                            print(player, "s chips is confiscated by 侯賽因")
                            time.sleep(1)
                            self.p.move.remove(player)
                            self.p.players.remove(player)
                            continue

                        elif types == "free-bet":
                            while True:
                                try:
                                    amount = int(input("enter chips no."))
                                    if amount > player.chips.chips:
                                        player.chips.chips -= amount
                                        self.bonus.add_bonus(amount)
                                        print(str(player) + "  bets   " + str(amount))
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
        if self.p.players:
            for player in self.p.players:
                if player.hand.point > 21:
                    print(str(player) + "  Bust !!")
                else:
                    self.max_pt.append(player)

            self.bonus.bonus_sharing(self.max_pt)

        else:
            print("\n\nAll player are sent to jail or Heaven !!!!")
            time.sleep(1)
            print("As no player remain in the game:")
            time.sleep(2)
            print("\n\n"
"""\033[33;1m
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0xc..oKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXk:.     .cONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXko,.          ,lOXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKko:'...              .;okKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNK0koc;........                  .':lxOKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKOxol:,...                                   .',:ldkKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0xc;..                                                  .'cxKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0o;.                                                           .;d0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKd;.                                         '::;;,'..               .:kXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0l.                                          .:OXNXXXK0kdl;.              ,dXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKl.                    ...,:cloodooooollllccccokKXXXXXXXXXXXKOo;.             'xXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx'              ..,;clodkO0KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKkl'             ,OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKc.           .'cdk0KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0d;.           .oXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO,           .:x0KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0x:.           ;0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWk.          .ckKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKkc.          ,OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx.         .:kKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKOc.         'OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWk.          .xKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKx,         ,0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0,            ,kKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKO;         cNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXc             .dKKKKKKKKKKKKKKKKKK0000KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0000KKKKKKKKKO;        .OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx.             'kKKKKKKKKKKKKKKOdl:;,,;;:cdOKKKKKKKKKKKKKKKKKKKKKKKKkoc:;,,,;:ox0KKKKKKx.        :XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK;              c0KKKKKKKKKKKKkc'...''''....:OKKKKKKKKKKKKKKKKKKKKKKx;....'''....,oOKKKK0:        .dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd.              .,,:d0KKKKKKKd,':ldkOOOOkxdox0KKKKKKKKKKKKKKKKKKKKKK0xodxOOOOOkdl;':kKKKKOc.       ,0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK;                   .oKKKKKKOookKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0xod0KKKKKOl.      cXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx'                   .oKKKKKKK0KKKK0koc:;;;:cdOKKKKKKKKKKKKKKKKKKKKOxdolccccloxOKKKKK0KKKKKKKOo.     .OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNl.              ..',cx0KKKKKKKKKKkc'.   ...   .:kKKKKKKKKKKKKKKKK0o.           .cOKKKKKKKKKKKK0:      oWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK:.         .,coxO00KKKKKKKKKKKKK0l. .',,,''..  .d0KKKKKKKKKKKKKKKKx:;,'.'',;::,.cOKKKKKKKKKKKK0c      ;XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWk'        .lkKKKKKKKKKKKKKKKKKKKKKOxl;.         'd0KKKKKKKKKKKKKKKK0x:.      .'cdOKKKKKKKKKKKKK0c      .OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx.      .lOKKKKKKKKKKKKKKKKKK0o:;;::.  .:oxxxoc:lx0KKKKKKKKKKKKKKKK0kl'.,:cc;.  .cddolccdOKKKKKKl      .kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWo.     .dKKKKKKKKKKKKKKKKKKKKk;...   .:x0KKKKKKK0kdl:;o0KKKKKKKKKKKKK0kxOKKKKOc.        .dKKKKKKl.     .dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNc      ;OKKKKKKKKKKKKKKKKKKKKK0Okkxxxko''lk0Okdc'.    ;OKKKKKKKKKKKKOc...,:clloolcccloddk0KKKKKKo.      lWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK;     ,kKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKo.  ....      .cOKKKKKKKKKKKKK0o'.       'xKKKKKKKKKKKKKKKo.      cNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0xdxkOKNW0'    .lKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKkl;..    .,:lOKKKKKKKKKKKKKKKKK0xoc:;,'';xKKKKKKKKKKKKKKKo.      ;0K00OO0KNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOc;:loolclo;     .lKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0kxddxO0KKKKKK0koc:::cdOKKKKKKKKKKK00KKKKKKKKKKKKKKKKKo.       .':looollo0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx;:x0KKKKOd:.     .oKKKKKKKKKKK00000000000KKKKKKKKKKKKKKKKKKKKKKKKK0d,.       'dKKKKKKKKKKKKKKKKKKK0000000000o.        .xKKKK0xc;xNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0::kKKKKKKKKk,     .oKKKKKKKKKK000000KKKK0000KKKKKKKKKKKKKKKKKKKKKKOc.  'codl.  .:lok0KKKKKKKKKKKK000000KKKK00d.        'kKKKKKKO::0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWk:o0Kkdllok00:     .oKKKKKKKK0000000KXXXXK0000KKKKKKKKKKKKKKK0Odol;.   :OKKKKx,.    .,lkKKKKKKKKK000000XXXXXK0d.        .clccokKKd;xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx:xKx;....,lx:     .oKKKKKKKK0000000KXXXXK00000KKKKKKKKKKK0xc,.      .:OKKKKKK0xolc'.  .;d0KKKKKK000000KXXXXK0d.         .....;xKx:dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx:x0l,;::;'':'     .oKKKKKKKK000000000000000000KKKKKKKKKkl'   .';:ldxk0KKKKKKKKKKKK0xc.   'lOKKKK0000000000000x.         .;:::;o0k;lXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMOcd0dokkkxl,'.     .oKKKKKKKK00000000000000000KKKKKKKKOc.  .,lk0KKKKKKKKKKKKKKKKKKKKKKOo,.  'o0KK0000000000000x.        .:kkkkox0d,lXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNxlOOxxkkOx:..     .oKKKKKKKKK000000000000000KKKKKKKKk,  .:x0KKKKKKKKKKKKKKKKKKKKKKKKKKK0d,  .:kKK000000000000x'        .lkkkxx00l,xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0ldKOkkkkx:..     .oKKKKKKKKKKK00000000000KKKKKKKKKO;  .o0KKKKKKKKKKKKKK0O00KKKKKKKKKKKKKOc.  'xKKK0000000000k'        .ckkkkOKx;cKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0::kK0OOOkl'      .oKKKKKKKKKKKKKKKK0KKKKKKKKKKKKK0c  .l0KKKKKKKKKKKK0d:'..,lOKKKKKKKKKKKK0d.  'kKKKKKKKKKKKKO,        .ckO00KOc,xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx;lOKKOOkxl.     .oKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKO,  'kKKKKKKKKKKKKKo.      :0KKKKKKKKKKKKKd'.'xKKKKKKKKKKKK0;         ck0KK0l,cKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXl,lOK0Okkx,     .oKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0o''o0KKKKKKKKKKKK0:       'kKKKKKKKKKKKKKKkxOKKKKKKKKKKKKK0;         :O0K0o,,xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO;'lOKOkOx,     .oKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK00KKKKKKKKKKKKKK0c       .xKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0:         :OK0o,'c0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXl',d00kOx,     .o0KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKo.      .oKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0:         ;OKx;.'lXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNo''o00OOx'     .o0KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKd.       lKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0:         ;OKd,',oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd',dK0Okx'     .o00KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKx.      .oKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0c         ;OKx;';xNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWd':kK0Okx'     .o00KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0l.    .:OKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKl         ;OKOc';kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx,cOK0Okd'     .o000KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKklc:lx0KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKl         ;OK0l';OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO;c0KK00x'     .lO000KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKo.        ,OK0l':0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdlOKKKKk,     .lOO000KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKo.        ,OKOc'lXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNkk0KK0d.     .lkOO00KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKo.        'kOo;:0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXKK0kl.     .lkkOO00KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKo.     ':,:oddkXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNx.    .lkkkOO000KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKd.     dWWNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX:    .lkkkkOO000KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKd.     dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX:    .lkkkkkOO000KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKx.     dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX:    .lkkkkkkOO00000KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKx.     dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX:    .lkkkkkkkOOO0000KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKx.     dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX:    .lkkkkkkkkkOO00000000000000000000000000000KKKKKKKK000000000000000000000000000000000000000000x'     dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX:    .lkkkkkkkkkkOO000000000000000000OxdxO0000000000000000000000000000000000000000000000000000000x'     oWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX:    .lkkkkkkkkkkkkOO000000000000000d,. ..lO0000000000000000000000000000000000xlcok00000000000000x'     oWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX:    .;loxkkkkkkkkkkOO0000000000000O;     .d000000000000000000000000000000000d.   ;k00000000000OOx'     oWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX:       ..cxkkkkkkkkkkOO00000000000k;      c000000000000000000000000000000000l.   .x000000000OOOkx,     oWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNl         .:xkkxkkkkkkkkOO0000000000l.     'x000000000000000000000000000000ko'    ,k0000000OOOkkkx;     :XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMk.         'dxxxxxxxxkkkkkOOO0000000k,      ;k000000000000000000000000000kc.     .o000000OOOkkkkkxl.    lNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK,         .cxxxxxxxxxxkkkkkOOO000000d.      :O000000000000000000000000Od,       'x0000OOOkkkkxxxx:.   'OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWo          'dxxxxxxxxxxxxkkkkOOOO000Oo.      .;lxkO0000000000000000Oxc'         ;k0OOOOkkkxxxxxd:.   'OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0'          :dxxxxxxxxxxxxxxkkkkOOOO0Ol.        ...;ldkOOOOOOkxdoc;'.          ,dOOOkkkkxxxxxxd;.   .dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMWXOkO0K0xoodkXWMMMMMMMMMMMMMMWNXKXNWMMMMMMMMMMMMMMMMMMMMMMMMK:          .lxxxxxxxxxxxxxxxxxkkkkOOOOo.             .........              .cxOkkkkxxxxxxxxd;     ;KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMW0xl;'',,,'.,:;,:dKWMMMMMMMMMMMNOdlccdKWMMMMMMMMMMMMMMMMMMMMMWKd:.          .lxxxxxxxxxxxxxxxxxxxkkkkOko,.                               .,cxkkkxxxxxxxxxxxd;.    ,0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MW0o,.';codl:;cdOOxl::d0NWMMMMMMW0oclol:;lONMMMMMMMMMMMMMMMMMWWN0o::,.          .lxxxxxxxxxxxxxxxxxxxxxkkkkxoc,.                         .'cdkkkxxxxxxxxxxxxdl'     .xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
Wk;..;okOOOOOkOOOOOOkoc:cokO0KK0d::dOOkl;;:oO00KKK000000Okxddlc:,''''..          .ldxxxxxxxxxxxxxxxxxxxxxxxxkkkxo:,'..               ..,:oxkxxxxxxxxxxxxxxdo;.     .lNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
WKo,':dkOOOOOOOOOOOOOOOxdlc:::c:coxOOOOdc,..''''''''''''''....        .           .cdxxxxxxxxxxxxxxxxxxxxxxxxxxxxkxxxol:;,'''..'',;:codxxxxxxxxxxxxxxxxxxd:.      .oXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMN0l,':oxOOOOOOOOOOOOOOOOkkkkkkOOOOOOOkl'...     ..                                ,odxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdddddxxxxxxxxxxxxxxxxxxxxxxxxl.      .kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMN0o,',cdkOOOOOOOOOOOOOOOOOOOOOOOOOko,...                                         .,codxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdl,       ;KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMWKxc'';cdkOOOOOOOOOOOOOOOOOOOOOOd;...                                             .';:lodxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdol;..        .;dKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMNk:'.';coxkkOOOOOOOOOOOOOOOOx:...                                                   .',;cloddxxdxxddxxxxxxxxxxxxxxxxxxxxxddxxxdxxxxdddoc:;'.               .;o0NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMWXkl;,'',;cldxkkOOOOOOOkxolc'...                                                         ..',;;:cclllllllllllllllllllllllllcc::;;,'...                       .,:dKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMWNK0Oxdoc;,;;:ccccc:;,,,'....                                                                                                                                 .:o0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMWKkdolc::ldxxxkd,...                                                                                                                                     .,dKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMWWWNWMMMMMK:...                                                                                                                                        .,lk0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK:..                                                      .''.                                                                                   .,ld0NWMMMMMMMMMMMMMMMMMMMMMWWWNXNMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK:..                                                      .oXK0kdlc;.                ......                                                          .':o0WMMMMMMMMMMMMMMMNKOdllc:oXMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK:..                                                       oWMMMMMWk;................;dKXX0l.                                                            oNMMMMMMMMMMMMMN0o:,;:odoco0WMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK:..                                                    .;xXMMMMMMW0:'.......'.......'oNMMMW0o;.                                                        cXMMMMMMMMMMMWXkl;;coxxkxo:,dNMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXo....                                             .':oOXWMMMMMMMMMWKd;'......'''...,l0WMMMMMMWKd'                                                     .;lxXMMMMMMWXOo::coxxxxxxl,'oNMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0o:,...                                      .clld0NWMMMMMMMMMMMMMMMNk:'..''.....':kNWMMMMMMMMMMKl.                                                     ..,oO0KKOo:,:ldxxxxxxxc''l0WMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKOdl:'..                                  .xWMMMMMMMMMMMMMMMMMMMMMWKl'...'''.,oKWMMMMMMMMMMMMMW0oc;.                                                .'.....'..';ldxxxxxxxxo,.:kXWWWMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKkdc,..                               cNMMMMMMMMMMMMMMMMMMMMMMXo'.....''oXMMMMMMMMMMMMMMMMMMWd.                                               .,ool;'.',;ldxxxxxxxxxxo;..,:cllodxkO00XWMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0xoc;'..                         .dNMMMMMMMMMMMMMMMMMMMMNd,....'..'dNMMMMMMMMMMMMMMMMMWx.                                               .:dxxxdolloxxxxxxxxxxxxxxoc:;,,,'''''''';xNM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXOxl'                        .lXMMMMMMMMMMMMMMMMMMMNo'.......'dNMMMMMMMMMMMMMMMMWx.                                                .oxxxxxxxxxxxxxxxxxxxxxxxxdolllooooolc;..;0M
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWK:.                       .xMMMMMMMMMMMMMMMMMMWXd,.......,dXWMMMMMMMMMMMMMMWk.                                            ',...:dxxxxxxxxxxxxxxxxxxxxxxxxo;...'',,;,,';lONM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOc.                       :XMMMMMMMMMMMMMMMMW0l,...'..'.',l0WMMMMMMMMMMMMWO'                                          .:kNWXOdocldxxxxxxxxxxxxxxxxxxxxxdol:;'......'oXWMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd.                       .xWMMMMMMMMMMMMMMMKc'...........'lXMMMMMMMMMMMM0,                                   '.   .;dKWMMMMMWNOdlccldxxxxxxxxxxxxxxxxl,,;:ccc:;,'..cKWMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0:..                       ,0MMMMMMMMMMMMMMXo,.....'.....'.;OWMMMMMMMMMMK;                                    .ddlo0WMMMMMMMMMMMMN0xoc:ldxxxxxxxxxxdddo:'....',;;;'.'dWMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXl..                         lNMMMMMMMMMMMWKo'...'..'.''....'lKWMMMMMMMMNl                                      oWMMMMMMMMMMMMMMMMMMMWKc,lxxxxxxxxdl;;:loolc;,.....,:xXMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd,.                          .dWMMMMMMMMMMNd,................,dNMMMMMMMWd.                                      ;XMMMMMMMMMMMMMMMMMMMMWO;;oxxxxxxxdc'...',;:c:;'.,xXNMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNKOOkxxxdddddddddooooolllllllllxNMMMMMMMMMMNkollllllcccccccccccdXMMMMMMMK:..........                             ,0MMMMMMMMMMMMMMMMMMMMMW0c;:clodddddc'......''',l0WMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWWWWWWWWNNNNNNNWWMMMMMMMWXKKKKKKKK00000OOOOOOOOkkkkkxxxxxxxddddddkNMMMMMMMMMMMMMMMMMMMMMMMXkdlc;;;:clolc;..,xKKKXWMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNX0xl:;,,,;''oXMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWX0kdlo0NMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0l;;;;:xNMMMMMMW0xddddddddddddddddddxKWMMMMMMMMMMMMMMMMMMMMMMWMMNkc:cccxNMNKOO0OOOO0OOOOOOO0XWMMMMMMMMMMNOdddddddddddkNMMMKl;;;;;xNMMMMMMXdcc::cxNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWd.     :XMMMMMM0,                    cXMMMMMMMMMXd::::::::::::::,.     ,0Wx........... .....;KMMMMMMMMMMO'           .xMMWd.     ,KMMWXKKo.     .dKXNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0dooool,      .cooodKM0,                    :XMMMMMMMMMK,                     cXWd.                '0MMMMMMMMMMk.           .xW0:.      .;0Wk'..        ...cXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMNc                   lNNOooooooooo:.      ,od0WMMMMMMMMMWx,......       ....';dXMWo.      ,cc:.     '0MMMMMMMMMMk.    ,l;    .xWd.        .xWo.             ,0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMNl                  .oWMMMMMMMMMMMK,     .xMMMMMMMMMMMMMMWNXXXXXx.     .xXXXNWMMMWd.     '0MMWd.    '0MMMMMMMMMMk.   .xMO.   .xWk'        'kW0c;;;;;;;;;;;;;dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKkxxxxd;      .lxxxkXMMMMMMMMMMMMK,     .xMMMMMMMMMMMMMKdoooooo;.     .;ooooooOWWd.     ,0MMWd.    '0MMMMMMMMMMk.   .kMO.   .xMWKl.     'OWMMWWWWWWWWWWNNNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx.     :XMMMMMMMMMMMMMMMMMK,     .xMMMMMMMMMMMMWo                      ,KWo.     ,0MMMd.    '0MMMMMMMMMMk.   .kMO.   .xMMMx.     ;KMMKoc:lOWMMKl;;;cOWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx.     :XMMMMMMMMMMMMMMMMMK,     .xMMMMMMMMMMMMWo.                     ;KWo.     ,0MMMd.    '0MMMMMMMMMMk.   .kMO.   .xMMMx.     ;KMMx.   cNMWd.    oWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx.     :XMMMMMMMMMMMMMMMMMK,     .xMMMMMMMMMMMMMXkxxxxxxc.     .cxxxxxx0WWo.     ,0MMMd.    '0MMMMMMMMMMk.   .kMO.   .xMMMx.     ;KMMO.   ;KMWl    .xMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx.     'oxlcl0MMMMMMMMMMMMK,     .xMMMMMMMMMMMMMMN0xxONMO'     'OMW0kxONMWo.     ,0MMMd.    '0MMMMMMMMMMk.   .kMO.   .xMMMx.     .oXM0'   ,0MNc    .kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXl.          .xMMMMMMMMMMMMK,     .xMMMMMMMMMMMMMMO'  .kMO'     'OM0'  .xWWd.     ,0MMMd.    '0MMMMMMMMMMk.   .kMO.   .xMMWd.      .dWK,   .OMK;    '0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKOdl:'.           .xMMMMMMMMMMMMK,     .xMMMMMMMMMMMMMMk.  .xMO'     'OMO.  .dWWd.     ,0MMMd.    '0MMMMMMMMMMk.   .kMO.   .xW0c.       .dWX:   .kM0'    ;XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMO;.               .'lKMMMMMMMMMMMMK,     .xMMMMMMMMMMMMMMk.  .xMO'     'OMO.  .dWWo.     ,0MMMd.    '0MMMMMMMMMMk.   .kMO.   .xNl         ,OMNc   .dWk.    cNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMWo.             .lOKNWMMMMMMMMMMMMMK,     .xMMMMMMMMMMMMMMk.  .xMO'     'OMO.  .dWWd.     ,0MMMd.    '0MMMMMMMMMMk.   .kMO.   .xNl        'OWMWo    oWx.    oWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMWo.  ..,;.      :XMMMMMMMMMMMMMMMMMK,     .xMMMMMMMMMMMMMMk.  .xMO'     'OMO.  .dWWd.     ,0MMMd.    '0MMMMMMMMMMk.   .kMO.   .xWkc'      ;KMMWd.   cXo    .xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMM0ooxOKNWd.     :XMMMMMMMMMMMMMMMMMK,     .xMMMMMMMMMMMMMMk.  .xMO'     'OMO.  .dWWd.     ,0MMMd.    '0MMMMMMMMMMk.   .kMO.   .xMMWx.     ;KMMMx.   .c,    .kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx.     :XMMMMMMMMMMMMMMMMMK,     .xMMMMMMMMMMMMMMk.  .xMO'     'OMO.  .dWWd.     ,0MMMd.    '0MMMMMMMMMMk.   .kMO.   .xMMMx.     ;KMMMO.          '0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMx.     :XMMMMMMMMMMMMMMMMMK,     .xMMMMMMMMMMMMMMk.  .xMO'     'OMO.  .dWWo.     ,0MMWd.    '0MMMMMMMMMMk.   .kMO.   .xMMMx.     ;KMMMNd.         ;KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx.     :XMMMMMMMMMMMMMMMMMK,     .xMMMMMMMMMMMMWXl.  .xMO'     'OMO.  .dWWd.     ,0MMMd.    '0MMMMMMMMMMk.   .kMO.   .xMMMx.     ;KMMMMWKxol'     :XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNNX0:      :XMMMMMMMMMWNXXXXXKd.     .xMMMMMMMMMMMMXc    .xMO'     'OMO.  .dWWd.     .xXXKc     '0MMMMMMMMMMk.   .oKo.   .dWW0c      ;KMMNXXXXXKl.    :KWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd'...       :XMMMMMMMMXl'......       .kMMMMMMMMMMMMNc    'OMO'     'OMO.  .dWWd.      ....      '0MMMMMMMMMMk.    ...    .xWk'       ;XM0:......       .lXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNl          .dWMMMMMMMMNc              :KMMMMMMMMMMMMMOc,;lOWMO'     'OMXl,,c0MWo.                ;KMMMMMMMMMMk.           .OMO.      .dWMk.              ,0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0c,''''',;lOWMMMMMMMMMWO:'''''''''',cxXMMMMMMMMMMMMMMMWWWMMMMXl,''',lXMMWWNWMMWO:''',''''''',',:oKWMMMMMMMMMMKc'''''''',;lOWMNd,'',;lOWMMKc,'''''''''''',oXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNNNNNNNWMMMMMMMMMMMMMMWNNNNNNNNNNWMMMMMMMMMMMMMMMMMMMMMMMMMMWNNNNNWMMMMMMMMMMMWNNNNNNNNNNNNNWWMMMMMMMMMMMMMMWNNNNNNNNNWMMMMMWWNNNWMMMMMMWNNNNNNNNNNNNNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNK0OkkkkkkkkkkkkkkOKNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOo:'..               ..,lONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0:.                        .lXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX:        ............        lNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO.      ;kKXXXXXXXXXX0l.      ;XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMx.     .xWMMMMMMMMMMMMNOdddddx0WMMMMMMMMW0dddx0WMMMMMMMMMKxdddONMMMMMMXkddddddddddddddddxkKNMMMMMMMWOdddddddddddddddddd0WMMMMMMNOddddddddddddddddxkKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMk.      :0XNNNNNNNNNNNNNNNWMMMMMMMMMMMMMX:    cNMMMMMMMMWo    '0MMMMMWd.                  .;kWMMMMMK,                  ;KMMMMMMO'                  .:OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK;       ..''''''''''''''';cdKWMMMMMMMMMX;    :XMMMMMMMMWl    '0MMMMMWd.    ...........     'OMMMMMK,     .............cXMMMMMMO'    .,,,,,,,,,.     :XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWk'                          .oXMMMMMMMMX;    :XMMMMMMMMWl    '0MMMMMWd.   .dKKKKKKKKKO;    .xMMMMMK,    :0KKKKKKKKKKKKNWMMMMMMO'   .oNWWWWWWWNk'    :XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKo;..                       .dWMMMMMMMX;    :XMMMMMMMMWl    '0MMMMMWd.   .OMMMMMMMMMWd.   .xMMMMMK,    :0XXXXXXXXXXXWMMMMMMMMO'   .dWMMMMMMMMK,    :XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXKOkkkkkkkkkkkkkkd:.      :XMMMMMMMX;    :XMMMMMMMMWl    '0MMMMMWd.   .:dddddddddl'    .kMMMMMK,    ............'oNMMMMMMMO'    'clllllllc,    .dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXkxxxxxONMMMMMMMMMMMMMMK,      :XMMMMMMMX;    :XMMMMMMMMWl    '0MMMMMWd.                   .lXMMMMMK,                 :XMMMMMMMO'                   cXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNl      .oNWWWWWWWWWWWWNx.      :XMMMMMMMX;    :XMMMMMMMMWl    'OMMMMMWd.    .............,ckNMMMMMMK,    ,dxxxxxxxxxxx0WMMMMMMMO'    .,;;;;;;;,.    .dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNl       .';;;;;;;;;;;;'.       cNMMMMMMMX:    .kNMMMMMMW0;    ,0MMMMMWd.   .dKXXXXXXXXXXXNWMMMMMMMMK,    cNMMMMMMMMMMMMMMMMMMMMO'   .oNWWWWWWWNO,    ;KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO,                            .kWMMMMMMMWx.    .,:ccccc;.    .lNMMMMMWd.   .OMMMMMMMMMMMMMMMMMMMMMMK,    .:ccccccccccccl0WMMMMMO.   .dWMMMMMMMMNl    ;KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0l.                         ,kWMMMMMMMMMNx'                .oXMMMMMMWd.   .OMMMMMMMMMMMMMMMMMMMMMMK,                   oWMMMMMO'   .dWMMMMMMMMNl    ;KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXkoc:;;;;;;;;;;;;;;;;;:cokXMMMMMMMMMMMMMXkl:,,,,,,,,,,;cd0WMMMMMMMMO:'',cKMMMMMMMMMMMMMMMMMMMMMMXo,,,,,,,,,,,,,,,,,,;kWMMMMMKl,,':OMMMMMMMMMWx;,',oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWWWWWWWWWWWWWWWMMMMMMMMMMMMMMMMMMMMWWNNNNNNNNWWMMMMMMMMMMMMWWNNNWMMMMMMMMMMMMMMMMMMMMMMMMWNNNNNNNNNNNNNNNNNNWWMMMMMMMWNNNWWMMMMMMMMMMWWNNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM

\033[0m
""")

    def again(self):
        while True:
            if not self.p.players:
                print("Be careful of what you say next time")
            again = input("Start a new game?").lower()

            if again == "y" or "yes":
                self.start()

            elif again == "n" or "no":
                print("See You")
                quit()

            else:
                print("try again!")

# call function
time.sleep(2)
print(
"""\033[34;1m
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx'  .::.    'c'   ;OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKc.  'c;       .c:.  .oXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXd.  .;:.          ,c'   ,kNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx,   ':,             .;;.  .:OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX00KWMMMMMMMNk;   .;,.                .;,.  .c0WMMMMMMMWK00XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWMMMMKocd:.;OWMMMWO:.  .;,.                    ';,.  .lKWMMMWO;.:dcoXMMMMWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXko:,;clkXXc.oO,  lNMNO:.  .;,.                        ';,.  .l0WMNc  ;0o.cXXkl:;,:oOXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXxdd'.:xxoc:;.:XNx:oKXk;.  ';,.                            .;;.  .cON0l:xNK;.;:coxx:.,ddxNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWo:0NkOWMMMW0; 'ONWWXx,  .,:,.                                ';;.  .:kNWWNk' :0WMMMNOON0:dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNl'coOWMMMMMMO' .,;;.  .,:,.                                    .;:'  .';;,. '0MMMMMMWOoc'oWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0:. .lKWMMMMK;      .;:,.                                        .;:'       ;XMMMMWKl. .cKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNkc..'cx0NM0'    .;:'                                             .;:,.    ,0MN0dc'.'cONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0OOKNXx,   ':;.                                                 .,:;.   ;kNNKOO0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0o'  .,:,.                                                      ';;.   ,xXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0kkxxkxxd:.   ';'.                                                          .,'    .lxxxxxkxkXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK;.loooooollllll;. .;lllll;.            .cllllllllll'         .:ldxxxoc,.,lllll;.     ,oooo:.:KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK;:XMMMMMWNNWMMWN0c;OMMMMMO.           .dWMMMMMMMMMMO.     .:kXWMMMMMMMXoxWMMMNc     ,0MMMKc:0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK;:XMMMMNd'':xXMMM0lOMMMMMO.           ;KMMMWXNWWMMMNl    ;ONMMMMMMMMMMNdxWMMMX:    ,0MMMXc.dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0;:XMMMM0,    lNMM0lOMMMMMO.          .kWMMXl.':xNMMM0,  cXMMMMMMWWMMMMKlxWMMMX:   'OWMMXl  .oXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNo.:XMMMM0'    cXMM0lOMMMMMO.          cNMMMO.   .xWMMWd.;KMMMMKd:;:lkNNd'dWMMMX;  .kWMMNo..   ,kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWK:  :XMMMMXc.':xXMMWkcOMMMMMO.         'OMMMWo     .xWMM0cxWMMMK;     .;:..dWMMMX: .oNMMNo..::.  .oXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWWk'   :XMMMMMXO0NMMMM0;,OMMMMMO.        .oNMMM0,      .xWMKoOMMMMx.         .dWMMMWXO0NMMWx.  .;c'   :0WWWNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXkodkkxo;.  ..:XMMMMNd..,oKWMNx:OMMMMMO.        ,KMMMXc        ,KMKokMMMMK:.     .'..dWMMMNxlxXMMM0;    .:;.  .:oxkxdokXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXo.  ;ONXc   ,;.:XMMMMX;    ;KMM0lOMMMMMO.       .xWMMMWOl::::cllkNMNddNMMMMN0o,',ckKl.dWMMMO. .lXMMMK;     ;:.  .oNXk,  'dXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO;'col'.;:.  ,:. :XMMMMXc    '0MM0lOMMMMM0,       :XMMMMMMMMMMMMMMMMMM0oOWMMMMMMWNNWMM0cxWMMMO.   :0WMMK:     ,:.  .c;.,lo:.:KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0;,OWMW0,    'c.  :XMMMMWOc,,cOWMM0lOMMMMMN0OkOOOl;kWMMMMNOkkOOOOOXWMMMW0okNMMMMMMMMMMMNdxWMMM0'    .dNMMK:     ;:.    :KMMWx':KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXc.lNMMMWx.  .:,   :XMMMMMMWNWWMMMM0lkNNNNNNNWWMMNdoKNNNNKl.       ;KMMMMWOcckKXWWWNNNNNKoxWMMWK:     .oNMMXc    .:,   .kMMMMX:.xMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNl.cXMMMWd.  ,:.   ,kKKKKKKKKKKK0Od,.lkkkkkkkox00dcdkkkkkxl:;.     .l00Okkkxdxkkkdldkkkkxcck0xlddl::;. ;OKKKk,    ,:.  .OMMMMK;.xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK;'kWMMX:   :;     .............   .kWWWWWWNl...,OWMWMMWWWWNl       .cxKNWMMMMMWklOWWWMWk'.. .dWMMWO'  .....     .c'   lNMMWx.:XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO;;OWMO.  .c'                     .kMMMMMMNl   lNMMMMWWMMMM0,     ,kNMMMMMMMMMM0o0MMMMMO.   ;KMMMK;              :;   ;KMNx,:KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKo;:l;   .c.                     .kMMMMMMNl  ,0MMMNd;:kNMMWd.   cKMMMMMMMMMMMM0o0MMMMWx.  :KMMMK:               ;:   .:l:;dXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0c.    .c.                     .kMMMMMMNl .dWMMWk.  .OMMMK;  :XMMMMMMWXK0XWNo:0MMMMX:  ,0MMMXc                ;:     .lKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx.   .l,                     .kMMMMMMNl ;XMMMK;   .dWMMWx,;xWMMMMNk:....cl.'0MMMWx. .xWMMXc                 c:    'kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWk'  .cc              .,,    .OMMMMMMNl'kWMMNl.    .kWMMOll0MMMMNl.        '0MMMMKockNMMNo.                .l,   ,0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWo   ,o'          .:OXNx.   .kMMMMMMNolXMMMk.      :XMM0oo0MMMMNc      .. '0MMMMMMWMMMMNd.                cl.  .kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK;   co.         'OMMM0;. .cKMMMMMM0oOMMMMNxcc::co0WMMXOoxWMMMMXo,..;dK0:,0MMMMXo:oKWMMNd.              ;d,   lNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0,  .ll.        .kMMMWX0OKNMMMMMMNdxNMMMMMMMMMMMMMMMMWWkoKMMMMMMNXXNMMWkc0MMMMK;  .xNMMWx.            ,d;   cXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0,  .cc.        :XMMMMMMMMMMMMMWOo0MMMMMNKKKKKKXWMMMMMNko0WMMMMMMMMMMM0o0MMMMWk.  .dNMMWk.          ,o,   cXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK:   ;c'        :0WMMMMMMMMMMMXoxWMMMMKc..,;...dNMMMMMWOloKWMMMMMMMMM0o0MMMMMO.   .kWMMWk'       .;c.  .lXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXo.  .;;.       .cx0NWWWWWNKkccOXNXNXo. 'c.   'kXNXXNXXo..cxKNWWWWNKd:kNNXXXx.    ;0XXNXd.    .,:'   'xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO;   .;;,.       ..,;;;,'.  .'''''...;:.     .,;'..,;.    .',:c;'. .,cllllc,... ........  .;;'   .cKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx,   .';;'.  ...',;cllodxxxo;.....:,   .;.  ':.  ,:.  .;.  .,,....:kXNNNNNXK0Okdoc:,..';,.   .:OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx,..';lxxxk0KXNWWMMMMMMMMWXx:....  'oKx.  ;c.  'l.  'O0c.  ....:ONMMMMMMMMMMMMMMWWXK0koc;',dXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXKXNWMMMMMMMMMMMMMMMMMMMMMW0:....oXWNc  .c;   .l;  .xWW0;. .'l0WMMMMMMMMMMMMMMMMMMMMMMMWNXXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKd;..ckXO'  ,l.    :l.  ;K0c..,:dKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWNO:...;,  .l:     .o;  .;:..,;:cok0KKXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNK0OOOOOOOOOOx;.  .'..cl.      ;o'  .'...  .cOKKKK0xooxk0KNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXO0WMMMMMMMMWNXK0kdl:,'.;d0KXXNNNX0d,.   ..:o.       .:c'.';loolc;;::cxXWKo.   .,dKXKO0KKKXXNWMMMWNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO:.,lk0Oxdollodo:'     .oKWMMMMN0o,.';,.   ,l,..',;:loxOKKXNNWMMMWKx:...;kNWKl.    'cdoollodkOXWN0ooXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0dolc:;;,,,;;:;.     .oKWMMMMMMKl'. ...,codkOO0KNWWWMMMMMMMMMMMMMMMMN0o,..lXMWKl.     .;:::coddxdoxXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
\033[0m
""")
input("                                                                           Press Enter"
      " to continue...")

g = Game()
g.start()
