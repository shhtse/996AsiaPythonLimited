#大既可供真實玩家使用身份既數量: 9
#設定真實玩家數量的方式: 建立相應的input, 將其他未被挑選的玩家pop up
#各真實玩家的起手籌碼: e.g.500

#用while loop執行以下行動:
#根據被挑選真實玩家數量決定行動的次數 (1人1次): hit / stand
#被挑選真實玩家決定加注/投降 -- pop up
#顯示其點數& 勝者名;分
#勝的:籌碼對分

# 需要既function:
# １)籌碼 2)５２張卡 ３）點數變換 ４）明牌ｓｔｅｐｓ　５）hit and stand and surrender 6) player list

# Part One: importing modules
import random
import time

# Part Two: Setting Global variables
# Place outside the scope as Global variable to prevent name error from definition of function
suit = ["Spade", "Heart", "Club", "Diamond"]
face = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
fvalue = ["(1, 11)", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10"] * 4
cardset = []
playerlst = []
point = dict()
player_point = {}
player_card = {}
minus = playerlst.copy()
chips = dict()


# Part Three: Defining Function
def Cardset():                       # Making a cardset contains 52 cards
    for w in suit:
        for p in face:
            cardset.append(w + " " + p)

def PointValue():                    # Convert facevalue into point
    keys = range(52)  # 用range integer化 -> 用作loop用途
    for i in keys:
        point[cardset[i]] = fvalue[i]

def playerformation():               # create players' number according to number user input
    running = True
    while running:
        try:
            playernum = input('''Welcome to the BlackJack World, \nhow many players you want to create?(Please enter the number from 2 to 9)''')
            number = int(playernum)
            if number > 1 and number < 10:
                for player in list((range(number))):
                    naming = input("Player " + str(player) + ", please enter your name:")
                    playerlst.append(naming)
                    running = False
            print("So we have the followings players:", playerlst, "\n\nThe game will start after 3 seconds")
            time.sleep(3)
        except:
            print("sorry, I don't understand what you mean, please try again!")

def opening():
    for player in playerlst:
        minus = playerlst[:]
        chips[player] -= 50             # this 50 chips does not calculate in bonus but 入場費　instead
        if chips[player] < 50:
            print("sorry to say that ", player, "does not have qualification to join the game")
            minus.remove(player)
    print("Dealer is now distributing cards...\n\n")
    time.sleep(1)
    drawing_cards()         # First distribution
    time.sleep(1)
    print("\n\n")
    drawing_cards()         # Second distribution

def betting_sys():          # calculating chips they put
    for player in playerlst:  # set origin dict is 500
        chips[player] = 500


def drawing_cards():
    for player in playerlst:
        draw = random.choice(list(point))
        if player not in player_card:
            player_card[player] = " "
        if player not in player_point:
            player_point[player] = 0
        player_card[player] = player_card[player] + " " + draw
        val = point[draw]
        if val == "(1, 11)":
            if player_point[player] > 10:
                pt = 1
            else:
                pt = 11
        else:
            pt = int(val)
        point.pop(draw, None)
        sum = player_point[player] + pt
        player_point[player] = sum
        time.sleep(1)
        print(player, player_card[player], "total point:", sum)

def decision():
    bonus = 0
    minus = playerlst[:]
    while len(minus) > 0:
        for player in minus:
            bet_ = input("\n" + player + "  you have " + " " + str(player_point[player]) + "  points" + ": Would you like to bet?").lower()
            if bet_ == "yes":
                amount = int(input("how many chips you want to bet?       Your chips available:" + str(chips[player])) + "")
                if amount <= chips[player]:
                    chips[player] -= amount
                    print(player, "has bet: " + str(amount) + " chips")
                    bonus = bonus + amount
                elif amount > chips[player]:
                    print("Sorry, you cannot do this")
                    bet_
                else:
                    print("sorry, I don't understand what you mean, please try again!")
                    bet_
            elif bet_ == "no":
                print(player, "decides not bet")
            else:
                print("sorry, I don't understand what you mean, please try again!")
                bet_
            action = input(player + "  you have " + " " + str(player_point[player]) + "  points" + ", Would you stand, hit or surrender?   ").lower()
            if action == "hit":
                draw = random.choice(list(point))
                player_card[player] = player_card[player] + "" + draw
                val = point[draw]
                if val == "(1, 11)":
                    if player_point[player] > 10:
                        pt = 1
                    else:
                        pt = 11
                else:
                    pt = int(val)
                point.pop(draw, None)
                sum = player_point[player] + pt
                player_point[player] = sum
                time.sleep(1)
                print(player, player_card[player], "total point:", sum)
                if player_point[player] > 21:
                    minus.remove(player)
            elif action == "stand":
                print(player, "decides to Stand")
                minus.remove(player)
            elif action == "surrender":                # 投降輸一半
                return_ = amount/2                     # 退回的chips
                print(player, "decides to surrender, where he takes back half of amount:", return_)
                chips[player] += return_
                bonus -= return_
                minus.remove(player)
            else:
                print("Sorry, I don't understand.")
    def point_judge():
        average_num = list()                        # take record of the winner
        print("\n\nLet see who is the winner")  # When 21 does not appear
        lst = list()
        for k, v in player_point.items():             # Obtain the max. pt. from players
            if v > 21:
                print(k, "loses as Bust")
                continue
            lst.append((v, k))
        a, b = max(lst)

        print("\n\nFinally, we get the winner:")          # Consider with more than one player having max.pt.

        for player in player_point:
            if player_point[player] == a:
                average_num.append(player)
                print(player, "with points:", a)
                equally = bonus / len(average_num)
                chips[player] += equally
        print("bonus will be granted to the winner equally:", equally)

        print("\n\nResult:")
        for player in player_point:
            print(player, "has:", player_card[player], "             with total point:", player_point[player],
            "Remaining chips:", chips[player])
            time.sleep(0.5)
    point_judge()

def playagain():
    print("\n\n")
    loop = True  # Play again?
    while loop == True:
        ask = input("would you like to start a New Round?").lower()
        if ask == "yes":
            loop = False
            main()
        elif ask == "no":
            print("See You")
            break
        else:
            print("Sorry, I don't understand. Please try again")


def main():                          # core part of the programme
    Cardset()
    PointValue()
    playerformation()
    betting_sys()
    opening()
    decision()
    playagain()


# Part Five: Calling function
main()










