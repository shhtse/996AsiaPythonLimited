
class Base_setting:
    def playerinfo(self):
        while True:
            try:
                playerlist = []
                playernum = int(input("""
                    Welcome to the BlackJack World !\n How many players you want to create?
                    (Please enter the number from 1 to 9) """))
                if playernum >= 1 and playernum < 10:
                    for player in range(playernum):
                        naming = input("Player, {}, please enter your name:   ".format(player +1))
                        playerlist.append(naming)
                    print("So we have the followings players:,{}, \n\nThe game will start after 3 seconds".format(playerlist))
                    time.sleep(3)
                    return playerlist
                    break
                else:
                    print('Sorry, out of range,please try again!\n')
            except ValueError:
                print("Sorry, I don't understand what you mean, please try again!\n")
          

    def cardset(self):
        suit = ["Spade", "Heart", "Club", "Diamond"]
        face = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        cardset = [(s + " " + f) for s in suit for f in face]
        return cardset
    

    def point(self):
        fvalue = ["(1, 11)", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10"]
        fv =[]
        n = 4
        while n >0:
            n -= 1
            for fs in fvalue:
               fv.append(fs)
        cards= self.cardset()
        pt = dict(zip(cards, fv))
        return pt



