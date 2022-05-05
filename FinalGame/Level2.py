#katie frymire
#the level 2 of the final gmae


import os, time, datetime, math
import pygame as p
os.system('cls')

#intailize p
p.init()

p.font.init()
#this font is from https://www.fontspace.com/a-goblin-appears-font-f30019
#made by Chequered Ink
popup = p.font.Font("FinalGame\Fonts\AGoblinAppears-o2aV.ttf",12)

#Constants
JUMP=False
MAX=10
WIDTH=700
HEIGHT=600
DEATH=False



#variables
run=True
move=5
deathcount=0
jumpCount=10
left= False
right=False
walkCount=0
keycount=0
doorCount=0
x=WIDTH*.0028
y=HEIGHT*.845
key=False
doorSeq=False
Ending=False
LOCK=False

 
 
#screen
screen=p.display.set_mode((WIDTH,HEIGHT))
p.display.set_caption("Level 2")


#clock
clock = p.time.Clock()

#images
walkRight = [p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R1.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R2.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R3.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R4.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R5.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R6.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R7.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R8.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R9.png')]
walkLeft = [p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L1.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L2.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L3.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L4.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L5.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L6.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L7.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L8.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L9.png')]
rip=p.image.load('Class Stuff\images\pngegg.png')
rip=p.transform.scale(rip,(50,65))
chara=p.image.load("Class Stuff\images\Pygame-Tutorials-master\Game\standing.png")
cave=p.image.load('FinalGame\images\cave.png')
cave=p.transform.scale(cave,(700,600))
cve2=p.image.load('FinalGame\images\cave.png')
cve2=p.transform.scale(cve2,(700,600))
smlPlat=p.image.load("FinalGame\images\cubecave.png")
smlPlat=p.transform.scale(smlPlat,(50,35))
medplat=p.image.load('FinalGame\images\mediumcaveplat.png')
medplat=p.transform.scale(medplat,(150,30))
longplat=p.image.load('FinalGame\images\longcaveplat.png')
longplat=p.transform.scale(longplat,(200,30))
key1=p.image.load('FinalGame\images\\bKey1.gif') #   REPLACE WITH IMAGE LIST FOR MOVEMENt
key1=p.transform.scale(key1,(70,70))
key2=p.image.load('FinalGame\images\\bKey2.gif')
key2=p.transform.scale(key2,(70,70))
key3=p.image.load('FinalGame\images\\bKey3.gif')
key3=p.transform.scale(key3,(70,70))
key4=p.image.load('FinalGame\images\\bKey4.gif')
key4=p.transform.scale(key4,(70,70))
key5=p.image.load('FinalGame\images\\bKey5.gif')
key5=p.transform.scale(key5,(70,70))
key6=p.image.load('FinalGame\images\\bKey6.gif')
key6=p.transform.scale(key6,(70,70))
key7=p.image.load('FinalGame\images\\bKey7.gif')
key7=p.transform.scale(key7,(70,70))
key8=p.image.load('FinalGame\images\\bKey8.gif')
key8=p.transform.scale(key8,(70,70))
key9=p.image.load('FinalGame\images\\bKey9.gif')
key9=p.transform.scale(key9,(70,70))
key10=p.image.load('FinalGame\images\\bKey10.gif')
key10=p.transform.scale(key10,(70,70))
key11=p.image.load('FinalGame\images\\bKey11.gif')
key11=p.transform.scale(key11,(70,70))
key12=p.image.load('FinalGame\images\\bKey12.gif')
key12=p.transform.scale(key12,(70,70))
keylist=[key1,key2, key3, key4,key5,key6,key7,key8,key9,key10,key11,key12]
clsdoor=p.image.load('FinalGame\images\door1.png')
openingdoor=[p.image.load('FinalGame\images\door1.png'),p.image.load('FinalGame\images\door2.png'),p.image.load('FinalGame\images\door3.png')]
darkness=p.image.load('FinalGame\images\doorBlack.png')
spikes=p.image.load("FinalGame\images\cavespike.png")
spikes=p.transform.scale(spikes, (75, 30))
tallSpike=p.transform.scale(spikes,(100,75))
dspikes=p.transform.flip(spikes,False,True)
#CHANGING IMAGE VARIABLES
bg=cave
spr=chara

def doorPlat(dx,dy):
    global doorCount
    global Ending
    global LOCK

    screen.blit(medplat,(dx,dy))
    xd=dx+medplat.get_width()/2-clsdoor.get_width()/2
    ds=1
    screen.blit(clsdoor,(xd,dy-clsdoor.get_height()))
    if doorCount + 1 >=12:
        ds=0
        doorCount=11
    if not doorSeq and not key:
        screen.blit(clsdoor,(xd,dy-clsdoor.get_height()))
    elif not doorSeq and key: 
        screen.blit(clsdoor,(xd,dy-clsdoor.get_height()))
    elif collidedoor and not key: 
        LOCK=True
    elif doorSeq and key:
        screen.blit(darkness, (xd,dy-clsdoor.get_height()+1))
        screen.blit(openingdoor[doorCount//4], (xd,dy-clsdoor.get_height()))
        ds=1
        doorCount+=ds
    
def keyPlat(px,py): 
    global keycount
    global xk
    screen.blit(medplat,(px,py))
    xk=px+medplat.get_width()/2-25
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
    global LOCK
    #hidden collision items DRAWN
    #hitbox
    hitbox=p.Rect(x+14,y+14,36,50) #use hitbox for collisions
    p.draw.rect(screen,(0,0,255), hitbox) 
    #the platforms
    plats1=[]
    plat1 = p.Rect(WIDTH-560,HEIGHT-275, 150, 3)
    plat2=p.Rect(WIDTH-320, HEIGHT-390, 150,3)
    plat3=p.Rect(WIDTH-100, HEIGHT-500, 200, 3)
    platd=p.Rect(WIDTH-660,HEIGHT-420, 150, 3)
    ground=p.Rect(0, HEIGHT-30, WIDTH, 1)
    plats1.append(plat1)
    plats1.append(plat2)
    plats1.append(plat3)
    plats1.append(platd)
    plats1.append(ground)
    if bg==cave:
        for plat in plats1:
            p.draw.rect(screen,(255,0,0),plat)
    plats2=[]
    plats2.append(ground)
    if bg==cve2:
        for plat in plats2:
            p.draw.rect(screen,(255,0,0),plat)
        p.draw.rect(screen, (0,0,255), keybox)
        spike2=p.Rect(WIDTH*.1, HEIGHT*.825, 200,75)
        spike3=p.Rect(WIDTH*.61, HEIGHT*.825, 200,75)
        p.draw.rect(screen, (0,0,100), spike2)
        

    # background
    screen.blit(bg,(0,0))
   #actual graphics
    if bg==cave:
        #steping plats
        # screen.blit(medplat,(WIDTH-560,HEIGHT-275))
        screen.blit(medplat,((WIDTH/3)-medplat.get_width(), HEIGHT*0.5))
        screen.blit(smlPlat,(WIDTH*0.542, HEIGHT*.35))
        screen.blit(smlPlat,((WIDTH/2)-smlPlat.get_width(),HEIGHT*0.69))
        screen.blit(longplat,((WIDTH*0.8), HEIGHT*0.225 ))
        screen.blit(tallSpike,(WIDTH*.68, HEIGHT*.825))
        screen.blit(tallSpike,((WIDTH*.68)+100, HEIGHT*.825))
        #door plat 
        doorPlat(WIDTH-660,HEIGHT-420)
        
    if bg==cve2:
        screen.blit(longplat,(-50, HEIGHT*0.225))
        screen.blit(medplat,(WIDTH*.365, HEIGHT*.028))
        screen.blit(dspikes,(WIDTH*.365, (HEIGHT*0.028)+30))
        screen.blit(dspikes,((WIDTH*.365)+75, (HEIGHT*0.028)+30))
        screen.blit(medplat,(WIDTH*.398, HEIGHT*.625))
        screen.blit(smlPlat,(WIDTH*0.244, HEIGHT*.458))
        screen.blit(tallSpike,(WIDTH*.1, HEIGHT*.825))
        screen.blit(tallSpike,((WIDTH*.1)+100, HEIGHT*.825))
        screen.blit(tallSpike,(WIDTH*.61, HEIGHT*.825))
        screen.blit(tallSpike,((WIDTH*.61)+100, HEIGHT*.825))
        #key plat
        keyPlat(WIDTH*.75, HEIGHT*0.42)
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
    if LOCK:
        PopUpM("It appears to be locked")  
        LOCK=False    
    p.display.update()

def PopUpM(message):
    txt=popup.render(message, 1, (255, 255, 255))
    #get width of the text
    #x value = WIDTH/2 - wtext
    xt= WIDTH/2-txt.get_width()/2
    screen.blit(txt,(xt,HEIGHT*.016))


while run:   
    clock.tick(27)
    #the collide variable
    if DEATH:
        clock.tick(24)
        screen.blit(chara,(x+14,y))
        JUMP=False #NEED TO BE ADJUST FOR NEW STUFF
        if not collide:
            acc=0
            acc+=0
            y+=1
        if p.Rect.colliderect(hitbox, plat):
            spr=rip
        if spr==rip and (keys[p.K_LEFT] or keys[p.K_RIGHT]):
            deathcount+=1
            bg=cave
            spr=chara
            x=WIDTH*0.0428
            y=HEIGHT*.845
            jumpCount=10
            MAX=10
            DEATH=False
            JUMP=False
        
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
        if event.type==p.MOUSEBUTTONDOWN:
            mouse_pos=p.mouse.get_pos()
            print(mouse_pos)
        # if event.type ==  p.K_LSHIFT:
        #     move=5
        if event.type == p.K_LSHIFT:
            move=10
    keys=p.key.get_pressed()  
       
    #chara controls
    if keys[p.K_LSHIFT]:
        move=10
    else:
        move=5
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

    if bg==cave: #screen with the door and
        if x>=WIDTH-50:
            bg=cve2
            x=-13

    if bg==cve2: #screen with the key
        if x<=-14:
            bg=cave
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
    plat1 = p.Rect((WIDTH/2)-smlPlat.get_width(),HEIGHT*0.69, 30, 5)
    plat2=p.Rect((WIDTH/3)-medplat.get_width(), HEIGHT*0.5, 150,5)
    plat3=p.Rect(WIDTH*0.542, HEIGHT*.35, 30, 5)
    plat0=p.Rect((WIDTH*0.8), HEIGHT*0.225, 200,5)
    platd=p.Rect(WIDTH-660,HEIGHT-420, 150, 5)
    ground=p.Rect(0, HEIGHT-30, WIDTH, 25)
    plats1.append(plat1)
    plats1.append(plat2)
    plats1.append(plat3)
    plats1.append(plat0)
    plats1.append(platd)
    plats1.append(ground)
    Spikes1=[] #############################################################################################
    spike1=p.Rect(WIDTH*.68, HEIGHT*.825, 200,75)
    Spikes1.append(spike1)
    if bg==cave:
        for spike in Spikes1:
            collidespike=p.Rect.colliderect(hitbox, spike)
            if collidespike:
                DEATH=True
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
    plat4=p.Rect(-50, HEIGHT*0.225, 200, 5)
    plat5=p.Rect(WIDTH*.365, HEIGHT*.028, 150, 5)
    plat6=p.Rect(WIDTH*.397, HEIGHT*.625, 150, 20)
    plat7=p.Rect(WIDTH*0.244, HEIGHT*.458, 30, 5)
    platk=p.Rect(WIDTH*.76, HEIGHT*0.42, 150, 5)
    plats2.append(ground)
    plats2.append(plat4)
    plats2.append(plat5)
    plats2.append(plat6)
    plats2.append(plat7)
    plats2.append(platk)
    Spikes2=[]
    spike2=p.Rect(WIDTH*.1, HEIGHT*.825, 200,75)
    spike3=p.Rect(WIDTH*.61, HEIGHT*.825, 200,75)
    Spikes2.append(spike2)
    Spikes2.append(spike3)
    if bg==cve2:
        for plat in plats2:
            collide=p.Rect.colliderect(hitbox, plat)
            if collide:
                y = plat.y-63
                acc=0
            for spike in Spikes2:
                collidespike=p.Rect.colliderect(hitbox, spike)
                if collidespike:
                    DEATH=True
        px=WIDTH*.75
        xck=px+medplat.get_width()/2
        keybox=p.Rect(xck,(HEIGHT*0.375)-50, 18, 32) #manually put py
        collidekey=p.Rect.colliderect(hitbox,keybox)
        if collidekey:
            key=True

    if not collide: #gravity
        acc+=1
        y+=acc

    
    drawWindow()