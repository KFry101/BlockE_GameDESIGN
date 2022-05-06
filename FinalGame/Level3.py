#katie frymire
#the level 3 of the final gmae


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

#screen
screen=p.display.set_mode((WIDTH,HEIGHT))
p.display.set_caption("Level 3")

#clock
clock = p.time.Clock()

#images
walkRight = [p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R1.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R2.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R3.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R4.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R5.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R6.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R7.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R8.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\R9.png')]
walkLeft = [p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L1.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L2.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L3.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L4.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L5.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L6.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L7.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L8.png'), p.image.load('Class Stuff\images\Pygame-Tutorials-master\Game\L9.png')]
rip=p.image.load('Class Stuff\images\pngegg.png')
rip=p.transform.scale(rip,(50,65))
chara=p.image.load("Class Stuff\images\Pygame-Tutorials-master\Game\standing.png")
castle=p.image.load('FinalGame\images\castle.webp')
castle=p.transform.scale(castle,(700,600))
cstle2=p.image.load('FinalGame\images\castle.webp')
cstle2=p.transform.scale(cstle2,(700,600))
cstle2=p.transform.flip(cstle2,True, False)
cstle0=p.image.load('FinalGame\images\castle.webp')
cstle0=p.transform.scale(cstle0,(700,600))
cstle0=p.transform.flip(cstle0,True, False)
smlPlat=p.image.load("FinalGame\images\cubecastle.png")
smlPlat=p.transform.scale(smlPlat,(75,35))
medplat=p.image.load('FinalGame\images\mediumcastle.png')
medplat=p.transform.scale(medplat,(150,30))
longplat=p.image.load('FinalGame\images\longcastle.png')
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
wkey1=p.image.load('FinalGame\images\wkey1.gif') #   REPLACE WITH IMAGE LIST FOR MOVEMENt
wkey1=p.transform.scale(wkey1,(70,70))
wkey2=p.image.load('FinalGame\images\wkey2.gif')
wkey2=p.transform.scale(wkey2,(70,70))
wkey3=p.image.load('FinalGame\images\wkey3.gif')
wkey3=p.transform.scale(wkey3,(70,70))
wkey4=p.image.load('FinalGame\images\wkey4.gif')
wkey4=p.transform.scale(wkey4,(70,70))
wkey5=p.image.load('FinalGame\images\wkey5.gif')
wkey5=p.transform.scale(wkey5,(70,70))
wkey6=p.image.load('FinalGame\images\wkey6.gif')
wkey6=p.transform.scale(wkey6,(70,70))
wkey7=p.image.load('FinalGame\images\wkey7.gif')
wkey7=p.transform.scale(wkey7,(70,70))
wkey8=p.image.load('FinalGame\images\wkey8.gif')
wkey8=p.transform.scale(wkey8,(70,70))
wkey9=p.image.load('FinalGame\images\wkey9.gif')
wkey9=p.transform.scale(wkey9,(70,70))
wkey10=p.image.load('FinalGame\images\wkey10.gif')
wkey10=p.transform.scale(wkey10,(70,70))
wkey11=p.image.load('FinalGame\images\wkey11.gif')
wkey11=p.transform.scale(wkey11,(70,70))
wkey12=p.image.load('FinalGame\images\wkey12.gif')
wkey12=p.transform.scale(wkey12,(70,70))
wkeylist=[wkey1,wkey2, wkey3, wkey4,wkey5,wkey6,wkey7,wkey8,wkey9,wkey10,wkey11,wkey12]
clsdoor=p.image.load('FinalGame\images\dbldoor.png')
openingdoor=[p.image.load('FinalGame\images\dbldoor.png'),p.image.load('FinalGame\images\dbldoor2.png'),p.image.load('FinalGame\images\dbldoor3.png')]
darkness=p.image.load('FinalGame\images\dbldoorBlack.png')
spikes=p.image.load("FinalGame\images\spikes.png")
spikes=p.transform.scale(spikes, (75, 30))
tallSpike=p.transform.scale(spikes,(100,90))
dspikes=p.transform.flip(spikes,False,True)
#CHANGING IMAGE VARIABLES
bg=castle
spr=chara

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
x=(WIDTH/2)-(spr.get_width()/2)
y=HEIGHT*.6783
key=False
keyw2=False
doorSeq=False
Ending=False
LOCK=False
ANOTHER=False
 
def doorPlat(dx,dy):
    global doorCount
    global Ending
    global LOCK

    screen.blit(longplat,(dx,dy))
    xd=dx+longplat.get_width()/2-clsdoor.get_width()/2
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
        ANOTHER=True
    elif doorSeq and key and keyw2:
        screen.blit(darkness, (xd,dy-clsdoor.get_height()+1))
        screen.blit(openingdoor[doorCount//4], (xd,dy-clsdoor.get_height()))
        ds=1
        doorCount+=ds

def wKeyPlat(px,py): 
    global keycount
    global xk
    screen.blit(smlPlat,(px,py))
    xk=px+(smlPlat.get_width()*.05)
    if keycount + 1 >= 36:
        keycount=0
    if not key:
        screen.blit(wkeylist[keycount//3], (xk,py-70))
        keycount+=1  
   
def bKeyPlat(px,py): 
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
    global ground
    global hitbox
    global plats1
    global plats0
    global plat
    global plat1, plat2, plat3, platd
    global xk
    global LOCK
    global ANOTHER
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
    ground=p.Rect(0, HEIGHT*0.783, WIDTH, 1)
    plats1.append(plat1)
    plats1.append(plat2)
    plats1.append(plat3)
    plats1.append(platd)
    plats1.append(ground)
    if bg==castle:
        for plat in plats1:
            p.draw.rect(screen,(255,0,0),plat)
    plats2=[]
    plats2.append(ground)
    if bg==cstle2:
        for plat in plats2:
            p.draw.rect(screen,(255,0,0),plat)
        p.draw.rect(screen, (0,0,255), keybox)
        spike2=p.Rect(WIDTH*.1, HEIGHT*.825, 200,75)
        p.draw.rect(screen, (0,0,100), spike2)
        

    #background
    screen.blit(bg,(0,0))
   #actual graphics
    if bg==cstle0:
        #ground
        screen.blit(tallSpike,((0), (HEIGHT*0.785)-tallSpike.get_height()))
        screen.blit(spikes,((tallSpike.get_width()), (HEIGHT*0.785)-spikes.get_height()))
        screen.blit(spikes,((tallSpike.get_width()+spikes.get_width()), (HEIGHT*0.783)-spikes.get_height()))
        screen.blit(spikes,((tallSpike.get_width()+spikes.get_width()*2), (HEIGHT*0.783)-spikes.get_height()))
        screen.blit(spikes,((tallSpike.get_width()+spikes.get_width()*3), (HEIGHT*0.783)-spikes.get_height()))
        screen.blit(spikes,((tallSpike.get_width()+spikes.get_width()*4), (HEIGHT*0.783)-spikes.get_height()))
        screen.blit(spikes,((tallSpike.get_width()+spikes.get_width()*5), (HEIGHT*0.783)-spikes.get_height()))
        screen.blit(spikes,((tallSpike.get_width()+spikes.get_width()*6), (HEIGHT*0.783)-spikes.get_height()))
        screen.blit(spikes,((tallSpike.get_width()+spikes.get_width()*7), (HEIGHT*0.783)-spikes.get_height()))
        #plats
        screen.blit(medplat,(WIDTH*0.77, HEIGHT*.55))
        screen.blit(medplat,((WIDTH*.35), HEIGHT*.618))
        screen.blit(smlPlat,((WIDTH*.134), HEIGHT*.4))
        screen.blit(dspikes,(WIDTH*.134, (HEIGHT*0.4)+30))
        screen.blit(smlPlat,((WIDTH*.35), HEIGHT*.2))
        screen.blit(dspikes,(WIDTH*.35, (HEIGHT*0.2)+30))
        screen.blit(smlPlat,((WIDTH*.57), HEIGHT*.07))
        screen.blit(dspikes,(WIDTH*.57, (HEIGHT*0.07)+30))
        #key 
        wKeyPlat(WIDTH*.77, HEIGHT*.083)
        screen.blit(dspikes,(WIDTH*.77, (HEIGHT*0.083)+30))
    if bg==castle:
        # screen.blit(medplat,(WIDTH-560,HEIGHT-275))
        screen.blit(smlPlat,((WIDTH*.3)-25, HEIGHT*.605))
        screen.blit(smlPlat,((WIDTH*.6)+25, HEIGHT*.605))
        screen.blit(medplat,((WIDTH*.03), HEIGHT*.4))
        screen.blit(dspikes,(WIDTH*.035, (HEIGHT*0.4)+30))
        screen.blit(dspikes,((WIDTH*.035)+dspikes.get_width(), (HEIGHT*0.4)+30))
        screen.blit(medplat,((WIDTH*.74), HEIGHT*.4))
        screen.blit(dspikes,(WIDTH*.74, (HEIGHT*0.4)+30))
        screen.blit(dspikes,((WIDTH*.74)+75, (HEIGHT*0.4)+30))
        screen.blit(tallSpike,(0, (HEIGHT*0.785)-tallSpike.get_height()))
        screen.blit(tallSpike,((WIDTH-tallSpike.get_width()), (HEIGHT*0.785)-tallSpike.get_height()))
        
        #door plat 
        doorPlat((WIDTH/2)-(longplat.get_width()/2), HEIGHT*0.23)
        screen.blit(dspikes,((WIDTH*.501)-(longplat.get_width()/2), (HEIGHT*0.23)+30))
        screen.blit(dspikes,((WIDTH*.501)-(longplat.get_width()/2)+dspikes.get_width(), (HEIGHT*0.23)+30))
        screen.blit(dspikes,((WIDTH*.501)-(longplat.get_width()/2)+(dspikes.get_width()*1.6), (HEIGHT*0.23)+30))
        
    if bg==cstle2:
        screen.blit(medplat,(WIDTH*.398, HEIGHT*.625))
        screen.blit(medplat,(WIDTH*0.11, HEIGHT*.5))
        screen.blit(smlPlat,((WIDTH*.44), HEIGHT*.35))
        screen.blit(medplat,((WIDTH*.23), HEIGHT*.155))
        screen.blit(dspikes,((WIDTH*.23), (HEIGHT*0.155)+30))
        screen.blit(dspikes,((WIDTH*.23)+dspikes.get_width(), (HEIGHT*0.155)+30))
        screen.blit(tallSpike,(WIDTH*.1, (HEIGHT*0.785)-tallSpike.get_height()))
        screen.blit(tallSpike,((WIDTH*.1)+100,(HEIGHT*0.785)-tallSpike.get_height()))
        screen.blit(tallSpike,(WIDTH*.61, (HEIGHT*0.785)-tallSpike.get_height()))
        screen.blit(tallSpike,((WIDTH*.61)+100, (HEIGHT*0.785)-tallSpike.get_height()))
        #key plat
        bKeyPlat(WIDTH*.65, HEIGHT*0.1)
        screen.blit(dspikes,((WIDTH*.65), (HEIGHT*0.1)+30))
        screen.blit(dspikes,((WIDTH*.65)+dspikes.get_width(), (HEIGHT*0.1)+30))
        
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
    if ANOTHER:
        PopUpM("There's another lock. You need another key")
        ANOTHER=False
    p.display.update()

def PopUpM(message):
    txt=popup.render(message, 1, (255, 255, 255))
    #get width of the text
    #x value = WIDTH/2 - wtext
    xt= WIDTH/2-txt.get_width()/2
    screen.blit(txt,(xt,HEIGHT*.016))

while run:   
    global plat
    clock.tick(27)
    if DEATH:
        clock.tick(24)
        JUMP=False #NEED TO BE ADJUST FOR NEW STUFF
        if not collide:
            acc=0
            acc+=0
            y+=1
        if p.Rect.colliderect(hitbox, plat) or collide:
            spr=rip    
        if spr==rip and (keys[p.K_LEFT] or keys[p.K_RIGHT]):
            deathcount+=1
            bg=castle
            spr=chara
            x=(WIDTH/2)
            y=HEIGHT*.6783
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
    if bg==cstle0:
            if x>=WIDTH-50:
                bg=castle
                x=-13
    if bg==castle: #screen with the door and
        if x>=WIDTH-50:
            bg=cstle2
            x=-13
        if x<=-14:
            bg=cstle0
            x=WIDTH-50
    if bg==cstle2: 
        if x<=-14:
            bg=castle
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
   
        # screen.blit(dspikes,((WIDTH*.501)-(longplat.get_width()/2), (HEIGHT*0.23)+30))
        # screen.blit(dspikes,((WIDTH*.501)-(longplat.get_width()/2)+dspikes.get_width(), (HEIGHT*0.23)+30))
        # screen.blit(dspikes,((WIDTH*.501)-(longplat.get_width()/2)+(dspikes.get_width()*1.6), (HEIGHT*0.23)+30))
    plats1=[]
    plat1=p.Rect((WIDTH*.3)-25, HEIGHT*.605, 75, 5)
    plat2=p.Rect((WIDTH*.6)+25, HEIGHT*.605, 75, 5)
    plat3=p.Rect((WIDTH*.74), HEIGHT*.4, 150, 5)
    plat4=p.Rect(WIDTH*.03, HEIGHT*.4, 150, 5)
    platd=p.Rect((WIDTH/2)-100, HEIGHT*0.23, 200, 5)
    ground=p.Rect(0, HEIGHT*0.783, WIDTH, 50)
    plats1.append(platd)
    plats1.append(plat1)
    plats1.append(plat2)
    plats1.append(plat3)
    plats1.append(plat4)
    plats1.append(ground)
    Spikes1=[] #############################################################################################
    spike1=p.Rect(0, (HEIGHT*0.783)-tallSpike.get_height(), 100,75)
    spike2=p.Rect(WIDTH-tallSpike.get_width(), (HEIGHT*0.785)-tallSpike.get_height(), 100,75)
    spike3=p.Rect((WIDTH*.74)+75, (HEIGHT*0.4)+30, 75,30)
    spike4=p.Rect((WIDTH*.035)+dspikes.get_width(), (HEIGHT*0.4)+30, 75,30)
    spike5=p.Rect(WIDTH*.74, (HEIGHT*0.4)+30, 75,30)
    spike6=p.Rect((WIDTH*.74)+75, (HEIGHT*0.4)+30, 75,30)
    Spikes1.append(spike1)
    Spikes1.append(spike2)
    Spikes1.append(spike3) 
    Spikes1.append(spike4) 
    Spikes1.append(spike5)
    Spikes1.append(spike6) 
    if bg==castle:
        for plat in plats1:
            collide=p.Rect.colliderect(hitbox, plat)
            if collide:
                y = plat.y-63
                acc=0
            for spike in Spikes1:
                collidespike=p.Rect.colliderect(hitbox, spike)
                if collidespike:
                    DEATH=True
            dx=(WIDTH/2)-100
            wd=clsdoor.get_width()
            hd=clsdoor.get_height()
            xcd=dx+longplat.get_width()/2-clsdoor.get_width()/2
            doorbox=p.Rect(xcd,HEIGHT*0.23-hd, wd ,hd) #manually put dy
            collidedoor=p.Rect.colliderect(hitbox, doorbox)
            if collidedoor:
                doorSeq=True
            if not collidedoor:
                doorSeq=False
    
    plats2=[]
    platk=p.Rect(WIDTH*.66, HEIGHT*0.1, 150, 5)
    plats2.append(ground)
    plats2.append(platk)
    Spikes2=[]
    
    if bg==cstle2:
        for plat in plats2:
            collide=p.Rect.colliderect(hitbox, plat)
            if collide:
                y = plat.y-63
                acc=0
        for spike in Spikes2:
            collidespike=p.Rect.colliderect(hitbox, spike)
            if collidespike:
                DEATH=True
        px=WIDTH*.66
        xck=px+medplat.get_width()/2
        keybox=p.Rect(xck,(HEIGHT*0.1)-50, 18, 32) #manually put py
        collidekey=p.Rect.colliderect(hitbox,keybox)
        if collidekey:
            key=True
      
    plats0=[]
    platA=p.Rect(WIDTH*.35, HEIGHT*.618, 150, 5)
    platB=p.Rect(WIDTH*0.77, HEIGHT*.55, 150, 5)
    platC=p.Rect(WIDTH*.35, HEIGHT*.2, 75, 5)
    platD=p.Rect(WIDTH*.57, HEIGHT*.07, 75, 5)
    platE=p.Rect(WIDTH*0.77, HEIGHT*.5, 150, 5)
    platK2=p.Rect(WIDTH*.77, HEIGHT*.083, 150, 5)
    plats0.append(ground)
    plats0.append(platA)
    plats0.append(platB)
    plats0.append(platC)
    plats0.append(platD)
    plats0.append(platK2)

    spikes0=[]
    spikeA=p.Rect(WIDTH*.134, (HEIGHT*0.4)+30, 75,30)
    spikeB=p.Rect(WIDTH*.35, (HEIGHT*0.2)+30, 75,30)
    spikeC=p.Rect(WIDTH*.57, (HEIGHT*0.07)+30, 75,29)
    spikeD=p.Rect(WIDTH*.77, (HEIGHT*0.083)+30, 75,29)
    spikeE=p.Rect(0, (HEIGHT*0.783)-tallSpike.get_height(), 75,30)
    spikeF=p.Rect(0, (HEIGHT*0.783)-spikes.get_height(), WIDTH,30)
    spikes0.append(spikeA)
    spikes0.append(spikeB)
    spikes0.append(spikeC)
    spikes0.append(spikeD)
    spikes0.append(spikeE)
    spikes0.append(spikeF)
    if bg==cstle0:
        for plat in plats0:
            collide=p.Rect.colliderect(hitbox, plat)
            if collide:
                y = plat.y-63
                acc=0
            for spike in spikes0:
                collidespike=p.Rect.colliderect(hitbox, spike)
                if collidespike:
                    DEATH=True    
        pxa=WIDTH*.77
        xck=pxa+medplat.get_width()/2
        keybox=p.Rect(xck,(HEIGHT*0.1)-50, 18, 32) #manually put py
        collidekey=p.Rect.colliderect(hitbox,keybox)
        if collidekey:
            key=True
    if not collide: #gravity
        acc+=1.5
        y+=acc

    
    drawWindow()