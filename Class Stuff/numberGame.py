#Katie Frymire
#1/26/22 

import os 
os.system('cls')

import random

#Make a menu 
# choices  1-10
# choices 1 -50
# choices 1-100

print("###################################")
print("#      Guess a number Menu        #")
print("#                                 #")
print("#          1. Guess 1-10          #")
print("#          2. Guess 1-50          #")
print("#          3. Guess 1-100         #")
print("#                                 #")
print("###################################")

print("Please enter a number from 1 to 3")
#Select your choice

check = True
while check:
    try:
        choice= int(input("Choice:  "))
        if choice > 0 and choice < 4:
            check = False
    except ValueError:
        print("Sorry, try again")


if choice==1:
    guess=random.randint(1,10)
elif choice==2:
    guess=random.randint(1,50)
else :
    guess=random.randint(1,100)


gameOn=True 
counter=0
#print(guess)
while(gameOn):
    userGuess= int(input("Guess a number: "))
    userGuess=int(userGuess)
    counter=counter+1
    if guess== userGuess:
        print("You guessed it!!!")
        gameOn=False
    else:
        if userGuess < guess-10:
            print("Too low")
        else:
            if userGuess > guess+10:
                print("Too high")
    if counter ==5 and gameOn:
        print("Sorry you did not guess the number")
        gameOn = False
print("The number to guessed was "+ str (guess))
print("    ")