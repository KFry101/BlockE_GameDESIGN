#Katie Frymire
#2/17/22


#war card game
#make a list with this
#deck of cards with each suit


import random, os
os.system('cls')

deck=[]
#next, let's start building lists to build the deck
#NumberCards is the list to hold numbers plus face cards
numberCards = []
suits = ['♠', '♦', '♥', '♣']
royals = ["J", "Q", "K", "A"]
tempPlayer1=[]  
tempPlayer2=[]
halfDeck=0
def theDeck():
    global suits
    global royals
    global numberCards
    global deck
    global counter

    #using loops and append to add our content to numberCards :
    for i in range(2,11):
        numberCards.append(str(i))
        #this adds numbers 2-10 and converts them to string data

    for j in range(4):
        numberCards.append(royals[j])
        #this will add the card faces to the base list
    #Create full deck
    for k in range(4):   # four suits
        for l in range(13): #13 cards per suit
            card = (numberCards[l] + " " + suits[k])
            #this makes each card, cycling through suits, but first through faces
            deck.append(card)
            #this adds the information to the "full deck" we want to make
    #you can print the deck here, if you want to see how it looks
    print(deck)
    #now let's see the deck!

def printDeck(): #to print the deck
    counter=0
    for row in range(4):
        for col in range(13):
            print(deck[counter], end=" ")
            counter +=1
        print()

def shuffleDeal():
    global player1
    global player2
    global tempPlayer1
    global tempPlayer2
    #now let's shuffle our deck!
    #Shuffle the deck cards
    random.shuffle(deck)
    player1=[]
    player2=[]
    # you could print it again here just to see how it shuffle
    #loop to devide the cards to each player
    for l in range(52):
        if l%2==0:
            player1.append(deck[l])
        else:
            player2.append(deck[l])


    print("player1 ",len(player1))
    print()
    print("player2 ",len(player2))

theDeck()
shuffleDeal()

gameOn=True
def splitDeck():
    global halfDeck
    halfDeck=int(len(deck)/2)
    #ask user to hit a key to release cards

splitDeck()

while gameOn:
    print()  
    for i in range (0,halfDeck):
        click=input("\nPress any key to get cards: ")
        print("Player 1     Player 2","      Turn: ", i)
        print("     "+player1[i]+"      "+player2[i])
        if player1[i]>player2[i]:
            tempPlayer1.append(player1[i])
            tempPlayer1.append(player2[i])
            # player1.pop(i)
            # player2.pop(i)

        elif player1[i]<player2[i]:
            tempPlayer2.append(player1[i])
            tempPlayer2.append(player2[i])
            # player1.pop(i)
            # player2.pop(i)
    print("End Round")
    print ("Player 1 has ", len(tempPlayer1), " cards   and   Player 2 has ", len(tempPlayer2)," cards" ) #added this for my own flare
    if (len(tempPlayer2))==0:
        print("Player one won the game ")
        gameOn=False
    elif (len(tempPlayer1))==0:
        print("Player two won the game ")
        gameOn=False
    else:
        if len(tempPlayer1)<len(tempPlayer2):
            halfDeck=len(tempPlayer1)
        elif len(tempPlayer2)<len(tempPlayer1):
         halfDeck=len(tempPlayer2)
        other1= player1[halfDeck: ]
        other2=player2[halfDeck: ]
        print(other1)
        print(player1)
        print(other2)
        print(player2)
        if len(player1)>len(player2):
            tempPlayer1.extend(other1)
        elif len(player2)>len(player1):
            tempPlayer2.extend(other2)
        print (tempPlayer1)
        print(tempPlayer2)
        for j in range (0,halfDeck):

            player1.pop(0)
            player2.pop(0)
        player1.extend(tempPlayer1)   
        player2.extend(tempPlayer2)
        tempPlayer1.clear()   #This was the missing piece. the Temp list kept the old temp cards from old lists/past rounds. 
        tempPlayer2.clear()   #That why there was a hand with 75 cards one time.
        if len(player1)<len(player2):
            halfDeck=len(player1)
        elif len(player2)<len(player1):
            halfDeck=len(player2)

        
            




