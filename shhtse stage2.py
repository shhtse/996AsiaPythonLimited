import random
class Player:
    def __init__(self, name, hand, point, chip, bet):
        self.name = name
        self.hand = hand
        self.point = point
        self.chip = chip
        self.bet = bet
    def __str__(self):
        return f'{self.name} has {self.hand} in hand, {self.point} point, bet for ${self.bet} this round, amount of remaining chips is ${self.chip}.'
suit = ['♠','♥','♣','♦']
face = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
deck = []
name = ["Dealer"]
def player_info():
    global n
    n = int(input("Each player has $1000 at the beginning.\nThe entrance fee is $10 for each game.\nBlackJack pays 3 to 2\nHow many players do you have?"))
    for i in range(n+1):
        if i == 0:
            continue
        if i == 1:
            name.append(input('What is the name of the ' + str(i) + ' st player?'))
        if i == 2:
            name.append(input('What is the name of the ' + str(i) + ' nd player?'))
        if i == 3:
            name.append(input('What is the name of the ' + str(i) + ' rd player?'))
        if i >= 4:
            name.append(input('What is the name of the ' + str(i) + ' th player?'))
    for i in range(n+1):
        if i == 0:
            name[0] = Player(name[0],[],0,0,0)
            continue
        name[i] = Player(name[i],[],0,1000,0)
def shuffle():
    for i in range(n):
        for w in suit:
            for p in face:
                deck.append(w+p)
        random.shuffle(deck)
def hit(k):
    card = deck.pop()
    name[k].hand.append(card)
def cal(k):
    name[k].point = 0
    for i in range(len(name[k].hand)):
        if name[k].hand[i] == '?' :
            continue
        if name[k].hand[i][1] == 'A':
            name[k].point += 1
        elif name[k].hand[i][1] == 'J' or name[k].hand[i][1] == 'Q' or name[k].hand[i][1] == 'K' or name[k].hand[i][1] == '1':
            name[k].point += 10
        else:
            name[k].point += int(name[k].hand[i][1])
    if ('♠A' in name[k].hand or '♥A' in name[k].hand or '♣A' in name[k].hand or '♦A' in name[k].hand) and name[k].point <= 11:
        name[k].point += 10
    return name[k].point
player_info()
while True:
    for i in range(n+1):
        name[i].hand = []
        name[i].bet = 0
    shuffle()
    name[0].hand.append('?')
    hit(0)
    cal(0)
    print(f'Dealer has {name[0].hand} in hand, {name[0].point} point.\n')
    for k in range(n+1):
        if k == 0:
            continue
        hit(k)
        hit(k)
        cal(k)
    finished_player = []
    while True:
        if len(finished_player) == n:
            break
        for k in range(n+1):
            if k == 0:
                continue
            if name[k].name in finished_player:
                continue
            if name[k].point == 21:
                print(f'{name[k].__str__()} Blackjack!! See if the Dealer gets a blackjack too.')
                finished_player.append(name[k].name)
                continue
            while name[k].bet == 0:
                bet = int(input(f'{name[k].name}, how much do you want to bet for this round? (At least $10)'))
                if bet < 10:
                    bet = int(input('You have to bet for AT LEAST $10'))
                if bet >= 10:
                    name[k].bet = bet
                    name[k].chip -= name[k].bet
            decision = input(f'{name[k].__str__()}Do you want to hit or stand?').lower()
            if decision == 'hit':
                hit(k)
                cal(k)
                if cal(k) > 21:
                    finished_player.append(name[k].name)
                    print(f'{name[k].__str__()} Bust!!')
                elif cal(k) == 21:
                    finished_player.append(name[k].name)
                    print(f'{name[k].__str__()} Blackjack!! See if the Dealer gets a blackjack too.')
                else:
                    print(name[k].__str__())
            if decision == 'stand':
                finished_player.append(name[k].name)
    name[0].hand.remove('?')
    hit(0)
    name[0].hand.reverse()
    cal(0)
    while name[0].point <17:
        hit(0)
        cal(0)
    print(f'Dealer has {name[0].hand} in hand, {name[0].point} point.\n')
    for k in range(n+1):
        if k == 0 :
            continue
        if name[k].point > 21:
            print(f'{name[k].__str__()}\nBusted!\n')
        elif name[k].point == name[0].point:
            name[k].chip += name[k].bet
            print(f'{name[k].__str__()}\nDealer has {name[0].hand} in hand, {name[0].point} point.\n打和啦Super!!\n')
        elif name[k].point == 21:
            name[k].chip += 1.5 * name[k].bet
            print(f'{name[k].__str__()}\nDealer has {name[0].hand} in hand, {name[0].point} point.\nBlackjack!! You win!!\n')
        elif name[0].point > 21:
            name[k].chip += 2 * name[k].bet
            print(f'{name[k].__str__()}\nDealer has {name[0].hand} in hand, {name[0].point} point.\nDealer busted, you win\n')
        elif name[k].point < name[0].point:
            print(f'{name[k].__str__()}\nDealer has {name[0].hand} in hand, {name[0].point} point.\nYou lose\n')
        else:
            name[k].chip += 2 * name[k].bet
            print(f'{name[k].__str__()}\nDealer has {name[0].hand} in hand, {name[0].point} point.\nYou win\n')
    bankrupt_player = []
    for k in range(n+1):
        if k ==0:
            continue
        if name[k].chip <= 0:
            bankrupt_player.append(name[k].name)
    if len(bankrupt_player) != 0:
        print('We have player goes bankrupt.')
        break
    again = input('Do you want to player again?(Yes / No)').lower()
    if again == 'no':
        break
for k in range(n+1):
    if k == 0:
        continue
    print(f'{name[k].name} has ${name[k].chip}.')
