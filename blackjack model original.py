#deck
from random import shuffle
import random

cards1=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
card_color=['紅心','方塊','黑桃','梅花']
new_card=[]
for i in cards1:
    for a in card_color:
        new_card.append(a+i)
#player

#distribute cards
def random_card(cards,num=1):
    cards=cards*num
    shuffle(cards)
    return cards
def game_start(cards):
    if len(cards) < 2:
        global new_cards
        new_cards = random_card(new_card)
        print ('已重新洗牌')
        cards=new_cards
    news=cards.pop()+','+cards.pop()
    return news
def game_next(cards):
    news=cards.pop()
#如果在玩的過程中，牌不夠了，拿一副新牌continue
    if news == None:
        global new_cards
        new_cards = random_card(new_card)
        print ('已重新洗牌！')
        news=new_cards.pop()
    return news
#計分
def score_count(count):
    new_count=0
    news=count.split(',')
#A either 1 or 11
    count_a=0
    for i in news:
        if i[2:].isdigit():
            new_count += int(i[2:])
        elif i[2:].upper() == 'A':
            count_a += 1
        else:
            new_count += 10

#除了A以外，其他全部計算完。計算A加入的total
    if new_count > 10:
        new_count += count_a
    elif count_a == 0:
        new_count += count_a
    else:
        new_count += 10+count_a
    return new_count
#洗牌
new_cards=random_card(new_card)
count_start = True
while count_start:
    print('Welcome to BlackJack')
    print('發牌')
#display players card
    player1_count = game_start(new_cards)
#show points
    new_player1_count = score_count(player1_count)
    print('player1 cards :%s'%player1_count)
    print('player1 points：%s'%new_player1_count)

    player2_count=game_start(new_cards)
    new_player2_count=score_count(player2_count)
    print('player2 cards：%s'%player2_count)
    print('player2 points：%s'%new_player2_count)
    
    player3_count=game_start(new_cards)
    new_player3_count=score_count(player3_count)
    print('player3 cards：%s'%player3_count)
    print('player3 points：%s'%new_player3_count)
    
    player4_count=game_start(new_cards)
    new_player4_count=score_count(player4_count)
    print('player4 cards：%s'%player4_count)
    print('player4 points：%s'%new_player4_count)
    while True:
        moves=input('One more card?(y/n)')
        if moves.lower() == 'y':
            #one more card
                count1=game_next(new_cards)
                player1_count += ',' + count1
                new_player1_count = score_count(player1_count)
                print('player1 cards：%s' % player1_count)
                print('player1 points：%s' % new_player1_count)
                #gameover when points>21
            
                if new_player1_count > 21:
                    new_player1_count = 0
                    print ('Bursted!You lose')
                    break
            #不要牌
        elif moves.lower() == 'n':
                print ('player1 final points%s'%new_player1_count)
                break
    else:
                print ('wrong move！')
    #player 2 move
    
    while True:
           moves=input('One more card?(y/n)')
           if moves.lower() == 'y':
                count2=game_next(new_cards)
                player2_count += ',' + count2
                new_player2_count=score_count(player2_count)
                print('player2 cards：%s' % player2_count)
                print('player2 points：%s' % new_player2_count)
            
                if new_player2_count > 21:
                    new_player2_count = 0
                    print ('Bursted!You lose')
                    break
           elif moves.lower() == 'n':
                print ('player2 final points%s'%new_player2_count)
                break
    else:
                print ('wrong move！')
    
    while True:
           moves=input('One more card?(y/n)')
           if moves.lower() == 'y':
                count3=game_next(new_cards)
                player3_count += ',' + count3
                new_player3_count=score_count(player3_count)
                print('player3 cards：%s' % player3_count)
                print('player3 points：%s' % new_player3_count)
            
                if new_player3_count > 21:
                    new_player3_count = 0
                    print ('Bursted!You lose')
                    break
           elif moves.lower() == 'n':
                print ('player3 final points%s'%new_player3_count)
                break
    else:
                print ('wrong move！')
   
    while True:
           moves=input('One more card?(y/n)')
           if moves.lower() == 'y':
                count4=game_next(new_cards)
                player4_count += ',' + count4
                new_player4_count=score_count(player4_count)
                print('player4 cards：%s' % player4_count)
                print('player4 points：%s' % new_player4_count)
            
                if new_player4_count > 21:
                    new_player4_count = 0
                    print ('Bursted!You lose')
                    break
           elif moves.lower() == 'n':
                print ('player4 final points%s'%new_player4_count)
                break
    else:
                print ('wrong move！')
    while True:            
        count_list=[new_player1_count,new_player2_count,new_player3_count,new_player4_count]
        if (new_player1_count>21):
            count_list.remove(new_player1_count)
        if (new_player2_count>21):
            count_list.remove(new_player2_count)
        if (new_player3_count>21):
            count_list.remove(new_player3_count)
        if (new_player4_count>21):
            count_list.remove(new_player4_count)
        n=max(count_list)
        if n==new_player1_count:
            print('player1 win')
            break
        if n==new_player2_count:
            print('player2 win')
            break
        if n==new_player3_count:
            print('player3 win')
            break
        if n==new_player4_count:
            print('player4 win')
            break
        