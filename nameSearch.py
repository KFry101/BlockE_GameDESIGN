#Katie Frymire
#user searchs name and give numbers for years
import os
os.system('cls')

nameLib={}

import csv
with open('Names.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name= row["NAME"]
        year=row["YEAR"]

        if not (name in nameLib):
            nameLib[name]={}

        if not (year in nameLib[name]):
            nameLib[name][year]=int(row["NUMBER"])
        else: 
            nameLib[name][year]+= int(row["NUMBER"])
        

nameS= input("Enter a Namem (Case-Sensitive): ")   
key=nameS          
try:
    print(key)
    print("2021: ", nameLib[key]["2021"])
    print("2020: ", nameLib[key]["2020"])
    print("2019: ", nameLib[key]["2019"])
    print("2018: ", nameLib[key]["2018"])
    print("2017: ", nameLib[key]["2017"])

except:
    print("Name is not valid for search.")

