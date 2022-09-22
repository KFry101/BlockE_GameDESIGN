#Katie Frymire

import os
os.system('cls')
import random
numRolls= int(input("Enter a number: "))

results={2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
for r in range(numRolls):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    total=dice1+dice2
    results[total] = results[total] + 1

for i, key in iter(results.items()):
    actPerct= key/numRolls
    actPerct=round(actPerct,3)
    
    if i<8:
        Predict= (i-1)/36
        Predict= round(Predict,3)
    elif i>7:
        Predict= (13-i)/36
        Predict= round(Predict,3)
    diff= abs(Predict-actPerct)
    diff= round(diff, 3)
    print( "Number: ", i , "\t", "Count: ", key, "\t", "Predicted %: ", Predict, "\t", "Actual %: ", actPerct, "\t", "Deviation: ", diff)
