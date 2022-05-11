#Katie Frymire
#Final Project for Class
from decimal import ROUND_UP
import os, random, math,datetime
import pygame as p
os.system('cls')

name= input("What is your name?  ")
#intailize p
p.init()

#MENU VARIABLES
WIDTH=700
HEIGHT=600
xs=50
ys=250
wb=30
hb=30
#declare constants
global LEV_1
global PSCORE1
MAIN=True
INSTR=False
SETT=False
BACKCLR=False
SIZE=False
LEV_1=False
LEV_2=False
LEV_3=False
PSCORE1=False
PSCORE2=False
PSCORE3=False
SCOREBOARD=False
EXIT=False
Ending=False
#lists fr messages
MenuList=["Instructions", 'Settings', '  Level 1', '  Level 2', "  Level 3", "Scoreboard", "Exit"]
SettingList=[ 'Background Color','Screen size']
BackColorList=['Aqua',"Magenta", "Yellow", "Orange"]
SizeList=['800x800', '1000x1000','Orginal']
#screen
screen=p.display.set_mode((WIDTH,HEIGHT))
p.display.set_caption("Doors: the game")
#Fonts
p.font.init()
#all non-SysFont fonts are made by "Chequered Ink"
popup = p.font.Font("FinalGame\Fonts\AGoblinAppears-o2aV.ttf",12)
fancy= p.font.Font("FinalGame\Fonts\AncientModernTales-a7Po.ttf", 100)
TITLE_FNT= p.font.SysFont("timesnewroman", 80)
SUBT_FNT= p.font.SysFont("comicsans", 40)
MENU_FNT= p.font.SysFont("arial", 50)
INST_FNT= p.font.SysFont('comicsans', 30)
#THE GAME VARIABLES
#declare consants,variables, lists and dictionary
check=True
move=5
grow=5
sec=0
#squareG variables
xsg=20
ysg=20
wbox=30
hbox=30
#create the rect object
squareG=p.Rect(xsg, ysg, wbox, hbox)
square=p.Rect(xs,ys,wb,hb)
#Define Colors
colors={'white': [255,255,255], 'red': [255,0,0], 'orange':[255, 85, 0], 'navy':[5, 31, 64], 
'forest':[16, 46, 12],'aqua':[51, 153, 255], 'pink': [200,75,125], 'litpur':[203,160,227],
'mag':[255, 0, 255], 'yellow':[240, 180, 14] }
#Get colors
background=colors.get('litpur')
sq_color=colors.get('navy')
cr_color=colors.get('white')
inscribSq_color=colors.get('white')
sqM_color=colors.get('navy')
#GLobalization setup
txt=''
txty=''
xt=''
def PopUpM(message):
        txt=popup.render(message, 1, (255, 255, 255))
        #get width of the text
        #x value = WIDTH/2 - wtext
        xt= WIDTH/2-txt.get_width()/2
        screen.blit(txt,(xt,HEIGHT*.016))
def FancyM(message):
    txt=fancy.render(message, 1, (255, 255, 255))
    screen.fill((background))
    #get width of the text
    #x value = WIDTH/2 - wtext
    xt= WIDTH/2-txt.get_width()/2
    screen.blit(txt,(xt,HEIGHT*.0714))
def TitleMenu(message):
    txt=TITLE_FNT.render(message, 1, (255, 255, 255))
    screen.fill((background))
    #get width of the text
    #x value = WIDTH/2 - wtext
    xt= WIDTH/2-txt.get_width()/2
    screen.blit(txt,(xt,HEIGHT*.0714))
def ReturnBut(message):
    txt=MENU_FNT.render(message, 1, (255, 255, 255))
    xt= WIDTH/2-txt.get_width()/2
    screen.blit(txt,(xt,HEIGHT*.69))
def ReturnButP(message):
    txt=MENU_FNT.render(message, 1, (255, 255, 255))
    xt= WIDTH/4-txt.get_width()/2
    screen.blit(txt,(xt,HEIGHT*.69))
def continueP(message):
    txt=MENU_FNT.render(message, 1, (255, 255, 255))
    xt= WIDTH*.75-txt.get_width()/2
    screen.blit(txt,(xt,HEIGHT*.69))    
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier
# got this from https://realpython.com/python-rounding/#rounding-up
#this function uses parameters fr menu
def mainmenu(Mlist):
    txty=HEIGHT*.35
    square.y=HEIGHT*.357
    for i in range(len(Mlist)):
        message=Mlist[i]
        txt=INST_FNT.render(message, 1, (5, 31, 64) )
        screen.blit(txt, (WIDTH*.128,txty))
        txty+=(HEIGHT*.0714)
        p.draw.rect(screen, sqM_color, square)
        square.y+=HEIGHT*.0714
  
def instr(): 
     
    txt=INST_FNT.render("Move with left and right arrows keys and ", 1,(5, 31, 64))
    xt= WIDTH/2-txt.get_width()/2
    screen.blit(txt,(xt,200))
    txt=INST_FNT.render("jump with space bar. Run by holding shift.", 1, (5, 31, 64)) 
    screen.blit(txt,(xt,240))
    txt=INST_FNT.render("You need to find the keys to the many doors",1, (5, 31, 64))
    screen.blit(txt, (xt,280))
    txt=INST_FNT.render("you will encounter. Good luck adventurer!!!",1, (5, 31, 64))
    screen.blit(txt, (xt,320)) 

def keepScore(score):
    date=datetime.datetime.now()
    print(date.strftime('%m/%d/%Y'))
    scoreLine=str(score)+"\t"+name+"\t"+date.strftime('%m/%d/%Y'+'\n')
    print (scoreLine)
    #open file and write in it
    myFile=open('FinalGame\SCore.txt', 'a')
    myFile.write(scoreLine)
    myFile.close()

