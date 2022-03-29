#Katie Frymire
#2/8.22
#a word game with 3 levels

import os, random, time
os.system ('cls')

cont=''
def contin():
    global cont
    cont=input(str("Enter anything to continue "))
    if cont.isalpha():
        os.system('cls')
        menu()
        select()
    
#menu way of seeing the scores and leaderboard
def leaderBoard():
    print(highscore)
#quit game code of the menu
def quit():
    os.system ('cls')
    print("THANKS FOR PLAYING")
    time.sleep(1) #delay for 1 seconds
    print("COME BACK SOON")
    time.sleep(2) #delay for 2 seconds
    os.system ('cls')
    exit()


cont=""
animals=""
fruits=""
guess=''
word=""
compParts=""
countLetter=""
choice=""
periodTable=""
#menu
def menu():
    print("##########################################")
    print("#                                        #")
    print("#               Word Game:               #")
    print("#                                        #")
    print("#       1. Fruit                         #")
    print("#       2. Animals                       #")
    print("#       3. Computer Parts                #")
    print("#       4. Leader board                  #")
    print("#       5. Exit Game                     #")
    print("#                                        #")
    print("##########################################")
    print("""Game Rules: choose a catagorie and
     enter letters to guess the word\n""")
    
   


menu()

#word list
def select():
    global choice
    global word 
    global fruits
    global animals
    global compParts 
    global guess
    global countLetter
    global cont 
    #the wordlist for choices
    fruits= ['grapes', 'watermelon', 'apple', 'orange', 'tomato', 'kiwi', 'papaya', 'strawberries', 'blackberries' ]
    animals=['cats', "wolves", "parrots","squirrel","dolphin", "shark", "fox","lizard", "turtle", "gecko","elephant"]
    compParts=['mouse','screen','keyboard', "console", "trackpad", "motherboard","ram","cpu", "camera", "microphone"]
    

    #choicing your choice
    check = True
    while check:
        try:
            choice= int(input("Choice:  "))
            if choice > 0 and choice < 6:
                check = False
        except ValueError:
            print("Sorry, try again")
    
    if choice==1:
        word=random.choice(fruits)
    elif choice==2:
        word=random.choice(animals)
    elif choice==3:
        word=random.choice(compParts)
    elif choice==4:
        leaderBoard()
        print(highscore)
    else:
        quit()
    

   
    
print(word)
#guessing fuction
def guessFunction():
    global cont
    global guess
    check=True
    while check:
        try:
            guess= input('\nguess a letter: ')
            if guess.isalpha() and len(guess)==1:
                check=False
            else:
                print('enter a valid letter')
        except ValueError:
            print('enter a valid letter')

#what happen when they what it play again
def playAgain():
    os.system ('cls')
    menu()
    select()
    global tries
    global letterGuessed
    tries=0
    letterGuessed=''
    guess=''
    letter=''

gameOn=True
tries=0
letterGuessed=""
select()
tries=0
highscore=0
while gameOn:
    guessFunction()
    letterGuessed += guess 
    if guess not in word:
        tries+=1
        print(tries)
    countLetter=0
    for letter in word:
        if letter in letterGuessed:
            print(letter, end=" ")
            countLetter+=1
        else:
            print ('_', end=" ")
    if tries>5:
        print ("\n run out of tries")
        print ("the word was " + word)
        # print("Do you want to play again? (Y/N)")
        # ans= input()
        # if ans=='y' or ans== 'Y':
        #         playAgain()
        # else: 
        #         gameOn=False 
        print("\n")
        contin()

    if countLetter == len(word):
        points=(len(word)*5-2*(tries))
        print('\nYay')
        print("Your score is", points )
        if points > highscore:
            highscore=points
        points=0
        contin()
   
        # print("Do you want to play again? (Y/N)")
        # ans= input()
        # if ans=='y' or ans== 'Y':
        #     playAgain()
        # else: 
        #     gameOn=False 
        #     print("Your highscore was ", highscore)
        #     print("\nThank for playing\n")
        #     time.sleep(2)
        #     os.system('cls')
        #     exit()


   
         

