#Katie Frymire
#2/17/22


#war card game
#make a list with this
#deck of cards with each suit


from operator import truediv
import random, os, time
os.system('cls')




# class card():
#     global suit
#     global rank

#     def __init__(self,suits,rank):
#         self.suit= suits
#         self.rank=rank
#         self.value=value

numberCards=[]
for i in range (2,11):
    numberCards.append(i)
    numberCards[i-2]=str(numberCards[i-2])
print (numberCards)


# suits=''
# #variables of thing about the cards
# suits= ['♠', '♦', '♥', '♣']
# rank= ['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']

# values={'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six' : 6 , 'Seven' :7, 'Eight': 8,'Nine':9,
#           'Ten':10,'Jack':11, 'Queen': 12,'King': 13,'Ace':14 }

#first let's import random since we will be shuffling
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


    print("player1 ",player1)
    print()
    print("player2 ",player2)

theDeck()
shuffleDeal()

gameOn=True
def splitDeck():
    global halfDeck
    global plyr1
    global plyr2
    halfDeck=int(len(deck)/2)
    plyr1=0
    plyr2=0
    #ask user to hit a key to release cards

splitDeck()

while gameOn:      
    for i in range (0,halfDeck):
        click=input("Press a any key to get cards")
        print("Player 1     Player 2")
        print("     "+player1[i]+"      "+player2[i])
        if player1[i]>player2[i]:
            tempPlayer1.extend(player1[i])
            tempPlayer1.extend(player2[i])
            player1.pop(i)
            player2.pop(i)

        elif player1[i]<player2[i]:
            tempPlayer2.extend(player1[i])
            tempPlayer2.extend(player2[i])
            player1.pop(i)
            player2.pop(i)
        print("Player I: "+str(plyr1)+"     Player II: "+ str(plyr2))

    if len(tempPlayer2==0):
        print("Player one won the game ")
        gameOn=False
    elif len(tempPlayer1==0):
        print("Player two won the game ")
        gameOn=False
    else:
        player1.extend(tempPlayer1)
        player2.extend(tempPlayer2)
        




