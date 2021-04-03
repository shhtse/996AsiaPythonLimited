import random

def restore_card():
    global card
    card = dict()
    face = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    fv = ["(1, 11)", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10"]
    for s in ["♠", "♥", "♣", "♦"]:
        for i in range(13):
            card[s + face[i]] = fv[i]
restore_card()

def restore_lst():      # Restore in each New Round
    global name_pt, name_card, sum, remove_lst
    sum = 0
    name_pt = {}
    name_card = {}
    remove_lst = []

def player_lst():     # Restore in Each NEW Game
    global player_lst
    player_lst = []
    running = True
    while running:
        try:
            player_num = input('''Welcome to the BlackJack World, \nhow many players you want to create?(Please enter the number from 2 to 9)''')
            number = int(player_num)
            if number > 1 and number < 10:
                for player in list((range(number))):
                    name = input("Player " + str(player) + ", please enter your name:")
                    player_lst.append(name)
                    running = False
                print("So we have the followings players:", player_lst, "\n\nThe game will start after 3 seconds")
                chips_system()
        except:
            print("sorry, I don't understand what you mean, please try again!")

def spacing():
    print("\n")

def chips_system(): # Restore in Each NEW Game
    global survivor_chips
    survivor_chips = {}
    for player in player_lst:
        survivor_chips[player] = 500

def remove():
    for k, v in survivor_chips.items():
        remove_lst.append(k)
    print("Dealer is now distributing cards...\n\n")

def entrance_fee():
    global bonus
    bonus = 0
    print("collecting 50 chips as entrance fee from all players")
    for player in survivor_chips:
        if survivor_chips[player] < 50:
            print("sorry to say that ", player, "does not have qualification to join the game")
            survivor_chips.pop(player)
            continue
        survivor_chips[player] -= 50
        bonus += 50

def drawing(): #  Before hit and stand
    for player in survivor_chips:
        global draw     # make a local variable global
        draw = random.choice(list(card))
        if player not in name_card:
            name_card[player] = draw
        elif player in name_card:
            name_card[player] += "," + draw
        val = card[draw]
        if player not in name_pt:
            name_pt[player] = 0
        if val == "(1, 11)":
            if name_pt[player] > 10:
                pt = 1
            else:
                pt = 11
        else:
            pt = int(val)
        card.pop(draw, None)  # drawing without replacement
        name_pt[player] += pt
        print(player, name_card[player], "total point:", name_pt[player])

def betting():
    for player in remove_lst:
        bet = input(player + "you have" + str(name_pt[player])+ "points. Would you like to bet? Yes or No").lower()
        while bet != "yes" and bet != "no":
            print("sorry, I don't understand what you mean, please try again!")
            bet = input(player + "Would you like to bet?").lower()
        if bet == "yes":
            question = input("Would you all-in? Yes or no").lower()
            while question != "no" and question != "yes":
                print("sorry, I don't understand what you mean, please try again!")
                question = input("How would you like to all-in? (yes or no)").lower()

            if question == "yes":
                global amount
                amount = survivor_chips[player]
                survivor_chips[player] -= amount
                print(player, "decides all in, betting: " + str(amount) + " chips")
                global bonus
                bonus += amount  # chips collected and betted  will be accumulated as bonus for winner in this round

            elif question == "no":
                check = input(player + "how many chips would you bet?")
                while not check.isdigit():
                    print("I don't understand what you mean, please try again!!")
                    check = input(player + "how many chips would you bet?")
                amount = int(check)
                if amount < survivor_chips[player]:
                    survivor_chips[player] -= amount
                    print(player, "has bet: " + str(amount) + " chips")
                    bonus += amount
                elif amount > survivor_chips[player]:
                    print("Since you do not have enough chips, we will default you are calling all-in")
                    amount = survivor_chips[player]
                    survivor_chips[player] -= amount
                    print(player, "decides all in, betting: " + str(amount) + " chips")
                    bonus += amount
        elif bet == "no":
            print(player, "decides not bet")

def hit_and_stand():
    for player in remove_lst:
        action = input(player + " you have " + " " + str(name_pt[player]) + " points" + ", Would you stand, hit or surrender?   ").lower()
        while action != "hit" and action != "stand" and action != "surrender":
            print("Sorry, I don't understand.")
            action = input(player + "Would you stand, hit or surrender?").lower()

        if action == "hit":
            hitting()

        elif action == "stand":
            print(player, "decides to Stand")
            remove_lst.remove(player)

        elif action == "surrender":
                print(player, "decides to surrender, and showing his card", name_card)
                remove_lst.remove(player)
        else:
            print("Sorry, I don't understand.")

def round_winner():
    spacing()
    largest = []
    winnerlst = []
    print("Result")
    for key, value in name_pt.items():
        if value > 21:
            print(key, "Bust")
            continue
        largest.append(value)
        large = max(largest)

    for player in survivor_chips:
        if name_pt[player] == large:
            winnerlst.append(player)
            print(player, "is the winner, with points:", large)
            average = int(bonus / len(winnerlst))
            survivor_chips[player] += average

    print("Bonus accumulated:", bonus)  # amout of chips as bonus in total
    print("Distributed winner(s) equally:", average)  # dividing equally if more than one winner

    for player in name_pt:
        print(player, "has:", name_card[player], " with total point:", name_pt[player], "Remaining chips:",
              survivor_chips[player])

def hitting():
    for player in remove_lst:
        draw = random.choice()
        name_card[player] += "," + draw
        val = card[draw]
        if card[draw] == "(1, 11)":
            if name_pt[player] > 10:
                pt = 1
            else:
                pt = 11
        else:
            pt = int(val)
        card.pop(draw, None)  # drawing without replacement
        name_pt[player] += pt
        print(player, "hit, gets", draw)
        print(player, ":", name_card[player], "total point", name_pt[player])
        if name_pt[player] > 21:
            remove_lst(player)

def hit_and_stand_and_bet():
    spacing()
    while len(remove_lst) > 0:
        betting()
        hit_and_stand()

def fouling_loser():
    for player in name_pt:
        if survivor_chips[player] == 0:  # fouling a player with 0 chips
            print("\n")
            print(player, "is fouled as no chips remained")
            survivor_chips.pop(player)

def final_winner():
    if len(survivor_chips) == 1:
        for k, v in survivor_chips.items():
            print(k, "is the final winner in this game as others are fouled with", v, "congratulation!!!")
        next_game()

def next_round():
    while True:
        ask = input("would you like to start a New Round?").lower()
        if ask == "yes":
            consecutive_round()
        elif ask == "no":
            print("See You")
            break
        else:
            print("Sorry, I don't understand. Please try again")

def next_game():
    while True:
        ask = input("would you like to start a New Game?").lower()
        if ask == "yes":
            initial_round()
        elif ask == "no":
            print("See You")
            break
        else:
            print("Sorry, I don't understand. Please try again")

def initial_round():
    restore_lst()
    restore_card()
    player_lst()
    print("3")
    remove()
    print("4")
    entrance_fee()
    final_winner()
    drawing()
    drawing()
    hit_and_stand_and_bet()
    round_winner()
    fouling_loser()
    final_winner()
    next_round()

def consecutive_round():
    restore_lst()
    restore_card()
    remove()
    entrance_fee()
    final_winner()
    drawing()
    drawing()
    hit_and_stand_and_bet()
    round_winner()
    fouling_loser()
    final_winner()
    next_round()

initial_round()
