#katie frymire
#the level one of the final gmae

import os, time, datetime, math
import pygame as p
os.system('cls')

#intailize p
p.init()

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
medplat=p.transform.scale(medplat,(150,30))
longplat=p.image.load('FinalGame\images\longgrassplat.png')
longplat=p.transform.scale(longplat,(200,30))
key=p.image.load('FinalGame\images\keywhitefl.gif') #   REPLACE WITH IMAGE LIST FOR MOVEMENT
key=p.transform.scale(key,(60,60))
clsdoor=p.image.load('FinalGame\images\clsdoor.png')
openingdoor=[p.image.load('FinalGame\images\clsdoor.png'),p.image.load('FinalGame\images\door2.png'),p.image.load('FinalGame\images\door3.png')]
bg=forest
spr=chara


#Constants

MAX=10
WIDTH=700
HEIGHT=600
GRAVITY=1
class Sprite():
    def __init__(self, image, px, py):
        self.image=image
        self.px=px
        self.py=py
    
class player(object):
    def __init__(self, x, y, wc, hc ):
        self.x = x
        self.y = y
        self.wc = wc
        self.hc = hc
        self.move = 5
        self.dy=0
        self.jumpCount= 10
        self.left= False
        self.right= False
        self.walkCount= 0
        self.jump=False
        self.hitbox = (self.x+14, self.y+14, 36, 50 )

    def move(self):
        self.x+= self.move
        self.y+= self.dy
        self.dy+=GRAVITY 
    
    def is_aabb_collision(self, other):
        # Axis Aligned Bounding Box
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return (x_collision and y_collision)
        
    
    
    def draw(self, screen):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            screen.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            screen.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
        else:
            screen.blit(spr, (self.x,self.y))

        self.hitbox = (self.x+14, self.y+14, 36, 50 )
        p.draw.rect(screen, (0,0,0), self.hitbox,2)
    

##########################################################################
#screen
screen=p.display.set_mode((WIDTH,HEIGHT))
p.display.set_caption("Level 1")

def keyPlat(px,py): 
    screen.blit(longplat,(px,py))
    xk=px+longplat.get_width()/2-25
    screen.blit(key,(xk,py-50))

def doorPlat(dx,dy):
    screen.blit(medplat,(dx,dy))
    xd=dx+medplat.get_width()/2-clsdoor.get_width()/2
    screen.blit(clsdoor,(xd,dy-clsdoor.get_height()))

def drawWindow():
    screen.blit(bg,(0,0))
    man.draw(screen)
   #actual graphics
    if bg==forest:
        #steping plats 
        screen.blit(medplat,(WIDTH-560,HEIGHT-275))
        screen.blit(medplat,(WIDTH-320, HEIGHT-390))
        screen.blit(longplat,(WIDTH-100, HEIGHT-500))
        #door plat 
        doorPlat(WIDTH-660,HEIGHT-440)
    if bg==frst2:
        screen.blit(longplat,(WIDTH-750, HEIGHT-500))
        #key plat
        keyPlat(WIDTH-450, HEIGHT-390)
    
    p.display.update()

#main loop
man= player(30, 418, 64, 64)
plats1=[]
plats1.append(Sprite(medplat, WIDTH-560,HEIGHT-275 ))
plats1.append(Sprite(medplat,WIDTH-320, HEIGHT-390))
plats1.append(Sprite(longplat,WIDTH-100, HEIGHT-500))
plats2=[]
run=True
while run:   
    clock.tick(27)
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
        if event.type==p.MOUSEBUTTONDOWN:
            mouse_pos=p.mouse.get_pos()
            print(mouse_pos)
    #chara controls
    keys=p.key.get_pressed()
    if keys[p.K_LEFT] and man.x >=-14:
        man.x -= man.move
        man.left=True
        man.right=False
    elif keys[p.K_RIGHT] and man.x<= WIDTH-50:
        man.x += man.move
        man.right=True
        man.left=False
    else:
        man.left=False
        man.right=False
        man.walkCount=0
    if bg==forest: #screen with the door and
        if man.x>=WIDTH-50:
            bg=frst2
            man.x=-13
        #this screen's platforms
   
    if bg==frst2: #screen with the key
        if man.x<=-14:
            bg=forest
            man.x=WIDTH-50 
    
    if not (man.jump):
        if keys[p.K_SPACE] or keys[p.K_UP]:
            man.jump=True
    else:
        if man.jumpCount>=-MAX:
            man.y-= man.jumpCount*abs(man.jumpCount)/2
            man.jumpCount-=1
        else:
            man.jumpCount=MAX
            man.jump=False

    
    drawWindow()




