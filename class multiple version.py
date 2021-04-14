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
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNO:'..l0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKko;.     .;okKNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXKOxdc,..            .,:oxOKXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKkl;'..                        ..;lkXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXk:.                      .,,'..       .lONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXd'           ..',,,,,,,''':kKKK0kd:.      .;kNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO,      .';cloxkO0KKKKKKK00KKKKKKKKKKOd;.     .cKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd.     .cx0KKKKKKKKKKKKKKKKKKKKKKKKKKKKK0x:.     'kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNl.    .cOKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKkc.    .xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNo.     .xKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKx'    .OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWk.      .oKKKKKKKKOxdddk0KKKKKKKKKKKKKK0kdddxOKKKx'    cXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX:       .lO0KKKKkl:;::;;lOKKKKKKKKKKKKOl;;::;:lkKKl.   .xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWk.         .c0KK0xdk00OOkOKKKKKKKKKKKKKKOOO000kdx0K0x;   ,0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNl        ..,o0KKKK0d:,,,,,ckKKKKKKKKK0o;;,,,;lOKKKKKKO,  .dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK;    .;lxkO0KKKKKKOc..... .l0KKKKKKKK0l'....':kKKKKKK0:   :NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO.   ;xKKKKKKKKKKx:;,.'coollxOkOKKKKKKKOl;cc;.'cccckKKKc   ,KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMx.  'kKKKKKKKKKKKkolllc:dxdc,..:OKKKKKKOl;:cc::::clkKKKl   'OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0O0XXl  .oKKKKKKKKKKKKKKKKKd;'...';ckKKK0KKK0xc,'.;xKKKKKKKKl   .dKKKXNWMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMW0ooxxxl.  .dKKKKKKK0000KKKKKKKK0kkk0KK0xc,,,:xKKKK000KKKKK0000l    .:xkxdONMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMXdd0OO0x.  .dKKKKK000KKK00KKKKKKKKKK0Okc..co:..;lx0KKKKKK00KKK0l.    :kO0ko0MMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMM0dxo;,:l'  .dKKKK0000KXK000KKKKKKkl;'...,xKK0xl:'.,lkKKK000KXK0l.    .,;lkdkWMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMKxdooo:,.  .xKKKK0000000000KKKKk:.':oxkO0KKKKKKK0d:..lOK0000000o.    'looxoxWMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMWkxOkkd,   .xKKKKK00000000KKKKd..cOKKKKKKK00KKKKKKKk:.,x0000000o.    ;xkOxoOMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMM0ok0Ox:.  .xKKKKKKKKKKKKKKKKO;.c0KKKKKKOl'.;xKKKKKK0l.;kKKKKKKd.    ,k0OodNMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdlk0Oo.  .xKKKKKKKKKKKKKKKK0lckKKKKKKKd.   ;0KKKKKK0xx0KKKKKKx.    ,k0ocOMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0clOOd.  .dKKKKKKKKKKKKKKKKKKKKKKKKKKKx.   ,OKKKKKKKKKKKKKKKKx.    ,kd,cXMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKccOOd.  .dKKKKKKKKKKKKKKKKKKKKKKKKKKKk'   'kKKKKKKKKKKKKKKKKk'    'ko,oNMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXlo0Od.  .d0KKKKKKKKKKKKKKKKKKKKKKKKKK0o,.,o0KKKKKKKKKKKKKKKKk'    'kx:dWMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdd00d.  .d00KKKKKKKKKKKKKKKKKKKKKKKKKKK000KKKKKKKKKKKKKKKKKKk'    'kk:xWMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXO00d.  .oO00KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKk,    'dooKMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXO,  .oOO00KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKO,  .okOKNMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWd. .okkO00KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKO,  '0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd. .okkkO0000KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKO;  '0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd. .okkkkOO0000000000000K00000000000000000000KK00K00K00O;  '0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd. .okkkkkkO00000000Oo;;oO0000000000000000000xok0000000O;  '0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd.  ';oxkkkkOO000000x.  .x000000000000000000d. ,k00000Ok;  '0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMk.    .lkkkkkkOO0000k;   :O000000000000000Oo,  ;k000OOkk:  .OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK;     ;xxxxxxkkOOO00d.  .ckO00000000000Od,   .l0OOOkkxx:  :XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMWNWWMMMMMMMMMMMMMMMMMMMMMMMMMWo     .lxxxxxxxkkkOOOl.   .,;coxxkxxol:'     ,xOkkkxxd:. ,0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MWKkoodolox0WMMMMMWXOkONMMMMMMMMMMMMNd.     'oxxxxxxxxxxkkko'        ...        'cxkkxxxxd:. .xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
Ko::ldoldkdodkKXNXOddoco0NNNNNNNXK0ko;'.     'oxxxxxxxxxxxkkdl;'.           ..;oxxxxxxxdl'   lNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
Kl;lxOOOOOOOxdoddddxOkl,,;;;;;,,'...          .ldxxxxxxxxxxxxxxxolc:;,,,,,;codxxxxxxxxd:.  .lXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MNOocldkOOOOOOOOOOOOOx:..                      .,codxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxo:.   ,KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMWKd:;coxkOOOOOOOOkl'.                          ..,:cloddxxxxxxxxxxxxxxxxxxxddolc;'.      ,lOXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMWKxolloooodddolc,.                                 ..'',,;;,,;;;;;;;;,,,'...              .:xKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMWNX0kdddxkkl'.                                                                           .;d0NMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMk,.                              .'..                                            .,cd0XWMMMMMMMMMWNXKXMMMMMMMM
MMMMMMMMMMMMMMMMMMMMk,                               :KXKk:..........:ol,                                .,OMMMMMMMN0doood0WMMMMMM
MMMMMMMMMMMMMMMMMMMMO,.                          .':dKWMMWOc'.''...';kWWXkc.                              .xNMMMWKkolodxockWMMMMMM
MMMMMMMMMMMMMMMMMMMMNkl;..                    .lx0NWMMMMMMWKo,...''cONMMMMWKl..                            .;oxdocldxxxl;oXMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMWNKkdc'.                .OMMMMMMMMMMMW0:..''lKWMMMMMMMWK:                           'c:,';cdxxxxxc,:oddxkOXW
MMMMMMMMMMMMMMMMMMMMMMMMMMMWX0kdc.             ,0MMMMMMMMMMNx,..''oNMMMMMMMMWd.                          .lxxdddxxxxxxxdl:;:::;,cK
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0;             :XMMMMMMMMW0c'..''c0WMMMMMMWx.                       .coccodxxxxxxxxxxxdl;,''';o0N
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNo.            .xWMMMMMMWKc'.....'cKMMMMMWk.                   .'':xXWMWX0xdoodxxxxxxdc;,,,,',xWM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO,              ,KMMMMMMKl'.......,dNMMMM0,                    .xNWMMMMMMMWNOllxxxxo::::;,'':o0WM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0dollllcccccc:::l0WMMMMW0ollllcccccdXMMMNd'................... .xWMMMMMMMMMMW0ollodo:'.';ccdKWMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWWWWWWWWMMMWNNXXXXXXXXKKKKKKK000000NMMMMMMMMMMMMMX0kxolc;':kXNWMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMMMMMMMMMMMMMMMMMMMMMWXKOkKWMMMMMMMM
MMMMMMMMMMMMMMMMMMMMXd::oXMMMXdooooooooooxNMMMMWX00000000xc:l0Xkddddddddx0WMMMMW0ooooookNWOc;cOWMWXdccoKMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMNkddc.  .:dxKk'....      ;0MMMMWd........   .kk.         :XMMMMNc      'Ok'   ,OOc'.   'c0MMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMM0,         .xNK0000d.  .oKWMMMMMKxod:.  .cdx0Wk.   ;ko.  :XMMMMNc  :l. 'kl.   .xk;'''''':OMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWKOOd.  .lO0NMMMMMM0'  'OMMMMMMXd:::'   .,::c0k.   oWK,  :XMMMMNc  ok' 'OXc   cXXkx0NKxdkNMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMM0,  .OMMMMMMMMM0'  'OMMMMMMXl'''.    .'';Ok.   oWK,  :XMMMMNc  ok' '0Wl   lWk..oWk. '0MMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMM0,  .codKMMMMMM0'  'OMMMMMMMXxd0x.  'O0dxNk.   oWK,  :XMMMMNc .ok' '0Wl   ;0k. cXd. ,KMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWKkd:.     .kMMMMMM0'  'OMMMMMMMO..dk.  ,0o '0k.   oWK,  :XMMMMNc .ok' 'OO'   .dO' ;0l  :XMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMWx.       ,lxXMMMMMM0'  'OMMMMMMMk..dk.  ,0o 'Ok.   oWK,  :XMMMMNc  ok' 'x:    ,0K, ,k:  lWMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMWx,;c:.  .OMMMMMMMMM0'  'OMMMMMMMk..dk.  ,0o 'Ok.   oWK,  :XMMMMNc  ok' 'kk'   lWX; .c' .dWMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWNWMK,  .OMMMMMMMMM0'  'OMMMMMMMk..dk.  ,0o 'Ok.   oWK,  :XMMMMNc  ok' '0Wo   lWNl     .kMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMM0,  .OMMMMMMMMM0'  'OMMMMMMNo..dk.  ,0o 'Ok.   oWK,  :XMMMMNc  ok' '0Wl   lWMXdc'  'OMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMNko;.  'OMMMMXxool;.  'OMMMMMM0, .xk.  ,0o '0k.   'l:.  :XMMMMNc  ';. 'Ok'   oNOool,  .cKMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMXc.....lXMMMMK:.......oXMMMMMMNkokN0,..:K0oxXO,........'dWMMMMNo......lKd...;0Xc.......'kMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMNK000XWMMMMMWX000000XWMMMMMMMMMMMMWK00XWMMMMWK0000000KXWMMMMMMNK0000KWMNK0KNMWX0000000KNMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMXkoc:::::::::lxXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMM0;    ......    ;0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMWo   'x000000d,..,kWMMMMNXNWMMMMMWXXWMMMWNXXXXXXXXXNWMMMMWNXXXXXXXXXNWMMMWNXXXXXXXXNWMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMWl   'x000000Okk0XWMMMMNo.,kWMMMWx''dWMM0:..........;xNMMKc.........;0MMMO;..'''''..,dXMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMWO,    ..........c0WMMMX: .dWMMMWl  cNMMO. .:doooo;. .OMM0' .:dooddoxXMMMx. .okkxxc. .OMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMWKxlc:::::::;.   ;XMMMX: .dWMMMWl  cNMMO. .d00000o. .OMM0' .:oooood0WMMMx. .dOkkkl. ,0MMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMNklllkNMMWWMWNl   ,0MMMX: .dWMMMWl  cNMMO.  ....... .lXMM0'  .''''',xWMMMx.  .....   :XMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMX:   .;cccccc:.   ;KMMMNc  ;OXXKO;  lNMMO. .lkkkkkkOKWMMM0' .o000000KNMMMx. 'x0000o. .OMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMW0:.             ,kWMMMM0;. ..... .;0MMMO. '0MMMMMMMMMMMM0'  .......'xWMMx. ;KMMMM0, .OMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMWKkxdddddddddxOXWMMMMMMNOxdddddxONMMMMXkdkNMMMMMMMMMMMMNkdddddddddd0WMMXxdONMMMMNkdkXMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM

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
