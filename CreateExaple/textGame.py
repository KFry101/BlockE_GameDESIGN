import os, random
os.system('cls')
list = ["\nAre we friends? ", "\nCan you help me? ", "\nCan we talk? "]
def Convo():
    print(list[random.randint(0,2)])
    response= input("your response:  (Y/N)")
    while (len(response)> 0):
        if  response=='y' or response== 'Y':
            print("thanks, " + name)
        else:
            print("I hate my life")
        print(list[random.randint(0,2)])
        response= input("your response:  (Y/N)")


    

#Main Code 
print("Welcome to the Friendship Simulator")
name= input("What is your name? ")
Convo()

