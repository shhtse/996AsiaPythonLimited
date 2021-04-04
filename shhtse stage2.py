import random
#chip, insurance, side bet, double, split
#BlackJack pays 3 to 2
class Player:
    def __init__(self, name, hand, bust, point, chip):
        self.name = name
        self.hand = hand
        self.bust = bust
        self.point = point
        self.chip ＝ chip
    def __repr__(self):
        return (self.name, self.hand, self.point)
suit = ['♠','♥','♣','♦']
face = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
deck = []
name = ["Dealer"]
def player_info():
    global n
    n = int(input("How many players do you have?"))
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
            name.append(input('What is the name of the ' + str(i) +' th player?'))
    for i in range(n+1):
        name[i] = Player(name[i], [], False, 0)
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
shuffle()
name[0].hand.append('?')
hit(0)
cal(0)
print(f'{name[0].__repr__()}\n')
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
            print(f'{name[k].__repr__()} Blackjack!! See if the Dealer gets a blackjack too.')
            continue
        decision = input(f'{name[k].__repr__()}, do you want to hit or stand?').lower()
        if decision == 'hit':
            hit(k)
            cal(k)
            if cal(k) > 21:
                name[k].bust = True
                finished_player.append(name[k].name)
                print(f'{name[k].__repr__()} Bust!!')
            elif cal(k) == 21:
                finished_player.append(name[k].name)
                print(f'{name[k].__repr__()} Blackjack!! See if the Dealer gets a blackjack too.')
            else:
                print(name[k].__repr__())
        if decision == 'stand':
            finished_player.append(name[k].name)
name[0].hand.remove('?')
hit(0)
name[0].hand.reverse()
cal(0)
while name[0].point <17:
    hit(0)
    cal(0)
print(f'{name[0].__repr__()}\n')
for k in range(n+1):
    if k == 0 :
        continue
    if name[k].point > 21:
        print(f'{name[k].__repr__()}\nBusted!\n')
    elif name[k].point == name[0].point:
        print(f'{name[k].__repr__()}\n{name[0].__repr__()}\n打和啦Super!!\n')
    elif name[k].point == 21:
        print(f'{name[k].__repr__()}\n{name[0].__repr__()}\nBlackjack!! You win!!\n')
    elif name[0].point > 21:
        print(f'{name[k].__repr__()}\n{name[0].__repr__()}\nDealer busted, you win\n')
    elif name[k].point < name[0].point:
        print(f'{name[k].__repr__()}\n{name[0].__repr__()}\nYou lose\n')
    else:
        print(f'{name[k].__repr__()}\n{name[0].__repr__()}\nYou win\n')