#===================================================== Importing Module ================================================
import random
import time

#===================================================== Global variable ================================================
suit = ["Spade", "Heart", "Club", "Diamond"]
face = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
fvalue = ["(1, 11)", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10"] * 4
cardset = []
playerlst = []
point = dict()
player_point = {}
player_card = {}
chips = dict()



#===================================================== Defining Function ===============================================

def Cardset():                       # Making a card set
    for w in suit:
        for p in face:
            cardset.append(w + " " + p)

def PointValue():                    # Convert facevalue to point
    keys = range(52)  # 用range integer化 -> 用作loop用途
    for i in keys:
        point[cardset[i]] = fvalue[i]

def playerformation():               # create players' number by number user input
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
                betting_sys()
        except:
            print("sorry, I don't understand what you mean, please try again!")

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

def betting_sys():  # Building a betting recording system
    for player in playerlst:  # set origin dict is 500
        chips[player] = 500


def next_round():
    print("\n\n")
    loop = True  # Play again?
    while loop == True:
        ask = input("would you like to start a New Round?").lower()
        if ask == "yes":
            loop = False
            Cardset()
        elif ask == "no":
            print("See You")
            break
        else:
            print("Sorry, I don't understand. Please try again")
    Consecutive_Round()

def mainbody():
    bonus = 0
    print("collecting 50 chips as entrance fee from all players")
    for player in chips:
        if chips[player] < 50:
            print("sorry to say that ", player, "does not have qualification to join the game")
            chips.pop(player)
            continue
        chips[player] -= 50  # this 50 chips does not calculate in bonus but 入場費　instead
        bonus += 50
    if len(chips) == 1:
        print(chips.keys() + "is the final winner in this game, which has" + chips.values())
    minus = []
    for k, v in chips.items():
        minus.append(k)
    print(minus)
    print("Dealer is now distributing cards...\n\n")
    time.sleep(1)
    drawing_cards()  # First distribution
    time.sleep(1)
    print("\n\n")
    drawing_cards()  # Second distribution

    while len(minus) > 0:
        for player in minus:
            bet_ = input("\n" + player + "  you have " + " " + str(
                player_point[player]) + "  points" + ": Would you like to bet?   Yes or No").lower()
            while bet_ != "yes" and bet_ != "no":
                print("sorry, I don't understand what you mean, please try again!")
                bet_ = input(player, "Would you like to bet?").lower()

            if bet_ == "yes":
                question = input("Would you all-in? Yes or no").lower()
                while question != "no" and question != "yes":
                    print("sorry, I don't understand what you mean, please try again!")
                    question = input("How would you like to all-in? (yes or no)").lower()

                if question == "yes":
                    a = 5
                    amount = chips[player]
                    chips[player] -= amount
                    print(player, "decides all in, betting: " + str(amount) + " chips")
                    bonus = bonus + amount

                elif question == "no":
                    check = input(player + "how many chips would you bet?")
                    while not check.isdigit():
                        print("I don't understand what you mean, please try again!!")
                        check = input(player + "how many chips would you bet?")
                    amount = int(check)
                    if amount < chips[player]:
                        a = 5
                        chips[player] -= amount
                        print(player, "has bet: " + str(amount) + " chips")
                        bonus = bonus + amount

                    elif amount > chips[player]:
                        print("Since you do not have enough chips, we will default you are calling all-in")
                        a = 5
                        amount = chips[player]
                        chips[player] -= amount
                        print(player, "decides all in, betting: " + str(amount) + " chips")
                        bonus = bonus + amount

            elif bet_ == "no":
                print(player, "decides not bet")
            action = input(player + "  you have " + " " + str(player_point[player]) +
                           "  points" + ", Would you stand, hit or surrender?   ").lower()
            while action != "hit" and action != "stand" and action != "surrender":
                print("Sorry, I don't understand.")
                action = input(player + "Would you stand, hit or surrender?").lower()

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
                    minus.pop(player)

            elif action == "stand":
                print(player, "decides to Stand")
                minus.remove(player)

            elif action == "surrender":  # 投降輸一半
                if a == 5:
                    back = int(amount / 2)  # 退回的chips
                    print(player, "decides to surrender, where he takes back half of amount:", back)
                    chips[player] += back
                    bonus -= back
                    minus.pop(player)
                    continue
                print(player, "decides to surrender")
                minus.remove(player)

    average_num = list()  # take record of the winner
    print("\n\nLet see who is the winner")  # When 21 does not appear
    lst = list()
    for k, v in player_point.items():  # Obtain the max. pt. from players
        if v > 21:
            print(k, "loses as Bust")
            continue
        lst.append((v, k))
        a, b = max(lst)

    print("\n\nFinally, we get the winner:")  # Consider with more than one player having max.pt.
    for player in player_point:
        if player in chips:
            if player_point[player] == a:
                average_num.append(player)
                print(player, "with points:", a)
                reward = bonus/len(average_num)
                chips[player] += reward
            print("bonus will be granted to the winner equally:", reward)

    print("\n\nResult:")
    for player in player_point:
        print(player, "has:", player_card[player], " with total point:", player_point[player],
                "Remaining chips:", chips[player])
        if chips[player] == "0":
            print("since number of chips become zero," + player + "can no longer take part in the next round")
            print(player + "loses")
            chips.pop(player)
        time.sleep(0.5)

def First_Round():
    Cardset()
    PointValue()
    playerformation()
    betting_sys()  # Call in the first round and when final winner appears (still having chips)
    mainbody()
    next_round()


def Consecutive_Round():
    Cardset()
    PointValue()
    mainbody()
    next_round()


#==================================================== Calling Function ================================================
First_Round()
Consecutive_Round()

