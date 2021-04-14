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
                            print("Remaining player:" + str(self.p.players))
                            continue

                        elif types == "double-down":
                            print('''When you reply: Split, public security guides came near''')
                            time.sleep(1)
                            print("Dealer: Sorry, there is only one China policy, and I am calling public security guides")
                            time.sleep(1)
                            print("\033[31;1m 同志 ,跟我们回去接受爱国思想教育\033[0m")
                            time.sleep(2)
                            print("\n" + srt(player) + "  is sent to Concentration Camp to enjoy comfortable life and quit the game")
                            time.sleep(1)
                            print(str(player) + "'s chips is confiscated")
                            time.sleep(1)
                            self.p.move.remove(player)
                            self.p.players.remove(player)
                            time.sleep(1)
                            print(str(player) + "'s chips is confiscated")
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
            print("\n\nAll player are sent to jail!!!!")
            time.sleep(1)
            print("As There are no player remain in the game:")
            time.sleep(2)
            print("\n\n"
"""\033[33;1m
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNXKNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXx;..,dKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNX0ko:'.     .,lxOKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKxl:,..               .';cd0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXx;.                .,:;'.    .;dXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd'     ..',:cllllllllx0XK0Od:.    .dXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0:    .cdk00KKKKKKKKKKKKKKKKKKKOl'    ;0WMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0,   .cOKKKKKKKKKKKKKKKKKKKKKKKKKKOo'   'OWMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMK;    .dKKKKKKKK0KKKKKKKKKKKKKKKK0KKKO;   ,KMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMNl     .o0KKK0xllccokKKKKKKKKKKxlcclokKk'   oWMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMM0'      .:kKKkdxkxddOKKKKKKKKK0kdxkkdxOKk:. 'OMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMWd.    .';lOKKKOo;,'';xKKKKKKKOl;,,;lOKKKKO;  lNMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMXc  .;dOKKKKK0xl,.,:;;d00KKKKK0o;,;';dxxOK0:  ;KMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMK,  c0KKKKKKK0dcc:cdxl;,:xKKKKKx::c;;cclkKKc  '0MMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMWKO00x. 'kKKKKKKKKKKKKOl:;,;cd00kkOKOo:;:xKKKKKKc  .o00KXWMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMWOdkOk:  ,OKKKK00KK0KKKKKK00KK0o;;;,cx0KKKKKK0KK0c   .oOkx0WMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMXxxoco:. ,OKKK000KK00KKKK0kl:;,'lOOo:;;cx0KK00KK0l.  .,cdxkNMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMNkdoo:.  ;OKKK0000000KKKx:,:odxO0KKKK0xc,;x000000l.   ;oddxNMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMW0xOOo.  ;OKKKK00000KKKx',xKKKKKOddOKKKKk;'o00000o.  .lOOdOWMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMKdxOk;  ;OKKKKKKKKKKKKo;xKKKKKO;  :OKKKKOod0KKKKd.  .lOddXMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMWklkO:  ,OKKKKKKKKKKKKK0KKKKKKk'  'kKKKKKKKKKKKKd.   ld:xWMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMOlxO:  ,OKKKKKKKKKKKKKKKKKKKK0:  ,kKKKKKKKKKKKKx.   cd:kWMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMM0dO0:  ,kKKKKKKKKKKKKKKKKKKKKKOookKKKKKKKKKKKKKx.   lxlOMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMN000:  ,k0KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKx.  .cdxXMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWNXd. ,xO0KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKx' .d0KNMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMK, ,xkO00KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKk' '0MMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMK, ,xkkOO00000KK00000000000000KKKKKKK00000Kk' '0MMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMK, 'dkkkkO000000x:;o000000000000000xlx00000x' '0MMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMK,  .:dkkkOO0000o. 'x0000000000000x' :O000Ox' '0MMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMNc   .cxxxkkOOO0k;  ;k0000000000kc. .lOOOkkd, ;KMMMMMMMMMMMMMMMMMMMMMMMMM
MMWWWNXNWMMMMMMMWMMMMMMMMMMMx.   'oxxxxxkkOOd'  .,:codddoc;.   ,xOkkxd:..kWMMMMMMMMMMMMMMMMMMMMMMMMM
NOdoolodkKWMMWXkxONMMMMMMMWXx'    ,dxxxxxxxkkd;.            .'cdxxxxo; .oNMMMMMMMMMMMMMMMMMMMMMMMMMM
O:cxkxkOxxxkOkdxdccoddddol:,..     ,oxxxxxxxxxxdl:;,.....',:oxxxxxdc.  cXMMMMMMMMMMMMMMMMMMMMMMMMMMM
N0dloxkOOOkkxkOOd;.                 .:ldxxxxxxxxxxxxddddddxxxxxxxdc.  ,0MMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMWKdccodxkkOkkx:.                     .';:clooodddddddddooolc:;'.     'lkXWMMMMMMMMMMMMMMMMMMMMMMMM
MMMMWX0Okxdddxdc'.                           ...............              .:xKWMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMWNNNNWO,                        ...                                 .;okKNMMMMMMMWNXNMMMMMM
MMMMMMMMMMMMMMMO,                       'kX0o'.......;ol'                        .xWMMMWN0xdodKWMMMM
MMMMMMMMMMMMMMMKc.                  .;lxKWMMNx;'.'''cOWWXk;.                      ;xKX0kdoddll0MMMMM
MMMMMMMMMMMMMMMWN0ko:..            .kWMMMMMMMNx,.',lKWMMMMNk,                     ';;:codxxo:cxkO0XW
MMMMMMMMMMMMMMMMMMMMWX0xo,          :KMMMMMMMNd'.,:xWMMMMMWk.                    ,ddddxxxxxxl:;;;;cO
MMMMMMMMMMMMMMMMMMMMMMMMMK:          oWMMMMMWO:'.',c0WMMMWk.                 'okxxdddxxxxxxdc;,,';kN
MMMMMMMMMMMMMMMMMMMMMMMMMK:          .OMMMMWO:'....'oXMMM0,               'oONMMMWX0xodxxdlc:;,,,lKM
MMMMMMMMMMMMMMMMMMMMMMMMWKdlcccccc:::ckWMMMNklllllccdKMMWx,'..............;KMMMMMMMMXxoooo:'':clONMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWWWWWWMMMWNNNNNXXXXXXXKKKKXWMMMMMMMMMWX0kxdclONWMMMM
MMMMMMMMMMMMMMMW0xONMMNK0000000KNMMMMWNNNNNX0k0NNKKKKKKKXWMMMWK0000XWXkx0WMWKkOXMMMMMMMMMMWNNMMMMMMM
MMMMMMMMMMMMNOxl. .cx0k;.......;OMMMNo,,,','..;kl.......cXMMM0,....:Oc. 'kOc.  ,dXMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMKc'.   .'dXK000c  ,ONMMMNklc'  .coO0;  .oo. ;KMMMO'.c; ;x,  .dkc::::oKMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMWNNO' .dNWMMMMWd. :XMMMM0:'..  ..'ck;  '00, ;XMMMO'.ol ;Kx. ;KOckNk:oXMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMK, .ck0WMMMWd. :XMMMMNxlo;  ,old0;  '00' ;XMMMO'.ol ;Kx. 'Oo.:0: ;KMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMXOd:.   .oWMMMWd. :XMMMMWo.oo. cx':O:  '00' ;XMMMO'.ol ;k:  .od.,x, cNMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMWd...  .:OXMMMMWo. :XMMMMNl.ol  cd.;O:  '00' ;KMMMO'.ol ;o'  'Ok.'l' oWMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMKk0k' .kMMMMMMWd. :XMMMMNl.ll  cx.;O:  '00' ;KMMMO'.oc ;0d. ;K0'.. .dWMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMW0, .kMMMMMMWo  :XMMMMK:.ll  cx.;O:  'OO' ;KMMMO'.oc ;Kx. ;KNkc. .kMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMKl'. .OMMM0l:;.  cNMMMMO;,xo. ck;cO;  .''. :XMMMO' .. :k;  :0d:;.  :KMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMXxlloONMMMXdlllldKMMMMMWXXW0ooONXXNkllllllo0WMMMXxlllo0XxldKXkllllldXMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMWWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMW0o:;,,,,,,:dKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMM0,  ,cccc:. .cXMMMMMMMMMMMWMMMMMMMWWMMMMMMMMMMMMMMMMMMMMMMMMMWMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMk. .oKKKK0kod0WMMWkcxNMMWOcdXMNx::::::::oKMWOc::::::lKMM0c::c:::cxXMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMXc. ........'oXMMNc ;XMMWl ,KMX; 'odddl. lNWo..cooodkXMWd..lkkx: .kMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMN0dodxxxxxc. .xMMNc ;XMMWl ,0MX; 'clll:..oWWo..:::: xWMMx..;ccc' ,0MMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMk'..cddddd:. .xMMNl 'ONNK: ,KMX; .cllllokXMWo..cdddxONMMd..:ooo;.'OMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMXl'..........lKMMW0;..,,'.'xNMX:.lNMMMMMMMMWd.::::   :kWMx.,OMMMO'.kMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMWX00OOOOOO0XWMMMMMNKOOOO0XWMMWKOXMMMMMMMMMMX0OOOOOO0XMMN00NMMMN00NMMMMMMMMMMMMMMMMMMM
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
g = Game()
g.start()
