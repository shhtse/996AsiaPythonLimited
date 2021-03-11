import random  # 隨機效果
import time  # 計時效果

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
    def common_cal():                                         # Card with Exhibition
        draw = random.choice(list(point))
        Player_card[player] = Player_card[player] + " " + draw   # extract corresponding value of key in dict()
        val = point[draw]
        if val == "(1, 11)":
            if Player_point[player] > 10:  # 用total點數決定ace既點數
                pt = 1
            else:
                pt = 11
        else:
            pt = int(val)
        point.pop(draw, None)                   # attain card drawing without replacement
        sum = Player_point.get(player) + pt
        Player_point[player] = sum
        time.sleep(1)   # ~~~~~~~~~~~~~followings are difference conclusions among the results~~~~~~~~~~~~~~~~~~~~~~~~~
        if a == 5:                                           # Situation 1: card exhibition on every players
            delay()
            print(player, Player_card[player], " total point:", sum)
        elif zzz == 100:  # 玩家hit 牌                        # Situation 2: when user's hit
            if player == Player1:
                print(player, "decides to Hit, and receives", draw, "total:", sum)
            elif player != Player1:  # cpu玩家hit 牌
                delay()
                print(player, "decides to Hit, and receives", draw)

    def cal_unknown():                                       # Card with covered
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
        time.sleep(1)
        delay()
        common_cal()

    def delay():                                              # speed of game flow
        if player == Player1:
            print("waiting ..............")
            time.sleep(2)

    Player_point = {Player1: 0, "player 2": 0, "player 3": 0, "player 4": 0, "Banker": 0}
    Player_card = {Player1: "", "player 2": "", "player 3": "", "player 4": "", "Banker": ""}
    minus = [Player1, "player 2", "player 3", "player 4", "Banker"]  # end looping  of useless meessage: (stand. stand. stand)
    print("\n\nNew Round\nWith Card Exhibiting")

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Part 1 Card Exhibtion & Covered~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    for player in Player_point:
        a = 5                                    # attain situation 1: result during card exhibition on every players
        common_cal()
        a = 0                                    # close
    print("\n\nWith Card Covered")
    cal_unknown()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Part 2 Hit and Stand~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    print("\n\n")
    HitNSt = True
    while HitNSt == True:
        ask = input("stand or hit?       :").lower()
        if ask == "hit":                            # independent event1: user hit
            zzz = 100  # enable hit 牌情況出現
            for player in minus:                    # ask again (stand or hit)-- stop until answering stand
                if player == Player1:
                    hit()  # 玩家hit 牌
                elif player != Player1 and Player_point[player] < 15:  # 2 situations : 1) > 15: stand 2) <15: hit --> 2 situations again --> looping
                    hit()  # 玩家hit 牌
                elif player != Player1 and Player_point[player] >= 15:
                    print(player, "decides to Stand")
                    minus.remove(player)
                    delay()
        elif ask == "stand":                       # independent event2: user stand
            zzz = 100                              # attain situation 2: conclusion when user's hit
            HitNSt = False
            fff = 3
            while fff > 0:
                for player in minus:
                    if len(minus) < 2:
                        fff = fff - 999  # 如果全部都stand就停
                    elif player == Player1:
                        print(player, "decides to Stand")
                        delay()
                    elif player != Player1:      # 2 situations : 1) > 15: stand 2) <15: hit --> 2 situations again --> looping
                        if Player_point[player] >= 15:
                            print(player, "decides to Stand")
                            # remove to prevent repeating printing (not removing from dict(player:Point)),
                            # but from list called minus with same player name instead (need dict to calculate point)
                            minus.remove(player)
                            delay()
                        elif Player_point[player] < 15:
                            hit()

        elif ask != "hit" and ask != "stand":    # prevent bug
            print("Sorry, I don't understand.")
    zzz = 0                                # close the situation 2

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Part 3 Point Judgement~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


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