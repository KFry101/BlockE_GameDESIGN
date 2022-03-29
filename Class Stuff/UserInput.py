#Katie Frymire
#1/21/22

import os
os.system ('cls')

import random

#Going to learn the input() function, typecasting, branching, looping, random
 
#Variables
# print("Enter a number from 1-10:", end=" ")
# userInfo=int(input()) #input returns in strings
# print("This number is %.2f" %(userInfo/3))
# guess=int(input("Please give me a number"))

#Guess a number
#myNumber=9; intsead of fixed number--> random
myNumber=random.randint(1,10)
print("######################################################################")
print("#                                                                    #")
print("#                          Guess a number                            #")

GameOn=True 
while(GameOn):
    userGuess= int(input("Guess a number from 1-10: "))
    if myNumber== userGuess:
        print("You guessed it!!!")
    else:
        print("Try Again...")
print("The number to guessed was"+ str (myNumber))

