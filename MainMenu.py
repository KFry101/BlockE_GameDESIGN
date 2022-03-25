#Katie Frymire
#3/23/22
#screen size, background color, circle color, Return. Main main


import pygame as p, time, random, math
p.init()

#VARIABLES
WIDTH=700
HEIGHT=700
xs=50
ys=250
wb=30
hb=30

#lists fr messages
MenuList=["Instruction", 'Setting', 'Level 1', 'Level 2', "Level 3", "Scoreboard", "Exit"]

#screen
screen=p.display.set_mode((WIDTH,HEIGHT))
p.display.set_caption("Circle Eats Square")

#Fonts
TITLE_FNT= p.font.SysFont("timesnewroman", 80)
SUBT_FNT= p.font.SysFont("timesnewroman", 25)
MENU_FNT= p.font.SysFont("comicsans", 40)
INST_FNT= p.font.SysFont('arial', 30)

#Titles


#Define Colors and Get colors
colors={'white': [255,255,255], 'red': [255,0,0], 'orange':[255, 85, 0], 'navy':[5, 31, 64], 
'forest':[16, 46, 12],'aqua':[51, 153, 255], 'pink': [200,75,125], 'litpur':[203,195,227],
'mag':[255, 0, 255], 'yellow':[240, 180, 14] }

background=colors.get('pink')
cr_color=colors.get('white')
inscribSq_color=colors.get('white')
sq_color=colors.get('navy')

#create diff text
#Create Text
txt=TITLE_FNT.render('Circle Eats Square', 1, (255, 255, 255))
screen.fill((200,75,125))
#get width of the text
#x value = WIDTH/2 - wtext
xt= WIDTH/2-txt.get_width()/2
screen.blit(txt,(xt,50))


# txt=INST_FNT.render("Instructions", 1, (5, 31, 64) )
# screen.blit(txt, (90,245))

#create square fr menu
txty=245

square=p.Rect(xs,ys,wb,hb)
for i in range(7):
    message=MenuList[i]
    txt=INST_FNT.render(message, 1, (5, 31, 64) )
    screen.blit(txt, (90,txty))
    txty+=50
    p.draw.rect(screen, sq_color, square)
    square.y+=50

p.display.update()
p.time.delay(10000)

# txt= MENU_FNT.render("Instructions", 1, (5, 31, 64))
#xt= WIDTH/2-txt.get_width()/2
#screen.blit(txt,(xt,50))
# screen.blit(txt, (xt,150))
# txt=INST_FNT.render("Control the circle with the arrow keys and absorb the square.", 1,(5, 31, 64))
# screen.blit(txt,(90,200))
# txt=INST_FNT.render("If there is a second player, control the square with the wasd keys.", 1, (5, 31, 64)) 
# screen.blit(txt,(90,225))
# txt=MENU_FNT.render("Return to Menu", 1, (255, 255, 255))
# screen.blit(txt,(200,550))
# p.display.update()

# p.time.delay(10000)
