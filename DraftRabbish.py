import random
import time
from collections import Counter

global suits,ranks,cards,values,deck,playerlist,bets,playerhand,playerpoint
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
cards = []
values = ['(1, 11)', '2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10'] * 4
deck = {}
playerlist = ['Dealer']
bets = {'Dealer' : 'Infinity'}
playerhand = {}
playerpoint = {}


#Player1 = input('What is your name?')

def playerinfo():
    while True:
        try:
            nop = int(input('\nHow many numbers of players? Please enter within range of 1-3. '))
            if 3 >= nop >= 1 :
                for number in range(1, nop + 1):
                    playerlist.append(input('\nPlayer.'+str(number)+', please enter your name. '))
                break
            else:
                print('\nSorry, please enter a VALID number.')
        except:
            print('\nSorry, please enter a NUMBER. ')

    counts = Counter(playerlist)
    for k,v in counts.items():
        if v > 1:
            for suffix in range(1, v + 1):
                playerlist[playerlist.index(k)] = k + '-' + str(suffix)

def betting():
    for player in playerlist:
            while player != "Dealer":
                try:
                    bet = int(input('\n' + player + ',how much you wanna bet? It must be an EVEN number within range of 2-100. '))
                    if 100 >= bet >= 2 and bet%2 == 0:
                        bets[player] = bet
                        break
                    else:
                        bet = print('\nSorry, please enter a VALID number. ')
                except:
                    print('\nSorry, please enter a NUMBER. ')

def decking():
    for suit in suits:
        for rank in ranks:
            cards.append(suit+' '+rank)
    for i in range(52):
        deck[cards[i]] = values[i]


def assign1():
    for player in playerlist:
        draw = random.choice(cards)
        playerhand[player] = draw
        cards.remove(draw)

def hit():
    draw = random.choice(cards)
    playerhand[player] = playerhand[player] + ' & ' + draw
    playerpoint[player] = int(playerpoint[player]) + int(deck[draw])
    cards.remove(draw)
    print(player + ' gets [' + playerhand[player] + ']. Values: [' + str(playerpoint[player]) + ']. Bet: [' + str(bets[player]) + ']')

def cal():
    if int(playerpoint[player]) == 21:
        print(player + ' gets BLACKJACK!')
    elif int(playerpoint[player]) > 21:
        print(player + ' is busted!')



#----------------------------------------------------------------------------------------------------------------------------------
# Gameplay
print("Welcome to BlackJack!")
playerinfo()                                                                    #Ask for players' information
#Create bet list
betting()                                                                       #Ask bets (0-100, must be even no.)
#Create card list
decking()                                                                       # Assign cards for different players
#Assign first card for everyone
assign1()
#Print acquired cards and correspinding values to players
for player in playerlist:
    playerpoint[player] = deck[playerhand[player]]
    print(player + ' gets [' + playerhand[player] + ']. Values: [' + playerpoint[player] + ']. Bet: [' + str(bets[player]) + ']')
# Ask for players' actions
for player in playerlist:
    while player != 'Dealer':
        move = input('Hit or Stand?').lower()
        if move == 'hit':
            hit()
            cal()
        elif move == 'stand':
            stand()
# Pay
assign1()
print(playerhand)
print(bets)
print(bets.get("Peter"))
