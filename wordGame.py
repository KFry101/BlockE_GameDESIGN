#Katie Frymire
#started 2/6/22
#a word game

import os, random
os.system ('cls')

words=""
word=""

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
    while check:
        letter=input("Dear user, please give us a nice letter " )
        if len(letter)>1 or not letter.isalpha():  #isalpha varible HAS to be alphabet
            print("Bad")
        else:
            check=False
            gameOn=False
    for i in range (len(word)):
        if letter== word[i]:
            print( letter, end=" ")
        else:
            print("_", end=" ")

