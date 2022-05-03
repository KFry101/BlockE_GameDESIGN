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




#variables
run=True
move=5
jumpCount=10
left= False
right=False
walkCount=0
keycount=0
doorCount=0
x=30
y=418
key=False
doorSeq=False
Ending=False


 
 
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
medplat=p.transform.scale(medplat,(150,30))
longplat=p.image.load('FinalGame\images\longgrassplat.png')
longplat=p.transform.scale(longplat,(200,30))
key1=p.image.load('FinalGame\images\wKey1.gif') #   REPLACE WITH IMAGE LIST FOR MOVEMENt
key1=p.transform.scale(key1,(70,70))
key2=p.image.load('FinalGame\images\wKey2.gif')
key2=p.transform.scale(key2,(70,70))
key3=p.image.load('FinalGame\images\wKey3.gif')
key3=p.transform.scale(key3,(70,70))
key4=p.image.load('FinalGame\images\wKey4.gif')
key4=p.transform.scale(key4,(70,70))
key5=p.image.load('FinalGame\images\wKey5.gif')
key5=p.transform.scale(key5,(70,70))
key6=p.image.load('FinalGame\images\wKey6.gif')
key6=p.transform.scale(key6,(70,70))
key7=p.image.load('FinalGame\images\wKey7.gif')
key7=p.transform.scale(key7,(70,70))
key8=p.image.load('FinalGame\images\wKey8.gif')
key8=p.transform.scale(key8,(70,70))
key9=p.image.load('FinalGame\images\wKey9.gif')
key9=p.transform.scale(key9,(70,70))
key10=p.image.load('FinalGame\images\wKey10.gif')
key10=p.transform.scale(key10,(70,70))
key11=p.image.load('FinalGame\images\wKey11.gif')
key11=p.transform.scale(key11,(70,70))
key12=p.image.load('FinalGame\images\wKey12.gif')
key12=p.transform.scale(key12,(70,70))
keylist=[key1,key2, key3, key4,key5,key6,key7,key8,key9,key10,key11,key12]
clsdoor=p.image.load('FinalGame\images\door1.png')
openingdoor=[p.image.load('FinalGame\images\door1.png'),p.image.load('FinalGame\images\door2.png'),p.image.load('FinalGame\images\door3.png')]
darkness=p.image.load('FinalGame\images\doorBlack.png')
bg=forest
spr=chara

