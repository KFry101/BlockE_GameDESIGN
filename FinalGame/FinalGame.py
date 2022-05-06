#Katie Frymire
#3/8/22
#make a pacman like game, move thing around screen, how to draw shape, how to use keys to move objects, dictionary
#objective of game: rectange to run away from circle;if the 2 collide, rect disappears and circle gets bigger
#C:\Users\Katie\coding and game design\BlockE_GameDESIGN\Class Stuff\colorCycle.py
from decimal import ROUND_UP
import os, random, math,datetime
import pygame as p
os.system('cls')

name= input("What is your name?  ")
#intailize p
p.init()

#MENU VARIABLES
WIDTH=700
HEIGHT=700
xs=50
ys=250
wb=30
hb=30
#declare constants
MAIN=True
INSTR=False
SETT=False
BACKCLR=False
CRCLR=False
SIZE=False
LEV_1=False
LEV_2=False
LEV_3=False
PSCORE1=False
SCOREBOARD=False
EXIT=False
#lists fr messages
MenuList=["Instructions", 'Settings', '  Level 1', '  Level 2', "  Level 3", "Scoreboard", "Exit"]
SettingList=[ 'Background Color', 'Circle Color','Screen size']
BackColorList=['Aqua',"Magenta", "Yellow", "Orange"]
CrClrList=['Green', "White", "Lilac", "Navy"]
SizeList=['800x800', '1000x1000','Orginal']
#screen
screen=p.display.set_mode((WIDTH,HEIGHT))
p.display.set_caption("Circle Eats Square")
#Fonts
TITLE_FNT= p.font.SysFont("timesnewroman", 80)
SUBT_FNT= p.font.SysFont("comicsans", 40)
MENU_FNT= p.font.SysFont("arial", 50)
INST_FNT= p.font.SysFont('comicsans', 30)
#THE GAME VARIABLES
#declare consants,variables, lists and dictionary
check=True
move=5
grow=5
eaten=0
sec=0
#squareG variables
xsg=20
ysg=20
wbox=30
hbox=30
#circle variables
rad=15
xc=random.randint(rad, WIDTH-rad)
yc=random.randint(rad, HEIGHT-rad)
#inner box
ibox=rad*math.sqrt(2)
xig= xc-(ibox/2)
yig= yc-(ibox/2)
inscribSq=p.Rect(xig,yig,ibox,ibox)
#create the rect object
squareG=p.Rect(xsg, ysg, wbox, hbox)
square=p.Rect(xs,ys,wb,hb)
#Define Colors
colors={'white': [255,255,255], 'red': [255,0,0], 'orange':[255, 85, 0], 'navy':[5, 31, 64], 
'forest':[16, 46, 12],'aqua':[51, 153, 255], 'pink': [200,75,125], 'litpur':[203,160,227],
'mag':[255, 0, 255], 'yellow':[240, 180, 14] }
#Get colors
background=colors.get('pink')
sq_color=colors.get('navy')
cr_color=colors.get('white')
inscribSq_color=colors.get('white')
sqM_color=colors.get('navy')
#GLobalization setup
txt=''
txty=''
xt=''
def TitleMenu(message):
    txt=TITLE_FNT.render(message, 1, (255, 255, 255))
    screen.fill((background))
    #get width of the text
    #x value = WIDTH/2 - wtext
    xt= WIDTH/2-txt.get_width()/2
    screen.blit(txt,(xt,50))

def ReturnBut(message):
    txt=MENU_FNT.render(message, 1, (255, 255, 255))
    xt= WIDTH/2-txt.get_width()/2
    screen.blit(txt,(xt,550))
    
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier
# got this from https://realpython.com/python-rounding/#rounding-up
#this function uses parameters fr menu
def mainmenu(Mlist):
    txty=245
    square.y=250
    for i in range(len(Mlist)):
        message=Mlist[i]
        txt=INST_FNT.render(message, 1, (5, 31, 64) )
        screen.blit(txt, (90,txty))
        txty+=50
        p.draw.rect(screen, sqM_color, square)
        square.y+=50
  