def scoreb():
    myFile=open('FinalGame\SCore.txt', 'r')
    yi=HEIGHT*.2142
    stuff= myFile.readlines()
    myFile.close()
    stuff.sort(reverse=True)

    for i in stuff[0:5]:
        txt=INST_FNT.render(i,1,"navy")
        xt= WIDTH/2-txt.get_width()/2
        screen.blit(txt, (xt,yi))
        yi+=HEIGHT*.0714

def changeClr():
    global randColor
    colorCheck=True
    while colorCheck:
        randColor=random.choice(list(colors))
        if colors.get(randColor) == background:
            randColor=random.choice(list(colors))
        else:
            colorCheck=False
changeClr()
sq_color=colors.get(randColor)  

def changeScreenSize(xm,ym):
    global HEIGHT, WIDTH, screen
    if ((mouse_pos[0] >WIDTH*.0714 and mouse_pos[0] <WIDTH*0.114) and (mouse_pos[1] >250 and mouse_pos[1] <290)):
        HEIGHT=700
        WIDTH=800
        print('here!')

    if ((mouse_pos[0] >WIDTH*.0714 and mouse_pos[0] <WIDTH*0.114) and (mouse_pos[1] >300 and mouse_pos[1] <340)):
        HEIGHT=900
        WIDTH=1000
        
    if ((mouse_pos[0] >WIDTH*.0714 and mouse_pos[0] <WIDTH*0.114) and (mouse_pos[1] >350 and mouse_pos[1] <390)):
        HEIGHT=700
        WIDTH=600
    screen=p.display.set_mode((WIDTH,HEIGHT))

def Level1():
    global DEATH
    global deathcount
    global walkCount
    global keycount
    global doorCount
    global Ending
    global ticksEnd
    global Leave
    global LOCK
    global LEV_1
    global PSCORE1
    global MAIN
    p.font.init()
    #this font is from https://www.fontspace.com/a-goblin-appears-font-f30019
    #made by Chequered Ink
    popup = p.font.Font("FinalGame\Fonts\AGoblinAppears-o2aV.ttf",12)

    #Constants
    JUMP=False
    MAX=10
    WIDTH1=700
    HEIGHT1=600
    DEATH=False

    #variables
    deathcount=0
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
    Leave=False
    LOCK=False

    
    
    #screen
    screen=p.display.set_mode((WIDTH1,HEIGHT1))
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
        global LEV_1
        global PSCORE1
        global Ending
        global LOCK
        screen.blit(medplat,(dx,dy))
        xd=dx+medplat.get_width()/2-clsdoor.get_width()/2
        ds=1
        screen.blit(clsdoor,(xd,dy-clsdoor.get_height()))
        if doorCount + 1 >=12:
            ds=0
            doorCount=11
        elif collidedoor and not key: 
            LOCK=True
        if not doorSeq and not key:
            screen.blit(clsdoor,(xd,dy-clsdoor.get_height()))
        elif not doorSeq and key: 
            screen.blit(clsdoor,(xd,dy-clsdoor.get_height()))
        elif doorSeq and key:
            screen.blit(darkness, (xd,dy-clsdoor.get_height()+1))
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
        global LOCK
        global ticksEnd
        global LEV_1
        global PSCORE1
        #hidden collision items DRAWN
        #hitbox
        hitbox=p.Rect(x+14,y+14,36,50) #use hitbox for collisions
        p.draw.rect(screen,(0,0,0), hitbox) 
        #the platforms
        plats1=[]
        plat1 = p.Rect(WIDTH1-560,HEIGHT1-275, 150, 3)
        plat2=p.Rect(WIDTH1-320, HEIGHT1-390, 150,3)
        plat3=p.Rect(WIDTH1-100, HEIGHT1-500, 200, 3)
        platd=p.Rect(WIDTH1-660,HEIGHT1-420, 150, 3)
        ground=p.Rect(0, HEIGHT1-150, WIDTH1, 1)
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
            screen.blit(medplat,(WIDTH1-560,HEIGHT1-275))
            screen.blit(medplat,(WIDTH1-320, HEIGHT1-390))
            screen.blit(longplat,(WIDTH1-100, HEIGHT1-500))
            #door plat 
            doorPlat(WIDTH1-660,HEIGHT1-420)
        if bg==frst2:
            screen.blit(longplat,(-50, HEIGHT1-500))
            #key plat
            keyPlat(WIDTH1-450, HEIGHT1-390)
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
        xt= WIDTH1/2-txt.get_width()/2
        screen.blit(txt,(xt,HEIGHT1*.016))

    while run:   
        clock.tick(27)
        #the collide variable
        for event in p.event.get():
            if event.type==p.MOUSEBUTTONDOWN:
                mouse_pos=p.mouse.get_pos()
                print(mouse_pos)
        #chara controls
        keys=p.key.get_pressed()
        if event.type == p.QUIT:
            Leave= True
            run=False
        if keys[p.K_LSHIFT]:
            move=10
        else:
            move=5
        if keys[p.K_LEFT] and x >=-14:
            x -= move
            left=True
            right=False
        elif keys[p.K_RIGHT] and x<= WIDTH1-50:
            x += move
            right=True
            left=False
        else:
            left=False
            right=False
            walkCount=0

        if bg==forest: #screen with the door and
            if x>=WIDTH1-50:
                bg=frst2
                x=-13

        if bg==frst2: #screen with the key
            if x<=-14:
                bg=forest
                x=WIDTH1-50
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
        plat1 = p.Rect(WIDTH1-560,HEIGHT1-275, 150, 5)
        plat2=p.Rect(WIDTH1-320, HEIGHT1-390, 150,5)
        plat3=p.Rect(WIDTH1-100, HEIGHT1-500, 200, 5)
        platd=p.Rect(WIDTH1-660,HEIGHT1-420, 150, 5)
        ground=p.Rect(0, HEIGHT1-150, WIDTH1, 25)
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
                dx=WIDTH1-660
                wd=clsdoor.get_width()
                hd=clsdoor.get_height()
                xcd=dx+medplat.get_width()/2-clsdoor.get_width()/2
                doorbox=p.Rect(xcd,HEIGHT1-420-hd, wd ,hd) #manually put dy
                collidedoor=p.Rect.colliderect(hitbox, doorbox)
                if collidedoor:
                    doorSeq=True
                if not collidedoor:
                    doorSeq=False
        plats2=[]
        plat4=p.Rect(-50, HEIGHT1-500, 200, 5)
        plat5=p.Rect(WIDTH1-450, HEIGHT1-390, 200, 5)
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
            keybox=p.Rect(xck, HEIGHT1-440, 18, 32) #manually put py
            collidekey=p.Rect.colliderect(hitbox,keybox)
            if collidekey:
                key=True

        if not collide: #gravity
            acc+=1
            y+=acc
        if Ending:
            ticksEnd=p.time.get_ticks()
            print(ticksStart, ticksEnd) 
            Ending=False 

        if doorCount==11:
            ticksEnd=p.time.get_ticks()
            run=False
        drawWindow()
        
    if not run and not Leave:
        LEV_1=False
        PSCORE1=True  
    if not run and Leave:
        LEV_1=False
        MAIN=True 

