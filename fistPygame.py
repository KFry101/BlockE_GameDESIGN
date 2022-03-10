#katie frymire
#3/4/22
#first pygames in class,

#Import needed things
import os,time
import pygame as p
os.system('cls')

#initalize pygame
p.init()

#define colors with RGB values
white=[255, 255, 255]
red=[255, 0, 0]
mag=[255, 0, 255]
aqua=[51, 153, 255]
m=[47,192,229]


#CREATE THE SCREEN
WIDTH=600 #pixels
HEIGHT=700
screen=p.display.set_mode((WIDTH,HEIGHT))
p.display.set_caption("My window") #title of window

#  screen.fill(m)
# p.display.update()
# p.time.delay(5000) #miliseconds
# screen.fill(aqua)
# p.display.update()
# p.time.delay(5000) #miliseconds
# screen.fill(white)
# p.display.update()
# p.time.delay(5000) #miliseconds
# screen.fill(mag)
# p.display.update()
# p.time.delay(5000) #miliseconds

#define rectangle
x=20
y=30

#w and h of rectangale
wbox=50
hbox=50
square=p.Rect(x,y,wbox,hbox)
square2=p.Rect(x+200, y+200, wbox, hbox)
#++ to x goes right and y goes down; -- to x goes left and y goes up

#window stays open until closed by user
run=True
while run:
    screen.fill(mag)
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False
    square.x+=5
    square.y+=5
    p.draw.rect(screen,(white), square )
    p.draw.rect(screen,(red), square2 )
    p.display.update()
    p.time.delay (300)