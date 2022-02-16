#card game


numberCards=[]
for i in range (2,11):
    numberCards.append(i)
    numberCards[i-2]=str(numberCards[i-2])
print (numberCards)
suits= 2
royals=3

#make a list with this