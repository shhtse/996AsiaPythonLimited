import random, time, itertools, copy, functools


class Base_setting:

    def playerinfo(self):
        while True:
            try:
                playerlist = []
                playernum = int(input("""Welcome to the BlackJack World !
                \nHow many players you want to create?(Please enter the number from 1 to 9)        """))
                if playernum >= 1 and playernum < 10:
                    for player in range(playernum):
                        naming = input(f"Player {player + 1} please enter your name:   ")
                        playerlist.append(naming)
                    print(f"So we have the followings players:{playerlist}\n\nThe game will start after 3 seconds")
                    return playerlist

                else:
                    print('Sorry, out of range,please try again!\n')
            except:
                print("sorry, I don't understand what you mean, please try again!\n")


    def cardset(self):
        suit = ["♠", "♥", "♣", "♦"]
        face = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        cardset = [(s + " " + f) for s in suit for f in face]
        return cardset


    def point(self):
        fvalue = [(1, 11), 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        fv =[]
        n = 4
        while n >0:
            n -= 1
            for fs in fvalue:
               fv.append(fs)
        cards= self.cardset()
        pt = dict(zip(cards, fv))
        return pt


    def calculator(self, x, operator, y ):
        return {'add': lambda x, y: x + y,
                'sub': lambda x, y: x - y,
                'mul': lambda x, y: x * y,
                'div': lambda x, y: x / y,
                }.get(operator, lambda: None)(x, y)

class Betting_system(Base_setting):

    def chips(self, playerinfo):
        playerlist = playerinfo
        chips = [1000]*len(playerlist)
        chips_list = dict(zip(playerlist, chips))
        print(chips_list)
        return chips_list


    def opening(self, playerlist, chips):
        for player in playerlist:
            if player in chips:
                chips[player] -= 50
            elif chips[player] < 50:
                print(f"sorry to say that{player}does not have qualification to join the game")
                playerlist.remove(player)
        chips.update(chips)
        return [50] * len(playerlist)


    def betting_option(self, chips):
        chips_list = chips
        lists = []
        chip_pan = []
        for i in chips_list.items():
                lists.append(i)
        while True:
                if len(chips_list) > len(chip_pan):
                    try:
                        option = int(input(
                                    "Please betting and enter the number to make the choice\n"
                                    "(1. 100, 2. 200, 3. 500, 4. All In)\n"))
                        if option == 1:
                            chip_pan.append(100)
                        elif option == 2:
                            chip_pan.append(200)
                        elif option == 3:
                            chip_pan.append(500)
                        elif option == 4:
                            chip_pan.append(lists[len(chip_pan)][1])
                        else:
                            print("Sorry, enter the correct number\n")
                    except:
                        print("sorry, I don't understand what you mean, please try again!\n")
                else:
                    return dict(zip(lists, chip_pan))


class Card_option_system(Betting_system):

    def hit_card(self):
        cardset = Base_setting.cardset(self)
        cardset_copy = copy.deepcopy(cardset)
        if cardset == None:
            cardset = cardset_copy
            card = random.choice(cardset)
            cardset.remove(card)
        else:
            card = random.choice(cardset)
            cardset.remove(card)
        return card

    def base_card_list(self, playerlist):
        card_set = [(player, self.hit_card()) for player in playerlist]
        return card_set


    def player_card_option(self, playerlist):
        card_set = []
        i = 0
        try:
            while len(card_set) < len(playerlist):
                    option = int(input(f" *** {playerlist[i]} *** please enter the number to make the choice:\n"
                                       "1.hit or 2.stand\n"))
                    i += 1
                    if option == 1:
                        card = self.hit_card()
                        card_set.append((playerlist[i - 1], card))
                    elif option == 2:
                        del playerlist[len(card_set)]
                        i -= 1
                    else:
                        print("sorry, I don't understand what you mean, please try again!\n")
                        i -= 1
        except:
                print("sorry, I don't understand what you mean, please try again!\n")
        return card_set


    def addtional_card_set(self, card_set):
        card_set = dict(card_set)
        pl = list(card_set.keys())
        cards = []
        while len(pl) != 0:
            cards.append(self.player_card_option(pl))
            print(cards)
        return cards

    def dec(self, card_set):
        temp = []
        cards = self.addtional_card_set(card_set)
        for i in range(len(cards)):
            for a in cards[i]:
                temp.append(a)
        temp =sorted(temp, key=lambda x: x[0])
        return temp


    def grouping_action(self, cardset1, cardset2, *args):
        temp = []
        temp2 =[]
        cardset = list(itertools.chain(cardset1, cardset2, *args))
        new_cs = sorted(cardset, key=lambda x: x[0])
        cardlists = [list(cardlist)for player, cardlist in itertools.groupby(new_cs, key=lambda x: x[0])]
        for i in range(len(cardlists)):
            for a in cardlists[i]:
                temp.append(a)
        for i in range(len(temp)):
            for b in temp[i]:
                temp2.append(b)
        temp3 = list(dict.fromkeys(temp2))
        return temp3


    def final_cardset(self,playerlist,temp3):
        final_list = []
        playerlist = sorted(playerlist, key=lambda x: x[0])
        for i in range(len(playerlist)-1):
            final_list.append((temp3[temp3.index(playerlist[i]):temp3.index(playerlist[i + 1])]))
        final_list.append((temp3[temp3.index(playerlist[len(playerlist) - 1]):]))
        return final_list







class Adjustment_system (Card_option_system):
    def __int__(self):
        pass

    # def ace_adjustment(self,playerlist,temp3):
    #     cardlist = cardlist
    #     pop =[]
    #     point_list = []
    #     point = Base_setting.point(self)
    #    for cl in cardlist

    def calculation(self,n, playerlist, temp4):
        temp6 = []
        if n < len(playerlist) - 1:
            for i in range(temp4.index(playerlist[n]), temp4.index(playerlist[n + 1])):
                if i != temp4.index(playerlist[n]):
                    temp6.append(temp4[i])

        else:
            for i in range(temp4.index(playerlist[n]), len(temp4)):
                if i != temp4.index(playerlist[n]):
                    temp6.append(temp4[i])

        return sum(temp6)































betting = Betting_system()
card_action =Card_option_system()
playerlist = betting.playerinfo()
pl = copy.deepcopy(playerlist)
# chips = betting.chips(playerlist)
# betting.opening(playerlist, chips)
# Betting_option = betting.betting_option(chips)
# print(Betting_option)
frist_card = card_action.base_card_list(pl)
print(frist_card)
second_card = card_action.base_card_list(pl)
print(second_card)
# card_set =card_action.player_card_option(pl)
# print(card_set)
# cards = card_action.dec(card_set)
print(playerlist)
final = card_action.grouping_action(frist_card, second_card)
print(card_action.final_cardset(playerlist,final))









