#Katie Frymire
#2/16/22

import os, random
os.system ('cls')

#In Class notes about arrays, indexs, collections, lists and list method

#lists and tuples very similar
    #List [] 
        #ordered and changable
        #allows duplicated members

    #tuples()
        #order and unchangable
        #Allows duplicate      
#dictaionary
    #unordered and changable
    #no duplicates
#LISTS
#Hetrogenous
#allows duplicat
#ordered
#changable

#Append() ----> adds elemants at end of list
#extend() ----> adds elements to a list; bring each elements themselves
#insert() ----> adds in specfic spot
#pop () ----> rmove a certain postion
#remove()-----> removes certain value

#Exaples:
fruits= ['grapes', 'watermelon', 'apple', 'orange', 'tomato', 'kiwi', 'papaya', 'strawberries', 'blackberries' ]

fruits.append('rambutan')

#length of array
size= len(fruits)
print(size)
for i in range(size):
    print(fruits[i])
print (fruits[size-1])
print (fruits[size-2])
print(fruits.count("grapes"))

list2=[3,6,8,9,10]
fruits.append(list2)
print(fruits)