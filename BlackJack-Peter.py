import random
import time
from collections import Counter

name = ['Dealer']
playpoint = {'Dealer' : '0'}

class Player():
    """Module of player"""

    def __init__(self, name, bet, cards, points):
        self.name = name
        self.bet = 0
        self.cards = cards
        self.points = points

def playerinfo():
    while True:
        try:
            nop = int(input('\nHow many numbers of players? Please enter within range of 1-9. '))
            if 9 >= nop >= 1 :
                for number in range(1, nop + 1):
                    name.append(input(f'Player. {number}, please enter your name.'))
                break
            else:
                print('\nSorry, please enter a VALID number.')
        except:
            print('\nSorry, please enter a number.')

        print(name)

    counts = Counter(name)
    for k, v in counts.items():
        if v > 1:
            for suffix in range(1, v + 1):
                name[name.index(k)] = k + '-' + str(suffix)

    print(name)

    for i in range(len(name)):
        if name[i] != 'Dealer':
            name[i] = Player(name[i], 0, [], 0)
            print(name[i].name)
        else:
            name[i] = Player(name[i], 'Infinity', [], 0)
            print(name[i].name)

    print(name)

    for i in range(len(name)):
        if name[i] != "Dealer":
            try:
                playerbet = int(input(f'\n{name[i]} ,how much you wanna bet? It must be within range of 1-100. '))
                if 100 >= playerbet >= 0:
                    print(name[i].bet)
                else:
                    betting = print('\nSorry, please enter a VALID number. ')
            except:
                print('\nSorry, please enter a NUMBER. ')


def decking():
    global cards
    cards = []
    if len(name) <= 4:
        cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4
    else:
        cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * (len(name)-1)
    random.shuffle(cards)

def cal():
    for p in name:
        playerpoint[p] = 0
        for k in f'card{p}':
            if k == 'A':
                playerpoint[k] += 11
                print(playerpoint)
            elif k == 'J' or k == 'Q' or k == 'K':
                playerpoint[k] += 10
                print(playerpoint)
            else:
                playerpoint[k] += k
                print(playerpoint)

"""Start of the game."""
print("Welcome to BlackJack!")
playerinfo()
decking()
cal()
