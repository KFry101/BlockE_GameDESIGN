#Katie Frymire
#1/31/22
#strings array of characters
#many functions

import os
os.system ('cls')

import random

myName= "Katie Frymire"
#""" = keeps formating in the print function
myStatment= """my name is no nice blah
blah 
abal"""

#index starts with 0
print(myName[6])
print( 'my last name stars with '+ myName[6] )

print(myStatment)
if 'blah' in myStatment:
    print('true')
print('expert' not in myStatment)

##############################################
#2/2/22
#continue of last class; 
# preping for word game and 'For loops', and lowercase and uppercase,
#for loop---> counting; while loops --->condition



for elem in myStatment:
    print(elem, end=" ")

guess=random.choice(myName)
print(guess)

words=["radio", "clues", "suite","peter", "robot"]
word=random.choice(words)
print(word)


#find() will return the index of the character you are looking for (first instance)
Dex=myName.find("a")
print(Dex)
#finding the length of your word
wordLen=len(myName)
print(wordLen,"\n") # your last len is index -1


#FOr loop in range 0 to limit
for i in range(wordLen-1):
    if "a" in myName[i]:
        print(i, end=", ")
print(" ")
print("done")
myStatment=myStatment.lower()
print(myStatment)


check=True
while check:
    letter=input("Dear user, please give us a nice letter " )
    if len(letter)>1 or not letter.isalpha():  #isalpha varible HAS to be alphabet
        print("Bad")
    else:
        check=False
print( "ready to play the Game")
for i in range (len(word)):
    if letter== word[i]:
        print( letter, end=" ")
    else:
        print("_", end=" ")


