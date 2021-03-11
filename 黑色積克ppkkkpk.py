# DLLM DEL ME FILE?
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

def CardSet():                                                # Double for-loop to build 52 cards
    for w in suit:
        for p in face:
            cardset.append(w + " " + p)


def PointValue():                                             # Appending dict()
    keys = range(52)  # 用range integer化 -> 用作loop用途
    for i in keys:
        point[cardset[i]] = fvalue[i]                         # dict[key] = value


def game():                                                   # Game Intro
    print(Player1, "The game will start soon")
    time.sleep(2)
    print("Dealer is distributing cards")
    scoring()


def scoring():
    def common_cal():                                         # Card with Exhibition
        draw = random.choice(list(point))                     # randomly distributing card
        Player_card[player] = Player_card[player] + " " + draw
        if point[draw] == "(1, 11)":                          # dict[key] = value
            if Playerpoint[player] > 10:  # 用total點數決定ace既點數
                pt = 1
            else:
                pt = 11
        else:
            pt = int(point[draw])
        sum = Playerpoint.get(player) + pt
        Playerpoint[player] = sum                            # dict[key] = value
        time.sleep(1)
        if a == 5:
            delay()
            print(player, Player_card[player], " total point:", sum)
        elif zzz == 100:  # 玩家hit 牌
            if player == Player1:
                print(player, "decides to Hit, and receives", draw, "total:", sum)
            elif player != Player1:  # cpu玩家hit 牌
                delay()
                print(player, "decides to Hit, and receives", draw)

    def cal_unknown():  # 暗牌部分
        for player in Playerpoint:
            if player != Player1:
                print(player, ":", Player_card[player], "+ ?, total point:", Playerpoint[player], "+ ?")
            draw = random.choice(list(point))
            Cpt = point.get(draw)
            Num = Player_card.get(player) + " " + draw
            Player_card[player] = Num
            if Cpt == "(1, 11)":
                if Playerpoint[player] > 10:
                    pt = 1
                else:
                    pt = 11
            else:
                pt = int(Cpt)
            sum = Playerpoint.get(player) + pt
            Playerpoint1[player] = sum
            if player == Player1:
                time.sleep(1)
                print(player, ":", Num, " total point:", sum)
                continue
            time.sleep(1)

    def hit():
        time.sleep(1)
        delay()
        common_cal()

    def delay():  # 調慢速度
        if player == Player1:
            print("waiting ..............")
            time.sleep(2)

    Player_point = {Player1: 0, "player 2": 0, "player 3": 0, "player 4": 0, "Banker": 0}     # dict(player:Point)
    Player_card = {Player1: "", "player 2": "", "player 3": "", "player 4": "", "Banker": ""} # dict(player:Card)
    minus = [Player1, "player 2", "player 3", "player 4", "Banker"]  # stop loop, 避免重覆出現meessage: (a stand.. a stand. a stand)
    print("\n\nNew Round\n With Card Exhibiting")
    for player in Player_point:
        a = 5  # show point
        common_cal()
        a = 0
    print("\n\n With Card Covered")
    cal_unknown()
    print("\n\n")
    HitNSt = True
    while HitNSt == True:
        ask = input("stand or hit          ").lower()
        if ask == "hit":  # 獨立事件1: 玩家決定hit  (目前夠用, 但可以改更好)
            zzz = 100  # enable hit 牌情況出現
            for player in minus:
                if player == Player1:
                    hit()  # 玩家hit 牌
                elif player != Player1 and Player_point[player] < 15:
                    hit()  # 玩家hit 牌
                elif player != Player1 and Player_point[player] >= 15:
                    print(player, "decides to Stand")
                    minus.remove(player)
                    delay()
        elif ask == "stand":
            zzz = 100
            HitNSt = False
            fff = 3
            while fff > 0:
                for player in minus:
                    if len(minus) < 2:
                        fff = fff - 999  # 如果全部都stand就停
                    elif player == Player1:
                        print(player, "decides to Stand")
                        delay()
                    elif player != Player1:
                        if Player_point[player] >= 15:
                            print(player, "decides to Stand")
                            minus.remove(player)
                            delay()
                        elif Player_point[player] < 15:
                            hit()

        elif ask != "hit" and ask != "stand":
            print("Sorry, I don't understand.")
    zzz = 0
    for player in Player_point:
        if Player_point[player] > 21:
            print(player, "Bust")
        elif Player_point[player] == 21:
            print(player, "has won black Jack")
            break
        elif Player_point[player] == 21:  # 未整好 :呢度我想整 if 無人=21, then winner = 最接近又細過21既數,but 唔識整
            pass
    print("\n\nResult:")
    for player in Player_point:
        print(player, "has:", Player_card[player], "             with total point:", Player_point[player])
        time.sleep(0.5)
    print("\n\n")
    loop = True
    while loop == True:
        ask = input("would you like to start a New Round?").lower()
        if ask == "yes":
            loop = False
            scoring()
        elif ask == "no":
            print("See You")
            break
        else:
            print("Sorry, I don't understand. Please try again")


CardSet()
PointValue()
game()
