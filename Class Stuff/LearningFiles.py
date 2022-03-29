#Katie Frymire
#Learning files:
#a) open and create a file
#B) write 'w'
#C) append 'a'
#D) read 'r'
#E) close() 

import pygame, os, datetime
os.system('cls')
date=datetime.datetime.now()
score=123
name='Jesse'
print(date.strftime('%m/%d/%Y'))
scoreLine=str(score)+" "+name+" "+date.strftime('%m/%d/%Y')
print (scoreLine)

myFile=open('Class Stuff\score.txt')