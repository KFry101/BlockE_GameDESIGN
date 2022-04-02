#Katie Frymire
#3/8/22
#make a pacman like game, move thing around screen, how to draw shape, how to use keys to move objects, dictionary

#objective of game: rectange to run away from circle;if the 2 collide, rect disappears and circle gets bigger

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
LEV_1=False
LEV_2=False
LEV_3=False
PSCORE1=False
SCOREBOARD=False
# SCRB1=False
# SCRB2=False
# SCRB3=False
EXIT=False

#lists fr messages
MenuList=["Instructions", 'Settings', '  Level 1', '  Level 2', "  Level 3", "Scoreboard", "Exit"]
SettingList=[ 'Background Color', 'Circle Color']
BackColorList=['Aqua',"Magenta", "Yellow", "Orange"]
CrClrList=['Green', "White", "Lilac", "Navy"]
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
    p.display.update()

def instr():  
    txt=INST_FNT.render("Control the circle with the arrow keys", 1,(5, 31, 64))
    screen.blit(txt,(90,200))
    txt=INST_FNT.render("and absorb the square. If there is a ", 1, (5, 31, 64)) 
    screen.blit(txt,(90,240))
    txt=INST_FNT.render("second player, control the square with",1, (5, 31, 64))
    screen.blit(txt, (90,280))
    txt=INST_FNT.render("the wasd keys. You got to be quick!",1, (5, 31, 64))
    screen.blit(txt, (90,320))
    p.display.update()

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
    stuff=myFile.readlines()
    stuff.sort()
    print(len(stuff))
    if len(stuff)>5:
        n=5
    else:
        n=(len(stuff))
    
    for i in range(n, -1, -1):
        txt=INST_FNT.render(stuff[i], 1, (5, 31, 64))
        screen.blit(txt, (90,yi))
        yi+= 50
    myFile.close()



randColor=''
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


######################################################################################################################

MAX=10
jumpCount=10
JUMP=False
mouse_pos=(0,0)
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
       #For the name in leaderboard
        # txt= INST_FNT.render("Enter your name:", 1,(5,31,64))
        # xt= WIDTH/2-txt.get_width()/2
        # screen.blit(txt,(xt,380)) 
        
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

    if BACKCLR:
        if ((mouse_pos[0] >306 and mouse_pos[0] <393) and (mouse_pos[1] >560 and mouse_pos[1] <595)) or SETT:
            BACKCLR=False
            SETT=True
            p.time.delay(300)
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
            p.time.delay(300)
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

        if eaten>=10:
            LEV_1=False
            PSCORE1=True
            ticksEnd=p.time.get_ticks()
            print(ticksStart, ticksEnd)

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