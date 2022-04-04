#Katie

from email.mime import image
import os, random, math,datetime
import pygame as p
os.system('cls')

#intailize p
p.init()

#MENU VARIABLES
WIDTH=700
HEIGHT=700
#screen
screen=p.display.set_mode((WIDTH,HEIGHT))
p.display.set_caption("Final Project")

bg=p.image.load('Class Stuff\images\\bi mountain.jpg')
character=p.image.load("Class Stuff\images\Pygame-Tutorials-master\Game\standing.png")
screen.blit(bg,(0,0))
screen.blit(character,(300,300))
p.display.update()
p.time.delay(300)
x=300
y=300
move= 5
check=True
while check:
    screen.blit(bg,(0,0))
    for event in p.event.get():
        if event.type == p.QUIT:
            check = False
    keys=p.key.get_pressed()
    if keys[p.K_LEFT]:
        x -= move
    if keys[p.K_RIGHT]:
        x += move
    if keys[p.K_UP]:
        y-= move
    if keys[p.K_DOWN]:
        y+= move
    screen.blit(character,(x,y))
    p.display.update()
    p.time.delay(10)