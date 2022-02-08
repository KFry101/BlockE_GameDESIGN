#Katie Frymire
#2/8.22
#a word game with 3 levels

import os, random
os.system ('cls')

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
    print("#       4. Periodic Table                #")
    print("#                                        #")
    print("##########################################")
    print("""Game Rules: choose a catagorie and
     enter letters to guess the word\n""")
    #word bank
   


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
     
    fruits= ['grapes', 'watermelon', 'apple', 'orange', 'tomato', 'kiwi', 'papaya', 'strawberries', 'blackberries' ]
    animals=['cats', "wolves", "parrots","squirrel","dolphin", "shark", "fox","lizard", "turtle", "gecko","elephant"]
    compParts=[ 'mouse','screen','keyboard', "console", "trackpad", "motherboard","ram","cpu",]
    


    if choice==1:
        word=random.choice(fruits)
    elif choice==2:
        word=random.choice(animals)
    else:
        word=random.choice(compParts)
    

    check = True
    while check:
        try:
            choice= int(input("Choice:  "))
            if choice > 0 and choice < 4:
                check = False
        except ValueError:
            print("Sorry, try again")
print(word)
#guessing fuction
def guessFunction():
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

gameOn=True
tries=0
letterGuessed=""
select()
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
        print("Do you want to play again? (Y/N)")
        ans= input()
        if ans=='y' or ans== 'Y':
                os.system ('cls')
                menu()
                select()
        else: 
                gameOn=False 
        print("\n")

    if countLetter == len(word):
        print('\nYay')
        print("Your score is",(len(word)*5-2*(tries)))
   
        print("Do you want to play again? (Y/N)")
        ans= input()
        if ans=='y' or ans== 'Y':
            os.system ('cls')
            menu()
            select()
        else: 
            gameOn=False 
        print("\n")


    

    
# gameOn=True
# check=True
# turns=0
# while gameOn:
#     letter=input("Guess a letter: " )
#     turns= turns+1
#     for i in range (len(word)):
#         if letter== word[i]:
#             print( letter, end=" ")
#         else:
#             print("_", end=" ")
#     if len(letter)>1 or not letter.isalpha():  #isalpha varible HAS to be alphabet
#         print("Please enter a valid guess")
#     else:
#         if letter== word[i]:
#             letter=input("Guess a letter: " )
#             turns= turns+1
#         else:
#             letter=input(" Guess a letter: " )
#             turns= turns+1
#     for i in range (len(word)):
#         if  letter== word[i]:
#             print( letter, end=" ")
#             turns=turns+1
#         else:
#             print("_", end=" ")
#     if turns== 5 and gameOn: #doesn't work??????
#         print("\nSorry you did not guess the word")
#         gameOn = False
# print ("the word was " + word)
        
    
         

