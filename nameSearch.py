#Katie Frymire
#user searchs name and give numbers for years
import os
os.system('cls')
nameLib={}
Name= input("Enter a name: ")
import csv
with open('Names.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        nameLib[row["NAME"]]={row["YEAR"]: row["NUMBER"]}
        if row["NAME"] in nameLib:
            nameLib.append({row["YEAR"]: row["NUMBER"]})
# Eric Idle
# John Cleese

try:
    print(nameLib[Name])
except:
    print("name is not valid for search")

