#Katie Frymire
#3/8/22
#make a pacman like game, move thing around screen, how to draw shape, how to use keys to move objects, dictionary

#objective of game: rectange to run away from circle;if the 2 collide, rect disappears and circle gets bigger

import os, random, math
import pygame as p

os.system('cls')

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
LEV_1=False

#lists fr messages
MenuList=["Instructions", 'Settings', 'Level 1', 'Level 2', "Level 3", "Scoreboard", "Exit"]
SettingList=['Screen Size', 'Background Color', 'Circle Color']

#screen
screen=p.display.set_mode((WIDTH,HEIGHT))
p.display.set_caption("Circle Eats Square")

#Fonts
TITLE_FNT= p.font.SysFont("timesnewroman", 80)
SUBT_FNT= p.font.SysFont("timesnewroman", 25)
MENU_FNT= p.font.SysFont("arial", 50)
INST_FNT= p.font.SysFont('comicsans', 30)


#THE GAME VARIABLES
#declare consants,variables, lists and dictionary
check=True
move=5
grow=5
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
'forest':[16, 46, 12],'aqua':[51, 153, 255], 'pink': [200,75,125], 'litpur':[203,195,227],
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
    screen.fill((200,75,125))
    #get width of the text
    #x value = WIDTH/2 - wtext
    xt= WIDTH/2-txt.get_width()/2
    screen.blit(txt,(xt,50))

def ReturnBut():
    txt=MENU_FNT.render("Return to Menu", 1, (255, 255, 255))
    xt= WIDTH/2-txt.get_width()/2
    screen.blit(txt,(xt,550))
    

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
    txt=INST_FNT.render("the wasd keys.",1, (5, 31, 64))
    screen.blit(txt, (90,320))
    p.display.update()

randColor=''
def changeClr():
    print(background)
    global randColor
    colorCheck=True
    while colorCheck:
        randColor=random.choice(list(colors))
        print("rand Clr = ", randColor)
        if colors.get(randColor) == background:
            print("backgrnd = randclr")
            randColor=random.choice(list(colors))
        else:
            colorCheck=False
changeClr()
sq_color=colors.get(randColor)    

MAX=10
jumpCount=10
JUMP=False

while check:
    if MAIN:
        screen.fill(background)
        TitleMenu("Circle Eats Square")
        mainmenu(MenuList)
    if INSTR:
        screen.fill(background)
        TitleMenu("Instructions")
        ReturnBut()
        instr()
    if SETT:
        screen.fill(background)
        TitleMenu("Settings")
        ReturnBut()
        mainmenu(SettingList)
             
    for event in p.event.get():
        if event.type == p.QUIT:
            check = False
   
    keys=p.key.get_pressed()
    #Mouse Controls
    #Menu Navigation
    if event.type ==p.MOUSEBUTTONDOWN:
        mouse_pos=p.mouse.get_pos()
        print(mouse_pos)
        if MAIN:
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290))or INSTR:
                MAIN=False
                screen.fill(background)
                INSTR=True
            if((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <340))or SETT:
                MAIN=False
                SETT=True
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <380))or LEV_1:
                MAIN=False
                LEV_1=True
        
        if not MAIN and not LEV_1:
            if ((mouse_pos[0] >210 and mouse_pos[0] <490) and (mouse_pos[1] >561 and mouse_pos[1] <595))or MAIN:
                if INSTR:
                    INSTR=False
                    MAIN=True
                if SETT:
                    SETT=False
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
        
        sqCollide=squareG.colliderect((inscribSq))
        if sqCollide:
            squareG.x=random.randint(wbox, WIDTH-wbox)
            squareG.y=random.randint(hbox, HEIGHT-hbox)
            changeClr()
            sq_color=colors.get(randColor)  
            rad+=grow
        ibox=rad*math.sqrt(2)
        xig= xc-(ibox/2)
        yig= yc-(ibox/2)
        inscribSq=p.Rect(xig,yig,ibox,ibox)

        p.draw.rect(screen,sq_color, squareG)    
        p.draw.circle(screen,cr_color, (xc,yc), rad)
        p.draw.rect(screen,inscribSq_color, inscribSq)

        p.display.update()
        p.time.delay(10)