def Level2():
    global DEATH
    global deathcount
    global walkCount
    global keycount
    global doorCount
    global Ending
    global ticksEnd
    global LOCK
    global MAIN
    global LEV_1
    global PSCORE2
    p.font.init()
    #this font is from https://www.fontspace.com/a-goblin-appears-font-f30019
    #made by Chequered Ink
    popup = p.font.Font("FinalGame\Fonts\AGoblinAppears-o2aV.ttf",12)

    #Constants
    JUMP=False
    MAX=10
    WIDTH1=700
    HEIGHT1=600
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
    screen=p.display.set_mode((WIDTH1,HEIGHT1))
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
        plat1 = p.Rect(WIDTH1-560,HEIGHT1-275, 150, 3)
        plat2=p.Rect(WIDTH1-320, HEIGHT1-390, 150,3)
        plat3=p.Rect(WIDTH1-100, HEIGHT1-500, 200, 3)
        platd=p.Rect(WIDTH1-660,HEIGHT1-420, 150, 3)
        ground=p.Rect(0, HEIGHT1-30, WIDTH1, 1)
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
            spike2=p.Rect(WIDTH1*.1, HEIGHT1*.825, 200,75)
            spike3=p.Rect(WIDTH1*.61, HEIGHT1*.825, 200,75)
            p.draw.rect(screen, (0,0,100), spike2)
            

        # background
        screen.blit(bg,(0,0))
    #actual graphics
        if bg==cave:
            #steping plats
            # screen.blit(medplat,(WIDTH-560,HEIGHT-275))
            screen.blit(medplat,((WIDTH1/3)-medplat.get_width(), HEIGHT1*0.5))
            screen.blit(smlPlat,(WIDTH1*0.542, HEIGHT1*.35))
            screen.blit(smlPlat,((WIDTH1/2)-smlPlat.get_width(),HEIGHT1*0.69))
            screen.blit(longplat,((WIDTH1*0.8), HEIGHT1*0.225 ))
            screen.blit(tallSpike,(WIDTH1*.68, HEIGHT1*.825))
            screen.blit(tallSpike,((WIDTH1*.68)+100, HEIGHT1*.825))
            #door plat 
            doorPlat(WIDTH1-660,HEIGHT1-420)
            
        if bg==cve2:
            screen.blit(longplat,(-50, HEIGHT1*0.225))
            screen.blit(medplat,(WIDTH1*.365, HEIGHT1*.028))
            screen.blit(dspikes,(WIDTH1*.365, (HEIGHT1*0.028)+30))
            screen.blit(dspikes,((WIDTH1*.365)+75, (HEIGHT1*0.028)+30))
            screen.blit(medplat,(WIDTH1*.398, HEIGHT1*.625))
            screen.blit(smlPlat,(WIDTH1*0.244, HEIGHT1*.458))
            screen.blit(tallSpike,(WIDTH1*.1, HEIGHT1*.825))
            screen.blit(tallSpike,((WIDTH1*.1)+100, HEIGHT1*.825))
            screen.blit(tallSpike,(WIDTH1*.61, HEIGHT1*.825))
            screen.blit(tallSpike,((WIDTH1*.61)+100, HEIGHT1*.825))
            #key plat
            keyPlat(WIDTH1*.75, HEIGHT1*0.42)
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
        xt= WIDTH1/2-txt.get_width()/2
        screen.blit(txt,(xt,HEIGHT1*.016))


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
                x=WIDTH1*0.0428
                y=HEIGHT1*.845
                jumpCount=10
                MAX=10
                DEATH=False
                JUMP=False
            
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
        elif keys[p.K_RIGHT] and x<= WIDTH1-50:
            x += move
            right=True
            left=False
        else:
            left=False
            right=False
            walkCount=0

        if bg==cave: #screen with the door and
            if x>=WIDTH1-50:
                bg=cve2
                x=-13

        if bg==cve2: #screen with the key
            if x<=-14:
                bg=cave
                x=WIDTH1-50
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
        plat1 = p.Rect((WIDTH1/2)-smlPlat.get_width(),HEIGHT1*0.69, 30, 5)
        plat2=p.Rect((WIDTH1/3)-medplat.get_width(), HEIGHT1*0.5, 150,5)
        plat3=p.Rect(WIDTH1*0.542, HEIGHT1*.35, 30, 5)
        plat0=p.Rect((WIDTH1*0.8), HEIGHT1*0.225, 200,5)
        platd=p.Rect(WIDTH1-660,HEIGHT1-420, 150, 5)
        ground=p.Rect(0, HEIGHT1-30, WIDTH1, 50)
        plats1.append(plat1)
        plats1.append(plat2)
        plats1.append(plat3)
        plats1.append(plat0)
        plats1.append(platd)
        plats1.append(ground)
        Spikes1=[] #############################################################################################
        spike1=p.Rect(WIDTH1*.68, HEIGHT1*.825, 200,75)
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
        plat4=p.Rect(-50, HEIGHT1*0.225, 200, 5)
        plat5=p.Rect(WIDTH1*.365, HEIGHT1*.028, 150, 5)
        plat6=p.Rect(WIDTH1*.397, HEIGHT1*.625, 150, 20)
        plat7=p.Rect(WIDTH1*0.244, HEIGHT1*.458, 30, 5)
        platk=p.Rect(WIDTH1*.76, HEIGHT1*0.42, 150, 5)
        plats2.append(ground)
        plats2.append(plat4)
        plats2.append(plat5)
        plats2.append(plat6)
        plats2.append(plat7)
        plats2.append(platk)
        Spikes2=[]
        spike2=p.Rect(WIDTH1*.1, HEIGHT1*.825, 200,75)
        spike3=p.Rect(WIDTH1*.61, HEIGHT1*.825, 200,75)
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
            px=WIDTH1*.75
            xck=px+medplat.get_width()/2
            keybox=p.Rect(xck,(HEIGHT1*0.375)-50, 18, 32) #manually put py
            collidekey=p.Rect.colliderect(hitbox,keybox)
            if collidekey:
                key=True

        if not collide: #gravity
            acc+=1
            y+=acc

        if doorCount==11:
            ticksEnd=p.time.get_ticks()
            run=False
        drawWindow()
    if not run and not Leave:
        LEV_2=False
        PSCORE2=True  
    if not run and Leave:
        LEV_2=False
        MAIN=True 
         
