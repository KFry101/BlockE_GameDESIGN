import os, random
os.system('cls')
list = ["\nAre we friends? ", "\nCan you help me? ", "\nCan we talk? ", ]

def Convo(Ans):
    while (len(Ans)> 0):
        if  Ans=='y' or Ans== 'Y':
            print(name+ ": Thanks")
        else:
            print(name+ ": I hate my life")
        break


    

#Main Code 
print("Welcome to the Friendship Simulator")
name= input("What is your friend's name? ")
print(list[random.randint(0,2)])
response= input("your response:  (Y/N)")
Convo(response)