def instr(): 
     
    txt=INST_FNT.render("Control the circle with the arrow keys", 1,(5, 31, 64))
    xt= WIDTH/2-txt.get_width()/2
    screen.blit(txt,(xt,200))
    txt=INST_FNT.render("and absorb the square. If there is a ", 1, (5, 31, 64)) 
    screen.blit(txt,(xt,240))
    txt=INST_FNT.render("second player, control the square with",1, (5, 31, 64))
    screen.blit(txt, (xt,280))
    txt=INST_FNT.render("the wasd keys. You got to be quick!",1, (5, 31, 64))
    screen.blit(txt, (xt,320)) 

def keepScore(score):
    date=datetime.datetime.now()
    print(date.strftime('%m/%d/%Y'))
    scoreLine=str(score)+"\t"+name+"\t"+date.strftime('%m/%d/%Y'+'\n')
    print (scoreLine)
    #open file and write in it
    myFile=open('Class Stuff\CircleEatsSquare\ScrBrd.txt', 'a')
    myFile.write(scoreLine)
    myFile.close()

def scoreb():
    myFile=open('Class Stuff\CircleEatsSquare\ScrBrd.txt', 'r')
    yi=150
    stuff= myFile.readlines()
    myFile.close()
    stuff.sort(reverse=True)

    for i in stuff[0:5]:
        txt=INST_FNT.render(i,1,"navy")
        xt= WIDTH/2-txt.get_width()/2
        screen.blit(txt, (xt,yi))
        yi+=50

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
    if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290)):
        HEIGHT=800
        WIDTH=800
        print('here!')

    if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <340)):
        HEIGHT=1000
        WIDTH=1000
        
    if ((mouse_pos[0] >0 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <390)):
        HEIGHT=700
        WIDTH=700
    screen=p.display.set_mode((WIDTH,HEIGHT))

def Level1():
    global DEATH
    global walkCount
    global keycount
    global doorCount
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
        screen.blit(clsdoor,(xd,dy-clsdoor.get_height()))
        if doorCount + 1 >=12:
            ds=0
            doorCount=11
            Ending=True
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

        fs=p.Rect(0,0,WIDTH,HEIGHT)
        # if Ending:
        #     fadeout()
    

            
                    
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
        for event in p.event.get():
            if event.type==p.MOUSEBUTTONDOWN:
                mouse_pos=p.mouse.get_pos()
                print(mouse_pos)
        #chara controls
        keys=p.key.get_pressed()
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