def Level3():
    global DEATH
    global deathcount
    global walkCount
    global keycount
    global doorCount
    global Ending
    global ticksEnd
    global LOCK
    global Leave
    p.font.init()
    #this font is from https://www.fontspace.com/a-goblin-appears-font-f30019
    #made by Chequered Ink
    popup = p.font.Font("FinalGame\Fonts\AGoblinAppears-o2aV.ttf",12)

    #Constants
    JUMP=False
    MAX=10
    WIDTH1=700
    HEIGHT1=600
    DEATH=False

    #screen
    screen=p.display.set_mode((WIDTH1,HEIGHT1))
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
    x=(WIDTH1/2)-(spr.get_width()/2)
    y= HEIGHT1*.6783
    key=False
    keyw2=False
    doorSeq=False
    Ending=False
    Leave=False
    LOCK=False
    ANOTHER=False
    
    def doorPlat(dx,dy):
        global doorCount
        global Ending
        global LOCK
        global ANOTHER
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
        elif collidedoor and not key and not keyw2: 
            LOCK=True
        elif doorSeq and key and not keyw2:
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
        spike3=p.Rect((WIDTH1*.501)-(longplat.get_width()/2), (HEIGHT1*0.23)+40, 75, 20)
        spike0=p.Rect((WIDTH1*.501)-(longplat.get_width()/2)+75, (HEIGHT1*0.23)+40, 75, 20)
        plats1.append(spike0)
        plats1.append(spike3)
        if bg==castle:
            for plat in plats1:
                p.draw.rect(screen,(255,0,0),plat)
        if bg==cstle2:
            for plat in plats2:
                p.draw.rect(screen,(255,0,0),plat)
            p.draw.rect(screen, (0,0,255), keybox)
            spike2=p.Rect(WIDTH1*.1, HEIGHT1*.825, 200,75)
            p.draw.rect(screen, (0,0,100), spike2)
        plats0=[]
        spikeA=p.Rect(WIDTH1*.134, (HEIGHT1*0.4)+55, 75,3)
        spikeB=p.Rect(WIDTH1*.35, (HEIGHT1*0.2)+55, 75,3)
        spikeC=p.Rect(WIDTH1*.57, (HEIGHT1*0.07)+55, 75,3)
        spikeD=p.Rect(WIDTH1*.77, (HEIGHT1*0.083)+55, 75,3)
        spikeE=p.Rect(0, (HEIGHT1*0.783)-tallSpike.get_height(), 100,75)
        spikeF=p.Rect(0, (HEIGHT1*0.783)-spikes.get_height(), WIDTH1,30)
        plats0.append(spikeA)
        plats0.append(spikeB)
        plats0.append(spikeC)
        plats0.append(spikeD)
        plats0.append(spikeE)
        plats0.append(spikeF)

        

        if bg==cstle0:
            for plat in plats0:
                p.draw.rect(screen,(255,0,255),plat)


        #background
        screen.blit(bg,(0,0))
    #actual graphics
        if bg==cstle0:
            #ground
            screen.blit(tallSpike,((0), (HEIGHT1*0.785)-tallSpike.get_height()))
            screen.blit(spikes,((tallSpike.get_width()), (HEIGHT1*0.785)-spikes.get_height()))
            screen.blit(spikes,((tallSpike.get_width()+spikes.get_width()), (HEIGHT*10.783)-spikes.get_height()))
            screen.blit(spikes,((tallSpike.get_width()+spikes.get_width()*2), (HEIGHT1*0.783)-spikes.get_height()))
            screen.blit(spikes,((tallSpike.get_width()+spikes.get_width()*3), (HEIGHT1*0.783)-spikes.get_height()))
            screen.blit(spikes,((tallSpike.get_width()+spikes.get_width()*4), (HEIGHT1*0.783)-spikes.get_height()))
            screen.blit(spikes,((tallSpike.get_width()+spikes.get_width()*5), (HEIGHT1*0.783)-spikes.get_height()))
            screen.blit(spikes,((tallSpike.get_width()+spikes.get_width()*6), (HEIGHT1*0.783)-spikes.get_height()))
            screen.blit(spikes,((tallSpike.get_width()+spikes.get_width()*7), (HEIGHT1*0.783)-spikes.get_height()))
            #plats
            screen.blit(medplat,(WIDTH1*0.77, HEIGHT1*.55))
            screen.blit(medplat,((WIDTH1*.35), HEIGHT1*.618))
            screen.blit(smlPlat,((WIDTH1*.134), HEIGHT1*.4))
            screen.blit(dspikes,(WIDTH1*.134, (HEIGHT1*0.4)+30))
            screen.blit(smlPlat,((WIDTH1*.35), HEIGHT1*.2))
            screen.blit(dspikes,(WIDTH1*.35, (HEIGHT1*0.2)+30))
            screen.blit(smlPlat,((WIDTH1*.57), HEIGHT1*.07))
            screen.blit(dspikes,(WIDTH1*.57, (HEIGHT1*0.07)+30))
            #key 
            wKeyPlat(WIDTH1*.77, HEIGHT1*.083)
            screen.blit(dspikes,(WIDTH1*.77, (HEIGHT1*0.083)+30))
        if bg==castle:
            # screen.blit(medplat,(WIDTH-560,HEIGHT-275))
            screen.blit(smlPlat,((WIDTH1*.3)-25, HEIGHT1*.605))
            screen.blit(smlPlat,((WIDTH1*.6)+25, HEIGHT1*.605))
            screen.blit(medplat,((WIDTH1*.03), HEIGHT1*.4))
            screen.blit(medplat,((WIDTH1*.74), HEIGHT1*.4))
            screen.blit(tallSpike,(0, (HEIGHT1*0.785)-tallSpike.get_height()))
            screen.blit(tallSpike,((WIDTH1-tallSpike.get_width()), (HEIGHT1*0.785)-tallSpike.get_height()))
            
            #door plat 
            doorPlat((WIDTH1/2)-(longplat.get_width()/2), HEIGHT1*0.23)
            # screen.blit(dspikes,((WIDTH*.501)-(longplat.get_width()/2), (HEIGHT*0.23)+30))
            # screen.blit(dspikes,((WIDTH*.501)-(longplat.get_width()/2)+dspikes.get_width(), (HEIGHT*0.23)+30))
            # screen.blit(dspikes,((WIDTH*.501)-(longplat.get_width()/2)+(dspikes.get_width()*1.6), (HEIGHT*0.23)+30))
            
        if bg==cstle2:
            screen.blit(medplat,(WIDTH1*.398, HEIGHT1*.625))
            screen.blit(medplat,(WIDTH1*0.11, HEIGHT1*.5))
            screen.blit(smlPlat,((WIDTH1*.44), HEIGHT1*.35))
            screen.blit(medplat,((WIDTH1*.23), HEIGHT1*.155))
            screen.blit(dspikes,((WIDTH1*.23), (HEIGHT1*0.155)+30))
            screen.blit(dspikes,((WIDTH1*.23)+dspikes.get_width(), (HEIGHT1*0.155)+30))
            screen.blit(tallSpike,(WIDTH1*.1, (HEIGHT1*0.785)-tallSpike.get_height()))
            screen.blit(tallSpike,((WIDTH1*.1)+100,(HEIGHT1*0.785)-tallSpike.get_height()))
            screen.blit(tallSpike,(WIDTH1*.61, (HEIGHT1*0.785)-tallSpike.get_height()))
            screen.blit(tallSpike,((WIDTH1*.61)+100, (HEIGHT1*0.785)-tallSpike.get_height()))
            #key plat
            bKeyPlat(WIDTH1*.65, HEIGHT1*0.1)
            screen.blit(dspikes,((WIDTH1*.65), (HEIGHT1*0.1)+30))
            screen.blit(dspikes,((WIDTH1*.65)+dspikes.get_width(), (HEIGHT1*0.1)+30))
            
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
            PopUpM("It is locked")  
            LOCK=False    
        if ANOTHER:
            PopUpM("It seems there is another lock")
            ANOTHER=False
        p.display.update()

    def PopUpM(message):
        txt=popup.render(message, 1, (255, 255, 255))
        #get width of the text
        #x value = WIDTH/2 - wtext
        xt= WIDTH1/2-txt.get_width()/2
        screen.blit(txt,(xt,HEIGHT*.016))

    while run:   
        global plat
        global ground
        clock.tick(27)
        if DEATH:
            JUMP=False #NEED TO BE ADJUST FOR NEW STUFF
            if not collide:
                acc=0
                acc+=0
                y+=1
            
        
                
            collide=p.Rect.colliderect(hitbox, plat)
            for plat in plats0:
                if collide:
                    spr=rip
        
            collide=p.Rect.colliderect(hitbox, plat)
            for plat in plats1:
                if collide:
                    spr=rip
        
            collide=p.Rect.colliderect(hitbox, plat)
            for plat in plats2:
                if collide:
                        spr=rip
            if spr==rip and (keys[p.K_LEFT] or keys[p.K_RIGHT]):
                deathcount+=1
                bg=castle
                spr=chara
                x=(WIDTH1/2)
                y=HEIGHT1*.6783
                jumpCount=10
                MAX=10
                DEATH=False
                JUMP=False
            
        for event in p.event.get():

            if event.type == p.QUIT:
                Leave= True
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
        elif keys[p.K_RIGHT] and x<= WIDTH1-50:
            x += move
            right=True
            left=False
        else:
            left=False
            right=False
            walkCount=0
        if bg==cstle0:
                if x>=WIDTH1-50:
                    bg=castle
                    x=-13
        if bg==castle: #screen with the door and
            if x>=WIDTH1-50:
                bg=cstle2
                x=-13
            if x<=-14:
                bg=cstle0
                x=WIDTH1-50
        if bg==cstle2: 
            if x<=-14:
                bg=castle
                x=WIDTH1-50
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
        hitbox=p.Rect(x+16,y+14,3,50)
        plats1=[]
        plat1=p.Rect((WIDTH1*.3)-25, HEIGHT1*.605, 75, 5)
        plat2=p.Rect((WIDTH1*.6)+25, HEIGHT1*.605, 75, 5)
        plat3=p.Rect((WIDTH1*.74), HEIGHT1*.4, 150, 5)
        plat4=p.Rect(WIDTH1*.03, HEIGHT1*.4, 150, 5)
        platd=p.Rect((WIDTH1/2)-100, HEIGHT1*0.23, 200, 5)
        ground=p.Rect(0, HEIGHT1*0.783, WIDTH1, 50)
        plats1.append(platd)
        plats1.append(plat1)
        plats1.append(plat2)
        plats1.append(plat3)
        plats1.append(plat4)
        plats1.append(ground)
        Spikes1=[] #############################################################################################
        spike1=p.Rect(0, (HEIGHT1*0.78)-tallSpike.get_height(), 100,70)
        spike2=p.Rect(WIDTH1-tallSpike.get_width(), (HEIGHT1*0.78)-tallSpike.get_height(), 100,70)
        Spikes1.append(spike1)
        Spikes1.append(spike2)
        if bg==castle:
            for spike in Spikes1:
                collidespike=p.Rect.colliderect(hitbox, spike)
                if collidespike:
                    DEATH=True
            for plat in plats1:
                collide=p.Rect.colliderect(hitbox, plat)
                if collide:
                    y = plat.y-63
                    acc=0
            dx=(WIDTH1/2)-100
            wd=clsdoor.get_width()
            hd=clsdoor.get_height()
            xcd=dx+longplat.get_width()/2-clsdoor.get_width()/2
            doorbox=p.Rect(xcd,HEIGHT1*0.23-hd, wd ,hd) #manually put dy
            collidedoor=p.Rect.colliderect(hitbox, doorbox)
            if collidedoor:
                doorSeq=True
            if not collidedoor:
                doorSeq=False
        
        plats2=[]
        platk=p.Rect(WIDTH1*.66, HEIGHT1*0.1, 150, 5)
        plat6=p.Rect(WIDTH1*.398, HEIGHT1*.625, 150, 5)
        plat7=p.Rect(WIDTH1*0.11, HEIGHT1*.5, 150, 5)
        plat8=p.Rect(WIDTH1*.44, HEIGHT1*.35, 75, 5)
        plat9=p.Rect((WIDTH1*.23), HEIGHT1*.155, 150, 5)
        plats2.append(ground)
        plats2.append(platk)
        plats2.append(plat6)
        plats2.append(plat7)
        plats2.append(plat8)
        plats2.append(plat9)
        Spikes2=[]
        spike4=p.Rect(WIDTH1*.25, ((HEIGHT1*0.155)+55), 70, 5)
        spike5=p.Rect((WIDTH1*.23)+dspikes.get_width(), (HEIGHT1*0.155)+55, 70, 5)
        spike6=p.Rect((WIDTH1*.68), (HEIGHT1*0.1)+55, 70, 5)
        spike7=p.Rect((WIDTH1*.65)+dspikes.get_width(), (HEIGHT1*0.1)+55, 75, 35)
        spike8=p.Rect(WIDTH1*.1, (HEIGHT1*0.785)-tallSpike.get_height(), 100, 75)
        spike9=p.Rect((WIDTH1*.1)+100,(HEIGHT1*0.785)-tallSpike.get_height(), 100, 75)
        spike10=p.Rect((WIDTH1*.65), (HEIGHT1*0.785)-tallSpike.get_height(), 100, 75)
        spike11=p.Rect((WIDTH1*.61)+100, (HEIGHT1*0.785)-tallSpike.get_height(), 100, 75)
        Spikes2.append(spike4)
        Spikes2.append(spike5)
        Spikes2.append(spike6)
        Spikes2.append(spike7)
        Spikes2.append(spike8)
        Spikes2.append(spike9)
        Spikes2.append(spike10)
        Spikes2.append(spike11)

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
            keybox=p.Rect(xck,(HEIGHT1*0.1)-50, 18, 32) #manually put py
            collidekey=p.Rect.colliderect(hitbox,keybox)
            if collidekey:
                key=True
        
        plats0=[]
        platA=p.Rect(WIDTH1*.35, HEIGHT1*.618, 150, 5)
        platB=p.Rect(WIDTH1*0.77, HEIGHT1*.55, 150, 5)
        platC=p.Rect(WIDTH1*.35, HEIGHT1*.2, 75, 5)
        platD=p.Rect(WIDTH1*.57, HEIGHT1*.07, 75, 5)
        platK2=p.Rect(WIDTH1*.77, HEIGHT1*.083, 150, 5)
        platF=p.Rect(WIDTH1*.134, (HEIGHT1*0.4), 75,5)
        plats0.append(ground)
        plats0.append(platA)
        plats0.append(platB)
        plats0.append(platC)
        plats0.append(platD)
        plats0.append(platK2)
        plats0.append(platF)


        spikes0=[]
        spikeB=p.Rect(WIDTH1*.35, (HEIGHT1*0.2)+55, 75,3)
        spikeC=p.Rect(WIDTH1*.57, (HEIGHT1*0.07)+55, 75,3)
        spikeD=p.Rect(WIDTH1*.77, (HEIGHT1*0.083)+55, 75,3)
        spikeE=p.Rect(0, (HEIGHT1*0.783)-tallSpike.get_height(), 100,75)
        spikeF=p.Rect(0, (HEIGHT1*0.783)-spikes.get_height(), WIDTH1,30)

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
            keybox=p.Rect(xck,(HEIGHT1*0.1)-50, 18, 32) #manually put py
            collidekey=p.Rect.colliderect(hitbox,keybox)
            if collidekey:
                key=True
        if not collide: #gravity
            acc+=1.5
            y+=acc
        if doorCount==11:
            ticksEnd=p.time.get_ticks()
            run=False
        drawWindow()
        

