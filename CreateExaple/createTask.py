#imports library for random
import random

#This is the list of character that the random generation/method will access
characters= ["a","b","c","d","e","f","g","h","i","j","k","l","m",'n',"o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F",'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
'0','1','2','3','4','5','6','7','8','9','!','"','#','$','%','&','*','+',':','?','@']

#define the method and the parameter "leng"
def getPassword(leng):
    #declare password variable
    password = ""
    #branching path for test case 1
    if int(leng)<6:
        print("This password is may not be secure. Please something longer.")
   #branching path for test case 2
    else:
        #a loop thorugh 0 to paramenter leng
        for i in range(int(leng)):
         #redeclares the passsword variable to a randomly selected elements from the characters list
         password= password + random.choice(characters) #this line of code is modified from https://pynative.com/python-generate-random-string/ 
        print(password)

#calls the method and requests user input for the parameter "leng"
getPassword(input('length of password: '))