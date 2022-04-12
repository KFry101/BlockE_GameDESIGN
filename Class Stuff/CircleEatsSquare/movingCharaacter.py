#Katie Frymire
#4/5/22

import os, random, math,datetime
import pygame as p
os.system('cls')

#intailize p
p.init()

#Constants
JUMP=False
MAX=10
WIDTH=700
HEIGHT=700

#screen
screen=p.display.set_mode((WIDTH,HEIGHT))
p.display.set_caption("Final Project")

#characters and images
walkRight = [p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R1.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R2.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R3.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R4.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R5.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R6.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R7.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R8.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R9.png')]
walkLeft = [p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L1.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L2.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L3.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L4.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L5.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L6.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L7.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L8.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L9.png')]
biM=p.image.load('Class Stuff\images\\bi mountain.jpg')
brW=p.image.load('Class Stuff\images\\broke window.jpg')
rip=p.image.load('Class Stuff\images\Gravestone.png')
rip=p.transform.scale(rip,(64,64))
chara=p.image.load("Class Stuff\images\Pygame-Tutorials-master\Game\standing.png")

#clock
clock = p.time.Clock()

#Variables
x=30
y=636
wc=64
hc=64
move= 5
check=True
jumpCount=10
left= False
right=False
walkCount=0

def drawWindow():
    global walkCount
    screen.blit(biM,(0,0))
    if walkCount + 1 >= 27:
         walkCount = 0
    if left:
        screen.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        screen.blit(walkRight[walkCount//3], (x,y))
        walkCount +=1
    else:
        screen.blit(chara, (x,y))
    p.display.update()

#main loop
while check:
    clock.tick(27)
    for event in p.event.get():
        if event.type == p.QUIT:
            check = False
    keys=p.key.get_pressed()
    if keys[p.K_LEFT] and x >=-14:
        x -= move
        left=True
        right=False
    elif keys[p.K_RIGHT] and x<= WIDTH-50:
        x += move
        right=True
        left=False
    else:
        left=False
        right=False
        walkCount=0
    if not JUMP:
        if keys[p.K_SPACE] or keys[p.K_UP]:
            JUMP=True
    else:
        if jumpCount>=-MAX:
            y -= jumpCount*abs(jumpCount)/2
            jumpCount-=1
        else:
            jumpCount=MAX
            JUMP=False

    drawWindow()

p.quit()