######################################################################################################################
MAX=10
WIDTH=700
HEIGHT=700
jumpCount=10
JUMP=False
mouse_pos=(0,0)
xm= mouse_pos[0]
ym=mouse_pos[1]
while check:
    keys=p.key.get_pressed()
    if MAIN:
        screen.fill(background)
        FancyM("D o o r s")
        mainmenu(MenuList)
    if INSTR:
        screen.fill(background)
        TitleMenu("Instructions")
        ReturnBut("Return to Menu")
        instr()
    if SETT: 
        screen.fill(background)
        TitleMenu("Settings")
        ReturnBut("Return to Menu")
        mainmenu(SettingList)   
    if BACKCLR:
        screen.fill(background)
        TitleMenu("Background Color")
        ReturnBut("Back")
        mainmenu(BackColorList)   
    if SIZE:
        screen.fill(background)
        TitleMenu("Screen Size")
        ReturnBut("Back")
        mainmenu(SizeList)     
    if PSCORE1:
        timePlayed=((ticksEnd/1000)-(ticksStart/1000))
        timePlyR=round_up(timePlayed)
        screen.fill(background)
        TitleMenu("Your Score")

        ReturnButP("Return to Menu")
        continueP("Next Level")
        txt=INST_FNT.render("Your score is:", 1,(5, 31, 64))
        xt= WIDTH/2-txt.get_width()/2
        screen.blit(txt,(xt,200))
        score= 1000-(timePlyR)-(deathcount*2)
        txt=SUBT_FNT.render(str(score), 1, (5, 31, 64))
        xt= WIDTH/2-txt.get_width()/2
        screen.blit(txt,(xt,250))       
    if PSCORE2:
        timePlayed=((ticksEnd/1000)-(ticksStart/1000))
        timePlyR=round_up(timePlayed)
        screen.fill(background)
        TitleMenu("Your Score")
        ReturnButP("Return to Menu")
        continueP("Next Level")
        txt=INST_FNT.render("Your score is:", 1,(5, 31, 64))
        xt= WIDTH/2-txt.get_width()/2
        screen.blit(txt,(xt,200))
        score= 1000-(timePlyR)-(deathcount*2)
        txt=SUBT_FNT.render(str(score), 1, (5, 31, 64))
        xt= WIDTH/2-txt.get_width()/2
        screen.blit(txt,(xt,250))       
    if PSCORE3:
        timePlayed=((ticksEnd/1000)-(ticksStart/1000))
        timePlyR=round_up(timePlayed)
        screen.fill(background)
        TitleMenu("Your Score")
        ReturnBut("Return to Menu")
        txt=INST_FNT.render("Your score is:", 1,(5, 31, 64))
        xt= WIDTH/2-txt.get_width()/2
        screen.blit(txt,(xt,200))
        score= 1000-(timePlyR)-(deathcount*2)
        txt=SUBT_FNT.render(str(score), 1, (5, 31, 64))
        xt= WIDTH/2-txt.get_width()/2
        screen.blit(txt,(xt,250))       
    if SCOREBOARD:
        screen.fill(background)
        TitleMenu("ScoreBoard") 
        ReturnBut("Return to Menu")
        scoreb()           
    if EXIT:
        screen.fill(background)
        txt=INST_FNT.render("Thank you for Playing", 1,(5, 31, 64))
        xt= WIDTH/2-txt.get_width()/2
        screen.blit(txt,(xt,200))
        txt=INST_FNT.render("Play again soon...", 1, (5, 31, 64)) 
        xt= WIDTH/2-txt.get_width()/2
        p.time.delay(2000)
        screen.blit(txt,(xt,240))
        p.time.delay(4000)
        p.QUIT    
    for event in p.event.get():
        if event.type == p.QUIT:
            check = False 
    #Mouse Controls
    #Menu Navigation
    if event.type ==p.MOUSEBUTTONDOWN:
        mouse_pos=p.mouse.get_pos()
        print(mouse_pos)
        
        if MAIN:
            eaten=0
            rad=15
            if ((mouse_pos[0] >WIDTH*.0714 and mouse_pos[0] <WIDTH*0.114) and (mouse_pos[1] >HEIGHT*.3571 and mouse_pos[1] <HEIGHT*.414))or INSTR:
                MAIN=False
                screen.fill(background)
                INSTR=True
            if((mouse_pos[0] >WIDTH*.0714 and mouse_pos[0] <WIDTH*0.114) and (mouse_pos[1] >HEIGHT*.4285 and mouse_pos[1] <HEIGHT*.4714))or SETT:
                MAIN=False 
                SETT=True
                p.time.delay(300)
                mouse_pos=(0,0)    
            if ((mouse_pos[0] >WIDTH*.0714 and mouse_pos[0] <WIDTH*0.114) and (mouse_pos[1] >HEIGHT*.5 and mouse_pos[1] <HEIGHT*.5428))or LEV_1:
                MAIN=False
                LEV_1=True
                ticksStart=p.time.get_ticks()
            if ((mouse_pos[0] >WIDTH*.0714 and mouse_pos[0] <WIDTH*0.114) and (mouse_pos[1] >HEIGHT*.5714 and mouse_pos[1] <HEIGHT*.6142))or LEV_2:
                MAIN=False
                LEV_2=True
                ticksStart=p.time.get_ticks()
            if ((mouse_pos[0] >WIDTH*.0714 and mouse_pos[0] <WIDTH*0.114) and (mouse_pos[1] >HEIGHT*.6428 and mouse_pos[1] <HEIGHT*.6857))or LEV_3:
                MAIN=False
                LEV_3=True
                ticksStart=p.time.get_ticks()
            if ((mouse_pos[0] >WIDTH*.0714 and mouse_pos[0] <WIDTH*0.114) and (mouse_pos[1] >HEIGHT*.7142 and mouse_pos[1] <HEIGHT*.7571))or SCOREBOARD:
                MAIN=False
                SCOREBOARD=True
            if ((mouse_pos[0] >WIDTH*.0714 and mouse_pos[0] <WIDTH*0.114) and (mouse_pos[1] >HEIGHT*.7857 and mouse_pos[1] <HEIGHT*.8285))or EXIT:
                MAIN=False
                EXIT=True

        if SETT:
            if ((mouse_pos[0] >WIDTH*.0714 and mouse_pos[0] <WIDTH*0.114) and (mouse_pos[1] >HEIGHT*.3571 and mouse_pos[1] <HEIGHT*.4142))or BACKCLR:
                SETT=False
                screen.fill(background)
                BACKCLR=True
                p.time.delay(300)
                mouse_pos=(0,0)
            if((mouse_pos[0] >WIDTH*.0714 and mouse_pos[0] <WIDTH*0.114) and (mouse_pos[1] >HEIGHT*.4285 and mouse_pos[1] <HEIGHT*.4857))or SIZE:
                SETT=False
                SIZE=True
                p.time.delay(400)
                mouse_pos=(0,0) 

        if BACKCLR:
            if ((mouse_pos[0] >WIDTH*.4371 and mouse_pos[0] <WIDTH*.5614) and (mouse_pos[1] >HEIGHT*.69 and mouse_pos[1] <HEIGHT*.75)) or SETT:
                BACKCLR=False
                SETT=True
                p.time.delay(400)
                mouse_pos=(0,0)
            if ((mouse_pos[0] >WIDTH*.0714 and mouse_pos[0] <WIDTH*0.114) and (mouse_pos[1] >HEIGHT*.3571 and mouse_pos[1] <HEIGHT*.4142)):
                background=colors.get('aqua')  
            if ((mouse_pos[0] >WIDTH*.0714 and mouse_pos[0] <WIDTH*0.114) and (mouse_pos[1] >HEIGHT*.4285 and mouse_pos[1] <HEIGHT*.4857)):
                background=colors.get('mag')     
            if ((mouse_pos[0] >WIDTH*.0714 and mouse_pos[0] <WIDTH*0.114) and (mouse_pos[1] >HEIGHT*.5 and mouse_pos[1] <HEIGHT*.5571)):
                background=colors.get('yellow')
            if ((mouse_pos[0] >WIDTH*.07140 and mouse_pos[0] <WIDTH*0.114) and (mouse_pos[1] >HEIGHT*.5714 and mouse_pos[1] <440)):
                background=colors.get('orange')   
        
        if SIZE:
            changeScreenSize(xm,ym)
            if ((mouse_pos[0] >WIDTH*.4371 and mouse_pos[0] <WIDTH*.5614) and (mouse_pos[1] >HEIGHT*.69 and mouse_pos[1] <HEIGHT*.75)) or SETT:
                SIZE=False
                SETT=True
                p.time.delay(400)
                mouse_pos=(0,0)
        #return to Menu
        if not MAIN and not LEV_1 and not LEV_2 and not LEV_3 and not PSCORE1 and not PSCORE2:
            if ((mouse_pos[0] >WIDTH*.3 and mouse_pos[0] <WIDTH*.7) and (mouse_pos[1] >HEIGHT*.69 and mouse_pos[1] <HEIGHT*.75))or MAIN:
                if INSTR:
                    INSTR=False
                    MAIN=True
                if SETT:
                    SETT=False
                    MAIN=True
                if PSCORE3:
                    PSCORE1=False
                    MAIN=True
                    keepScore(score)
                if SCOREBOARD:
                    SCOREBOARD=False
                    MAIN=True
        if PSCORE1:
            if ((mouse_pos[0] >WIDTH*.25 and mouse_pos[0] <WIDTH*.65) and (mouse_pos[1] >HEIGHT*.69 and mouse_pos[1] <HEIGHT*.85))or MAIN:
                PSCORE1=False
                MAIN=True
                keepScore(score)
            if ((mouse_pos[0] >WIDTH*.75 and mouse_pos[0] <WIDTH*.9) and (mouse_pos[1] >HEIGHT*.69 and mouse_pos[1] <HEIGHT*.85))or LEV_2:
                if PSCORE1:
                    PSCORE1=False
                    LEV_2=True
                    keepScore(score)
        if PSCORE2:
            if ((mouse_pos[0] >WIDTH*.25 and mouse_pos[0] <WIDTH*.65) and (mouse_pos[1] >HEIGHT*.69 and mouse_pos[1] <HEIGHT*.85))or MAIN:
                PSCORE2=False
                MAIN=True
                keepScore(score)
            if ((mouse_pos[0] >WIDTH*.75 and mouse_pos[0] <WIDTH*.9) and (mouse_pos[1] >HEIGHT*.69 and mouse_pos[1] <HEIGHT*.85))or LEV_3:
                PSCORE2=False
                LEV_3=True
                keepScore(score)
                PSCORE2=False
                LEV_3=True
                keepScore(score)
        
    #THE GAME 
    keys=p.key.get_pressed()

    if LEV_1:
        Level1()
        if keys[p.K_ESCAPE]: #leave the level
            LEV_1=False
            MAIN=True

        if Ending: 
            LEV_1=False
            PSCORE1=True
    if LEV_2:        
        Level2()
        if keys[p.K_ESCAPE]:
            LEV_2=False
            MAIN=True
        if Ending:
            LEV_2=False
            PSCORE2=True
    if LEV_3:        
        Level3()
        if keys[p.K_ESCAPE]:
            LEV_3=False
            MAIN=True
        if Ending:
            LEV_3=False
            PSCORE3=True
          
    p.display.update()
    p.time.delay(9)