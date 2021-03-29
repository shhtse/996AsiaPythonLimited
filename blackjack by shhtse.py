import random
player_hand=[]
dealer_hand=[]
deck = []

def shuffle():
    a= 1
    while a<5:
        for i in range(13):
            if i == 1:
                deck.append('A')
            elif i  == 11 :
                deck.append('J')
            elif i  == 12 :
                deck.append('Q')
            elif i  == 0 :
                deck.append('K')
            else:
                deck.append(i)
        a += 1
        
    random.shuffle(deck)

def hit():
    card = deck.pop()
    player_hand.append(card)

def dealer_hit():
    card = deck.pop()
    dealer_hand.append(card)

def cal():
    player_pt = 0
    for i in player_hand:
        try:
            player_pt += i
        except:
            if i == 'A':
                if player_pt > 10:
                    player_pt += 1
                else:
                    player_pt += 11
            else:
                player_pt += 10
    return player_pt

def dealer_cal():
    dealer_pt = 0
    for i in range(len(dealer_hand)):
        if i == 0:
            continue
        try:
            dealer_pt += dealer_hand[i]
        except:
            if i == 'A':
                if dealer_pt > 10:
                    dealer_pt += 1
                else:
                    dealer_pt += 11
            else:
                dealer_pt += 10
    return dealer_pt

shuffle()
for i in range(2):hit()
cal()
print('Player hand :', player_hand,'. Player point =',cal())
for i in range(2):dealer_hit()
dealer_cal()
print('Dealer hand : [?], ',dealer_hand[1:],'. Dealer point =',dealer_cal())
decision = input('Hit or stand?(H) or (S)').lower()
while decision != 's':
    hit()
    cal()
    print('Player hand :', player_hand,'. Player point =',cal())
    if cal() > 21:
        print('Bust!')
        break
    if cal() == 21:
        break
    decision = input('Hit or stand?(H) or (S)').lower()
if cal() <= 21:
    while dealer_cal() < 17:
        dealer_hit()
        dealer_cal()
    print('Dealer hand : ',dealer_hand,'. Dealer point =',dealer_cal())
    if cal() == dealer_cal() :
      print('打和啦Super!!')
    elif cal() == 21:
      print('BlackJack! You win.')
    elif dealer_cal() == 21:
      print('Dealer has a BlackJack')
    elif dealer_cal() >21:
      print('Dealer bust, you win')
    elif cal() < dealer_cal():
      print('You loss')
    else:
        print('Yon win')
