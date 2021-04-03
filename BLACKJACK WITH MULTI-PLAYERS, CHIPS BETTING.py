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
round = 0


#===================================================== Defining Function ===============================================
def Cardset():                       # Making a card set
    for w in suit:
        for p in face:
            cardset.append(w + " " + p)

def PointValue():                    # Convert facevalue to point
    keys = range(52)
    for i in keys:
        point[cardset[i]] = fvalue[i]

def playerformation():               # create players' number from their input
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

def betting_sys():
    for player in playerlst:
        chips[player] = 500

def next_round():
    print("\n\n")
    loop = True
    while loop == True:
        ask = input("would you like to start a New Round?").lower()
        if ask == "yes":
            loop = False
            Consecutive_Round()
        elif ask == "no":
            print("See You")
            break
        else:
            print("Sorry, I don't understand. Please try again")
    Consecutive_Round()                # New round without restoring the amount of chips to 500

def mainbody():
    # Starting new Round
    bonus = 0
    print("collecting 50 chips as entrance fee from all players")   # indication to foul players
    for player in chips:
        if chips[player] < 50:
            print("sorry to say that ", player, "does not have qualification to join the game")
            chips.pop(player)
            continue
        chips[player] -= 50
        bonus += 50
    if len(chips) == 1:                 # id the last player appears: final winner
        for k, v in chips.items():   ### correct to list
            print(k, "is the final winner in this game as others are fouled with", v, "congratulation!!!")
        restart_whole_game()
    minus = []                          # setting conditions for while loop
    for k, v in chips.items():
        minus.append(k)
    print("Dealer is now distributing cards...\n\n")
    time.sleep(1)

    # Drawing cards
    player_card = {}
    player_point = {}
    drawloop = 2
    while drawloop > 0:
        drawloop -= 1
        for player in chips:
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
        time.sleep(2)
        print("\n\n")

    # Hit and Stand Stage with betting decision
    # player's move to choose action: hit/stand/surrender & bet:
    # each action, player need to choose: 1) bet? 2)hit/stand/surrender
    # if stand/ surrender is picked, player would no longer be able to make further action
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
                    bonus = bonus + amount    # chips collected and betted  will be accumulated as bonus for winner in this round

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
                    minus.remove(player)

            elif action == "stand":
                print(player, "decides to Stand")
                minus.remove(player)

            elif action == "surrender":
                if a == 5:
                    back = int(amount / 2)  # if player surrender, he/she can take back half of chips he/she bet in this round
                    print(player, "decides to surrender, where he takes back half of amount:", back)
                    chips[player] += back
                    bonus -= back
                    minus.remove(player)
                    continue
                print(player, "decides to surrender")
                minus.remove(player)

    # Deciding winner
    print("\n\nLet see who is the winner")
    lst = list()
    for k, v in player_point.items():        # Obtain the max. pt. from players
        if v > 21:
            print(k, "loses as Bust")
            continue
        lst.append((v, k))
        a, b = max(lst)

    winnerlst = list()
    for player in chips:
        if player_point[player] == a:        # print all players who has the largest points
            winnerlst.append(player)
            print(player, "with points:", a)
            average = int(bonus/len(winnerlst))
            chips[player] += average

    print("Bonus accumulated:", bonus)       # amount of chips as bonus in total
    print("Distributed winner(s) equally:", average)  # dividing equally if more than one winner

    print("\n\nResult:")
    for player in player_point:
        print(player, "has:", player_card[player], " with total point:", player_point[player], "Remaining chips:", chips[player])

        if chips[player] == 0:               # fouling a player with 0 chips
            print("\n")
            print(player, "is fouled as no chips remained")
            chips.pop(player)
        time.sleep(0.5)

    if len(chips) == 1:                      # when the last player survives: winner of this game
        print("\n\n")
        for k, v in chips.items():
            print(k, "is the final winner in this game as others are fouled with", v, "congratulation!!!")
        restart_whole_game()

def First_Round():
    Cardset()
    PointValue()
    playerformation()
    betting_sys()
    mainbody()
    next_round()


def Consecutive_Round():
    Cardset()
    PointValue()
    mainbody()
    next_round()

def restart_whole_game():
    print("\n\n")
    re = True  # Play again?
    while re == True:
        ask = input("would you like to start a New Round?").lower()
        if ask == "yes":
            re = False
            First_Round()
        elif ask == "no":
            print("See You")
            break
        else:
            print("Sorry, I don't understand. Please try again")
    Consecutive_Round()

#==================================================== Calling Function ================================================
First_Round()
Consecutive_Round()
