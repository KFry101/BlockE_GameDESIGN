#Katie Frymire
#1/27/22

#Rock, paper, scissors Game


import os
os.system('cls')



import random
# user= input("Rock, paper, or scissor ")
# computer =1

# if 'pap' in user:
#     user= int(1)
#     print("paper"+str(user))
# elif 'ro' in user:
#     user=int(2)
# elif 'sc' in user:
#     user= int(3)


#Psuedocode
#add menu 1=paper, 2=rock 3=scissor
#needs user input() for rock paper or scissors
#need computer to generate random number (1,3)
#set up a system for rock beats scissors, paper beats rock, etc.
    #if, elif, and else statments and print ()
        #if user is paper, if computer = 1 print("Its a tie") , etc




comp=random.randint(1,3)
choice=""
def menu():
    print("                            ")
    print("###################################")
    print("#   Rock, paper, scissors Game    #")
    print("###################################")
    print("                               ")
    print("Winning Rules of the Rock paper scissor game as follows: \n""Rock vs paper->paper wins \n""Rock vs scissor->Rock wins \n""paper vs scissor->scissor wins\n")
    print(" Enter choice ")
    print("  [1] Rock                         ")
    print("  [2] Paper                        ")
    print("  [3] Scissors                     ")
    print("                               ")


    global choice
    check = True
    while check:
        try:
            choice= int(input("Player choice: "))
            if choice > 0 and choice < 4:
                check = False       
        except ValueError:
            print("Sorry, try again")

menu()

#number to words
gameOn=True
while gameOn:
    if choice==1:
        choiceType= 'Rock'
    elif choice==2:
        choiceType= 'Paper'
    else:
        choiceType= 'Scissors'

    if comp==1:
        compType= 'Rock'
    elif comp==2:
        compType= 'Paper'
    else:
        compType= 'Scissors'

    #display
    print("Player's choice is: " + choiceType,"\n" )
    print("Computer's choice is: " + compType,)
    print(choiceType+ " V/s " + compType, )


    #winning system
    if choice== comp:
        print ("It's a Tie!")
    elif choice==1:
        if comp==2:
            print ("Computer Wins!")
        elif comp==3:
            print ("Player Wins!")
    elif choice==2:
        if comp==1:
            print ("Player Wins!")
        elif comp==3:
            print ("Computer Wins!")
    else:
        if comp==2:
            print ("Player Wins!")
        elif comp==1:
            print ("Computer Wins!") 

  #asking to play agian
    print("Do you want to play again? (Y/N)")
    ans= input()
    if ans=='y' or ans== 'Y':
        os.system ('cls')
        menu()

    else: 
        gameOn=False 
    print("\n")

