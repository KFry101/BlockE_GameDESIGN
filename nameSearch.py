#Katie Frymire
#user searchs name and give numbers for years
import os
os.system('cls')

nameLib={}
years=[2016, 2017, 2018, 2019, 2020, 2021]
Name= input("Enter a name (Case-Sensitive): ")
key=Name
import csv
with open('Names.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    #Old Code
    # for row in reader:
    #     nameLib[row["NAME"]]={row["YEAR"]: row["NUMBER"]}
    #     if row["NAME"] in nameLib:
    #        

#New Code
if not (Name in nameLib):
    nameLib[key]={}

if not (years in nameLib):
    nameLib[key][years]=10
else: 
    nameLib[key][years]= nameLib[key][years]+10

    
try:
    print(nameLib[key])
    print(nameLib[key][years])
except:
    print("Name is not valid for search.")

