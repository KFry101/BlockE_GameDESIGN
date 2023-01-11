import os
os.system ('cls')

check=True
def whoInClass():
    name=(input("Whos in your class? "))
    names=[]
    if (len(name)>3):
        names.append(name)
        
    else:
        print("invalid name")


while check:
    whoInClass()