#Katie Frymire
#started 2/6/22
#a word game

import os, random
from pickle import FALSE
os.system ('cls')

words=""
word=""
letter=''
#menu
def menu():
    print("##########################################")
    print("#                                        #")
    print("#               Word Game:               #")
    print("#                                        #")
    print("##########################################")
    print("Game Rules: enter letters to guess the word\n")
    #word bank
    global words
    global word
    words=["radio", "clues", "suite","peter", "robot", "moist","apple" ]
    word=random.choice(words)
    print(word)

    global letter 
    
    
menu()
gameOn=True
check=True
turns=0
while gameOn:
    letter=input("Guess a letter: " )
    turns= turns+1
    for i in range (len(word)):
        if letter== word[i]:
            print( letter, end=" ")
        else:
            print("_", end=" ")
    if len(letter)>1 or not letter.isalpha():  #isalpha varible HAS to be alphabet
        print("Please enter a valid guess")
    else:
        if letter== word[i]:
            letter=input("Guess a letter: " )
            turns= turns+1
        
        else:
            letter=input(" Guess a letter: " )
            turns= turns+1
    for i in range (len(word)):
        if  letter== word[i]:
            print( letter, end=" ")
            turns=turns+1
        else:
            print("_", end=" ")
    if turns== 5 and gameOn: #doesn't work??????
        print("\nSorry you did not guess the word")
        gameOn = False
print ("the word was " + word)
        
    
         

