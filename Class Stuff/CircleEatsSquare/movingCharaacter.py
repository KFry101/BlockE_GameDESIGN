#Katie Frymire
#4/5/22

import os, random, math,datetime, time
import pygame as p
os.system('cls')

#intailize p
p.init()

#Constants
JUMP=False
MAX=12
WIDTH=700
HEIGHT=700
DEATH=False

#screen
screen=p.display.set_mode((WIDTH,HEIGHT))
p.display.set_caption("Final Project")

#characters and images
walkRight = [p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R1.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R2.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R3.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R4.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R5.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R6.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R7.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R8.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R9.png')]
walkLeft = [p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L1.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L2.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L3.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L4.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L5.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L6.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L7.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L8.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L9.png')]
biM=p.image.load('Class Stuff\images\\bi mountain.jpg')
brW=p.image.load('Class Stuff\images\\broke window.jpg')
rip=p.image.load('Class Stuff\images\pngegg.png')
rip=p.transform.scale(rip,(50,65))
chara=p.image.load("Class Stuff\images\Pygame-Tutorials-master\Game\standing.png")
bg=biM
spr=chara

#clock
clock = p.time.Clock()

#Variables
x=30
y=636
wc=64
hc=64
move= 5
check=True
jumpCount=12
left= False
right=False
walkCount=0

def drawWindow():
    global walkCount
    screen.blit(bg,(0,0))
    if walkCount + 1 >= 27:
         walkCount = 0
    if left:
        screen.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        screen.blit(walkRight[walkCount//3], (x,y))
        walkCount +=1
    else:
        screen.blit(spr, (x,y))

    p.display.update()

#main loop
while check:
    clock.tick(27)
    #basic death slow fall
    if DEATH:
        clock.tick(24)
        screen.blit(chara,(x+14,y))
        JUMP=False
        if y<636:
            y+=7
        elif y>=636:
            spr=rip
        if spr==rip and keys[p.K_LEFT] or keys[p.K_RIGHT]:
            spr=chara
            x=-14
            y=636
            jumpCount=12
            MAX=12
            DEATH=False
            JUMP=False
        
            
   #chara controls
    for event in p.event.get():
        if event.type == p.QUIT:
            check = False
        if event.type ==p.MOUSEBUTTONDOWN:
            mouse_pos=p.mouse.get_pos()
            print(mouse_pos)
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
    if bg==biM:
        if x>=WIDTH-50:
            bg=brW
            x=-13
            y=636
    if bg==brW:
        if x<=-14:
            bg=biM
            x=WIDTH-50
    
    if not JUMP:
        if keys[p.K_SPACE] or keys[p.K_UP]:
            JUMP=True
    else:
        if jumpCount>=-MAX:
            y-= jumpCount*abs(jumpCount)/2
            jumpCount-=1
        else:
            jumpCount=MAX
            JUMP=False
    
    if JUMP and not DEATH:
        if bg==biM:
            if x>=436  and x<=570 and y>=370 and y<=410:
                DEATH=True
                
    drawWindow()

p.quit()
