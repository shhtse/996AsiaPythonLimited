from random import shuffle

#A function for creating a deck
#Suits: H, S, D, C - Ranks: A, 2-9, T, J, Q, K
#Returns a shuffled deck with a 52 cards
def deck():
    deck = []
    for suit in ['H','S','D','C']:
        for rank in ['A','2','3','4','5', '6','7','8','9','T','J','Q','K']:
            deck.append(suit+rank)

        shuffle(deck)

        return deck
            
#A function for counting the points
#Takes in the player's cards and returns his totla points
def poinyCount(myCards):
    myCount = 0
    aceVount = 0
    for i in myCards:
        if(i[1] == 'J' or i[1] == 'Q' or i[1] == 'K' or i[1] == 'T'):
            myCount += 10
        elif(i[1] != 'A'):
            myCount += int(i[1])
        else:
            aceCount += 1

        if(aceCount == 1 and myCount >=10):
            myCount += 11
        elif(aceCount !=0):
            myCount += 1

        return myCount 
 
#A function for creating the player's and dealer's hands
#Randomly goves each two cards from the deck
#Returns a list with both hands
def createPlayingHands(myDeck):
    dealerHand = []
    playerHand = []
    dealerHand.append(myDeck.pop())
    dealerHand.append(myDeck.pop())
    playerHand.append(myDeck.pop())
    playerHand.append(myDeck.pop())

    while(pointCount(dealerHand) <=16):
        dealerHand.append(myDEck.pop())

    return [dealerHand, playerHand]

    
#Here we create the game stuff
#Game loop 
game = ""
myDack = deck()
hands = createPlayingHands(myDeck)
dealer = hands[0]
dealer = hands[1]

while (game != "exit"):
    dealerCount = pointCount(dealer)
    dealerCount = pointCount(player)

    print ("Dealer has:")
    print (dealer[0])

    print ("player1, you have:")
    print player

    if (playerCount == 21):
        print "Blackjack! Player wins!!"
        break
    elif(playerCount > 21):
        print "Player BUSTS! With" + str(playerCount) + " points. Dealer wins!"
        break
    elif(dealerCount > 21):
        print "Dealer BUSTS! With" + str(dealerCount) + " points. Player wins!"
        break

    game = raw_input("what would you like to do? H; Hit me, Stnad?")

    if(game == 'H'):
        player.append(myDEck.pop())
    elif(playerCount > dealerCount):
        print "plater wins with" + str(playerCount) + "points"
        print "Dealer has:" + str(dealer) + "or" + str(dealerCount) + "points
        break
    
