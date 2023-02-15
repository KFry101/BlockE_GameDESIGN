import os
import random 

#next line clears terminal each time program is ran
os.system('cls') 

#This is the list of character that the random generation/method with access
characters= ["a","b","c","d","e","f","g","h","i","j","k","l","m",'n',"o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F",'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
'0','1','2','3','4','5','6','7','8','9','!','"','#','$','%','&','*','+',':','?','@']

#define the method and the parameter "leng"
def getPassword(leng):

    #defines pssword variable
    password = ""

    
    if int(leng)<6:
        print("This password is will not be safe. Please try again.")
    else:
        for i in range(int(leng)):
         password= password + random.choice(characters) #this line of code is modified from https://pynative.com/python-generate-random-string/ 
        print(password)

#calls the method and requests user input for the parameter "leng"
getPassword(input('length of password: '))