######################################################################################################################
MAX=10
jumpCount=10
JUMP=False
mouse_pos=(0,0)
xm= mouse_pos[0]
ym=mouse_pos[1]
while check:
    keys=p.key.get_pressed()
    if MAIN:
        screen.fill(background)
        TitleMenu("Circle Eats Square")
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
    if CRCLR:
        screen.fill(background)
        TitleMenu("Circle Color")
        ReturnBut("Back")
        mainmenu(CrClrList)
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
        ReturnBut("Return to Menu")
        txt=INST_FNT.render("Your score is:", 1,(5, 31, 64))
        xt= WIDTH/2-txt.get_width()/2
        screen.blit(txt,(xt,200))
        score= ((eaten)*5-2*(timePlyR))
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
        screen.blit(txt,(xt,200))
        txt=INST_FNT.render("Play again soon...", 1, (5, 31, 64)) 
        p.time.delay(2000)
        screen.blit(txt,(xt,240))
        p.time.delay(5000)
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
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <280))or INSTR:
                MAIN=False
                screen.fill(background)
                INSTR=True
            if((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <330))or SETT:
                MAIN=False 
                SETT=True
                p.time.delay(300)
                mouse_pos=(0,0)    
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <380))or LEV_1:
                MAIN=False
                LEV_1=True
                ticksStart=p.time.get_ticks()
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >400 and mouse_pos[1] <430))or LEV_2:
                MAIN=False
                LEV_2=True
                ticksStart=p.time.get_ticks()
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >450 and mouse_pos[1] <480))or LEV_3:
                MAIN=False
                LEV_3=True
                ticksStart=p.time.get_ticks()
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >500 and mouse_pos[1] <530))or SCOREBOARD:
                MAIN=False
                SCOREBOARD=True
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >550 and mouse_pos[1] <580))or EXIT:
                MAIN=False
                EXIT=True

        if SETT:
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290))or BACKCLR:
                SETT=False
                screen.fill(background)
                BACKCLR=True
                p.time.delay(300)
                mouse_pos=(0,0)
            if((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <340))or CRCLR:
                SETT=False
                CRCLR=True
                p.time.delay(300)
                mouse_pos=(0,0)
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <390)):
                SETT=False
                SIZE=True
                p.time.delay(400)
                mouse_pos=(0,0) 

        if BACKCLR:
            if ((mouse_pos[0] >306 and mouse_pos[0] <393) and (mouse_pos[1] >560 and mouse_pos[1] <595)) or SETT:
                BACKCLR=False
                SETT=True
                p.time.delay(400)
                mouse_pos=(0,0)
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290)):
                background=colors.get('aqua')  
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <340)):
                background=colors.get('mag')     
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <390)):
                background=colors.get('yellow')
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >400 and mouse_pos[1] <440)):
                background=colors.get('orange')   
        
        if CRCLR:

            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290)):
                cr_color=colors.get('forest') 
                inscribSq_color=colors.get('forest')  
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <340)):
                cr_color=colors.get('white') 
                inscribSq_color=colors.get('white')   
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <390)):
                cr_color=colors.get('litpur')  
                inscribSq_color=colors.get('litpur')  
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >400 and mouse_pos[1] <440)):
                cr_color=colors.get('navy')  
                inscribSq_color=colors.get('navy')  
            if ((mouse_pos[0] >306 and mouse_pos[0] <393) and (mouse_pos[1] >560 and mouse_pos[1] <595)) or SETT:
                CRCLR=False
                SETT=True
                p.time.delay(400)
                mouse_pos=(0,0)
        if SIZE:
            print("i am here!!!")
            changeScreenSize(xm,ym)
            if ((mouse_pos[0] >306 and mouse_pos[0] <393) and (mouse_pos[1] >560 and mouse_pos[1] <595)) or SETT:
                SIZE=False
                SETT=True
                p.time.delay(400)
                mouse_pos=(0,0)
                
        #return to Menu
        if not MAIN and not LEV_1:
            if ((mouse_pos[0] >210 and mouse_pos[0] <490) and (mouse_pos[1] >561 and mouse_pos[1] <595))or MAIN:
                if INSTR:
                    INSTR=False
                    MAIN=True
                if SETT:
                    SETT=False
                    MAIN=True
                if PSCORE1:
                    PSCORE1=False
                    MAIN=True
                    keepScore(score)
                if SCOREBOARD:
                    SCOREBOARD=False
                    MAIN=True

    #THE GAME Level 1
    if LEV_1:
        Level1()
    if LEV_2:        
        screen.fill(background)
        # Game Controls
        #squareG control
        if keys[p.K_a] and squareG.x>=move :
            squareG.x -= move 
        if keys[p.K_d] and squareG.x <=WIDTH-(wbox+move):
            squareG.x += move
        #jumping part
        if not JUMP:
            if keys[p.K_w] and squareG.y>=move:
                squareG.y -= move  
            if keys[p.K_s] and squareG.y<=HEIGHT-(hbox+move):
                squareG.y += move 
            if keys[p.K_SPACE]:
                JUMP=True
        else:
            if jumpCount>=-MAX:
                squareG.y -= jumpCount*abs(jumpCount)/2
                jumpCount-=1
            else:
                jumpCount=MAX
                JUMP=False
        #circle control
        if keys[p.K_LEFT] and xc >=rad+move:
            xc -= move
        if keys[p.K_RIGHT] and xc<=WIDTH-(rad+move):
            xc += move
        if keys[p.K_UP] and yc>=rad+move:
            yc -= move
        if keys[p.K_DOWN] and yc<=HEIGHT-(rad+move):
            yc+= move
        
        checkCollide=squareG.collidepoint((xc,yc))
        if checkCollide:
            squareG.x=random.randint(wbox, WIDTH-wbox)
            squareG.y=random.randint(hbox, HEIGHT-hbox)
            rad+=grow
        ibox=rad*math.sqrt(2)
        xig= xc-(ibox/2)
        yig= yc-(ibox/2)
        inscribSq=p.Rect(xig,yig,ibox,ibox)
        sqCollide=squareG.colliderect((inscribSq))
        if sqCollide:
            squareG.x=random.randint(wbox, WIDTH-wbox)
            squareG.y=random.randint(hbox, HEIGHT-hbox)
            changeClr()
            sq_color=colors.get(randColor)  
            rad+=grow
            eaten+=1
            # secs=Something to track the amount of time played

        p.draw.rect(screen,sq_color, squareG)    
        p.draw.circle(screen,cr_color, (xc,yc), rad)
        p.draw.rect(screen,inscribSq_color, inscribSq)

        if eaten>=20:
            LEV_2=False
            PSCORE1=True
            ticksEnd=p.time.get_ticks()
            print(ticksStart, ticksEnd)
    
    if LEV_3:        
        screen.fill(background)
        # Game Controls
        #squareG control
        if keys[p.K_a] and squareG.x>=move :
            squareG.x -= move 
        if keys[p.K_d] and squareG.x <=WIDTH-(wbox+move):
            squareG.x += move
        #jumping part
        if not JUMP:
            if keys[p.K_w] and squareG.y>=move:
                squareG.y -= move  
            if keys[p.K_s] and squareG.y<=HEIGHT-(hbox+move):
                squareG.y += move 
            if keys[p.K_SPACE]:
                JUMP=True
        else:
            if jumpCount>=-MAX:
                squareG.y -= jumpCount*abs(jumpCount)/2
                jumpCount-=1
            else:
                jumpCount=MAX
                JUMP=False
        #circle control
        if keys[p.K_LEFT] and xc >=rad+move:
            xc -= move
        if keys[p.K_RIGHT] and xc<=WIDTH-(rad+move):
            xc += move
        if keys[p.K_UP] and yc>=rad+move:
            yc -= move
        if keys[p.K_DOWN] and yc<=HEIGHT-(rad+move):
            yc+= move
        
        checkCollide=squareG.collidepoint((xc,yc))
        if checkCollide:
            squareG.x=random.randint(wbox, WIDTH-wbox)
            squareG.y=random.randint(hbox, HEIGHT-hbox)
            rad+=grow
        ibox=rad*math.sqrt(2)
        xig= xc-(ibox/2)
        yig= yc-(ibox/2)
        inscribSq=p.Rect(xig,yig,ibox,ibox)
        sqCollide=squareG.colliderect((inscribSq))
        if sqCollide:
            squareG.x=random.randint(wbox, WIDTH-wbox)
            squareG.y=random.randint(hbox, HEIGHT-hbox)
            changeClr()
            sq_color=colors.get(randColor)  
            rad+=grow
            eaten+=1
            # secs=Something to track the amount of time played
      
        p.draw.rect(screen,sq_color, squareG)    
        p.draw.circle(screen,cr_color, (xc,yc), rad)
        p.draw.rect(screen,inscribSq_color, inscribSq)

        if eaten>=30:
            LEV_3=False
            PSCORE1=True
            ticksEnd=p.time.get_ticks()
            print(ticksStart, ticksEnd)  
        
    p.display.update()
    p.time.delay(9)