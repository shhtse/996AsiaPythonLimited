import random
import time        # control the speed of the game

suit = ["Spade", "Heart", "Club", "Diamond"]
face = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
fvalue = ["(1, 11)", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10"] * 4
cardset = []
point = dict()
sum = 0
Player1 = input("Hello, What's your name?")
time.sleep(1)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Part 0 Definiton~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def CardSet():                                                # build 52 cards
    for w in suit:
        for p in face:
            cardset.append(w + " " + p)


def PointValue():                                             # Appending dict()
    keys = range(52)  # 用range integer化 -> 用作loop用途
    for i in keys:
        point[cardset[i]] = fvalue[i]                         # dict[key] = value

def game():                                           # Game Intro
    print(Player1, "The game will start soon")
    time.sleep(2)
    print("Dealer is distributing cards")
    scoring()

def scoring():
    CardSet()
    PointValue()
    def card_expose():
        draw = random.choice(list(point))
        Player_card[player] = Player_card[player] + " " + draw                  # extract corresponding value of key in dict()
        val = point[draw]
        if val == "(1, 11)":
            if Player_point[player] > 10:                                       # point determination of Ace
                pt = 1
            else:
                pt = 11
        else:
            pt = int(val)
        point.pop(draw, None)                                                   # attain card drawing without replacement
        sum = Player_point.get(player) + pt
        Player_point[player] = sum
        time.sleep(1)
        delay()
        print(player, Player_card[player], " total point:", sum)

    def cal_unknown():                                                          # Card with covered
        for player in Player_point:
            if player != Player1:
                print(player, ":", Player_card[player], "+ ?, total point:", Player_point[player], "+ ?")
            draw = random.choice(list(point))
            val = point[draw]
            Num = Player_card.get(player) + " " + draw
            Player_card[player] = Num
            if val == "(1, 11)":
                if Player_point[player] > 10:
                    pt = 1
                else:
                    pt = 11
            else:
                pt = int(val)
            point.pop(draw, None)
            sum = Player_point.get(player) + pt
            Player_point[player] = sum
            if player == Player1:
                time.sleep(1)
                print(player, ":", Num, " total point:", sum)
                continue
            time.sleep(1)

    def hit():
        draw = random.choice(list(point))
        Player_card[player] = Player_card[player] + " " + draw                                  # marking card into dict()
        val = point[draw]
        if val == "(1, 11)":
            if Player_point[player] > 10:                                                       # point determination of Ace
                pt = 1
            else:
                pt = 11
        else:
            pt = int(val)
        point.pop(draw, None)                                                                   # attain card drawing without replacement
        sum = Player_point.get(player) + pt
        Player_point[player] = sum
        time.sleep(1)
        if player == Player1:
            print(player, "decides to Hit, and receives", draw, "total:", sum)
        elif player != Player1:
            delay()
            print(player, "decides to Hit, and receives", draw)

    def delay():                                              # speed of game flow
        if player == Player1:
            print("waiting ..............")
            time.sleep(1)

    Player_point = {Player1: 0, "player 2": 0, "player 3": 0, "player 4": 0, "Banker": 0}
    Player_card = {Player1: "", "player 2": "", "player 3": "", "player 4": "", "Banker": ""}
    minus = [Player1, "player 2", "player 3", "player 4", "Banker"]  # end looping  of useless meessage: (stand. stand. stand)
    minus_2 = [Player1, "player 2", "player 3", "player 4", "Banker"]
    print("\n\nNew Round\nWith Card Exhibiting")

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Part 1 Card Exhibtion & Covered~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    for player in Player_point:
        card_expose()

    print("\n\nWith Card Covered")
    cal_unknown()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Part 2 Hit and Stand~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    print("\n\n")
    while len(minus) > 1:
        action = input("stand or hit?       :").lower()
        if action == "hit":
            for player in minus:
                if player == Player1:
                    hit()
                elif player != Player1 and Player_point[player] < 15:
                    hit()
                elif player != Player1 and Player_point[player] >= 15:
                    print(player, "decides to Stand")
                    minus.remove(player)
                    delay()
        elif action == "stand":
            while len(minus) > 0:
                for player in minus:
                    if player == Player1:
                        print(player, "decides to Stand")
                        minus.remove(player)
                        delay()
                    elif player != Player1:
                        if Player_point[player] >= 15:
                            delay()
                            print(player, "decides to Stand")
                            minus.remove(player)
                            delay()
                        elif Player_point[player] < 15:
                            hit()
                            delay()
        else:    # prevent bug
            print("Sorry, I don't understand.")


    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Part 3 Point Judgement~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    print("\n\nLet see who is the winner")  # When 21 does not appear
    largest = 0
    lst = list()
    for k, v in Player_point.items():             # Obtain the max. pt. from players
        if v > 21:
            print(k, "loses as Bust")
            continue
        lst.append((v, k))
    a, b = max(lst)

    print("\n\nFinally, we get the winner:")          # Consider with more than one player having max.pt.
    for player in Player_point:
        if Player_point[player] == a:
            print(player, "with points:", a)

    print("\n\nResult:")
    for player in Player_point:
        print(player, "has:", Player_card[player], "             with total point:", Player_point[player])
        time.sleep(0.5)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Part 4 Start Again?~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    print("\n\n")
    loop = True                                      # Play again?
    while loop == True:
        ask = input("would you like to start a New Round?").lower()
        if ask == "yes":
            loop = False
            game()
        elif ask == "no":
            print("See You")
            break
        else:
            print("Sorry, I don't understand. Please try again")

CardSet()
PointValue()
game()
