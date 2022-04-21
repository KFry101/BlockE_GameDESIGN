#katie frymire
#the level one of the final gmae

import os, time, datetime, math 
import pygame as p
os.system('cls')

#intailize p
p.init()

#Constants
JUMP=False
MAX=10
WIDTH=700
HEIGHT=600
DEATH=False

#variables
check=True
move=5
jumpCount=10
left= False
right=False
walkCount=0
x=30
y=418
 
#screen
screen=p.display.set_mode((WIDTH,HEIGHT))
p.display.set_caption("Level 1")

#clock
clock = p.time.Clock()

#images
walkRight = [p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R1.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R2.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R3.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R4.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R5.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R6.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R7.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R8.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R9.png')]
walkLeft = [p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L1.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L2.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L3.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L4.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L5.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L6.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L7.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L8.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L9.png')]
rip=p.image.load('Class Stuff\images\pngegg.png')
rip=p.transform.scale(rip,(50,65))
chara=p.image.load("Class Stuff\images\Pygame-Tutorials-master\Game\standing.png")
forest=p.image.load('FinalGame\images\\forest.jpeg')
forest=p.transform.scale(forest,(700,600))
frst2=p.image.load('FinalGame\images\\forest.jpeg')
frst2=p.transform.scale(forest,(700,600))
medplat=p.image.load('FinalGame\images\\notaslonggrass.png')
longplat=p.image.load('FinalGame\images\longgrassplat.png')
bg=forest
spr=chara

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

while check:   
    clock.tick(27)
    for event in p.event.get():
        if event.type == p.QUIT:
            check = False
    if event.type ==p.MOUSEBUTTONDOWN:
            mouse_pos=p.mouse.get_pos()
            print(mouse_pos)
    #chara controls
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
    if bg==forest: #screen with the door
        if x>=WIDTH-50:
            bg=frst2
            x=-13
    if bg==frst2: #screen with the key
        if x<=-14:
            bg=forest
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
    drawWindow()