def doorPlat(dx,dy):
    global doorCount
    global Ending
    screen.blit(medplat,(dx,dy))
    xd=dx+medplat.get_width()/2-clsdoor.get_width()/2
    ds=1
    screen.blit(darkness, (xd,dy-clsdoor.get_height()+1))
    if doorCount + 1 >=12:
        ds=0
        doorCount=11
        p.time.delay(100)
        Ending=True
    if not doorSeq and not key:
        doorCount=0
        screen.blit(clsdoor,(xd,dy-clsdoor.get_height()))
    elif not doorSeq and key: 
        screen.blit(clsdoor,(xd,dy-clsdoor.get_height()))
    elif doorSeq and key:
        screen.blit(openingdoor[doorCount//4], (xd,dy-clsdoor.get_height()))
        ds=1
        doorCount+=ds
    
def keyPlat(px,py): 
    global keycount
    global xk
    screen.blit(longplat,(px,py))
    xk=px+longplat.get_width()/2-25
    if keycount + 1 >= 36:
        keycount=0
    if not key:
        screen.blit(keylist[keycount//3], (xk,py-70))
        keycount+=1

def drawWindow():
    global walkCount 
    global hitbox
    global plats1
    global plat
    global plat1, plat2, plat3, platd
    global xk
    #hidden collision items DRAWN
    #hitbox
    hitbox=p.Rect(x+14,y+14,36,50) #use hitbox for collisions
    p.draw.rect(screen,(0,0,0), hitbox) 
    #the platforms
    plats1=[]
    plat1 = p.Rect(WIDTH-560,HEIGHT-275, 150, 3)
    plat2=p.Rect(WIDTH-320, HEIGHT-390, 150,3)
    plat3=p.Rect(WIDTH-100, HEIGHT-500, 200, 3)
    platd=p.Rect(WIDTH-660,HEIGHT-420, 150, 3)
    ground=p.Rect(0, HEIGHT-150, WIDTH, 1)
    plats1.append(plat1)
    plats1.append(plat2)
    plats1.append(plat3)
    plats1.append(platd)
    plats1.append(ground)
    if bg==forest:
        for plat in plats1:
            p.draw.rect(screen,(255,0,0),plat)
    plats2=[]
    plats2.append(ground)
    if bg==frst2:
        for plat in plats2:
            p.draw.rect(screen,(255,0,0),plat)
        p.draw.rect(screen, (0,0,255), keybox)

    # background
    screen.blit(bg,(0,0))

   #actual graphics
    if bg==forest:
        #steping plats
        screen.blit(medplat,(WIDTH-560,HEIGHT-275))
        screen.blit(medplat,(WIDTH-320, HEIGHT-390))
        screen.blit(longplat,(WIDTH-100, HEIGHT-500))
        #door plat 
        doorPlat(WIDTH-660,HEIGHT-420)
    if bg==frst2:
        screen.blit(longplat,(-50, HEIGHT-500))
        #key plat
        keyPlat(WIDTH-450, HEIGHT-390)
# the character moveent  
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
    if Ending:
        p.time.wait(100)
        fscreen=p.Rect(0,0,WIDTH,HEIGHT)
        fade= 1
        if fade <=255:
           
            p.draw.rect(screen,(255,255,255, fade), fscreen) 
            fade=fade+1
            
    p.display.update()



while run:   
    clock.tick(27)
    #the collide variable
    
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
        if event.type==p.MOUSEBUTTONDOWN:
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

    if bg==forest: #screen with the door and
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
 #collision rules  
 #Items for the collision itselfdfsdgwrhryeh
    #hitbox
    hitbox=p.Rect(x+14,y+14,36,50)
    #platforms
    plats1=[]
    plat1 = p.Rect(WIDTH-560,HEIGHT-275, 150, 5)
    plat2=p.Rect(WIDTH-320, HEIGHT-390, 150,5)
    plat3=p.Rect(WIDTH-100, HEIGHT-500, 200, 5)
    platd=p.Rect(WIDTH-660,HEIGHT-420, 150, 5)
    ground=p.Rect(0, HEIGHT-150, WIDTH, 25)
    plats1.append(plat1)
    plats1.append(plat2)
    plats1.append(plat3)
    plats1.append(platd)
    plats1.append(ground)
    if bg==forest:
        for plat in plats1:
            collide=p.Rect.colliderect(hitbox, plat)
            if collide:
                y = plat.y-63
                acc=0
            dx=WIDTH-660
            wd=clsdoor.get_width()
            hd=clsdoor.get_height()
            xcd=dx+medplat.get_width()/2-clsdoor.get_width()/2
            doorbox=p.Rect(xcd,HEIGHT-420-hd, wd ,hd) #manually put dy
            collidedoor=p.Rect.colliderect(hitbox, doorbox)
            if collidedoor:
                doorSeq=True
            if not collidedoor:
                doorSeq=False
    plats2=[]
    plat4=p.Rect(-50, HEIGHT-500, 200, 5)
    plat5=p.Rect(WIDTH-450, HEIGHT-390, 200, 5)
    plats2.append(ground)
    plats2.append(plat4)
    plats2.append(plat5)
    if bg==frst2:
        for plat in plats2:
            collide=p.Rect.colliderect(hitbox, plat)
            if collide:
                y = plat.y-63
                acc=0
        px=WIDTH-450
        xck=px+longplat.get_width()/2
        keybox=p.Rect(xck, HEIGHT-440, 18, 32) #manually put py
        collidekey=p.Rect.colliderect(hitbox,keybox)
        if collidekey:
            key=True

    if not collide: #gravity
        acc+=1
        y+=acc

        


            
    

    
    drawWindow()




