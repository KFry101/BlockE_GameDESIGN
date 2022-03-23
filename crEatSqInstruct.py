#katie Frymire
#3/22/22
# instruction screen for cr eats sq game

#import and set up window
import pygame as p, time
p.init()
wind=p.display.set_mode((700,700))
p.display.set_caption("testing")

#create diff text
TITLE_FNT= p.font.SysFont("timesnewroman", 80)
SUBT_FNT= p.font.SysFont("timesnewroman", 25)
MENU_FNT= p.font.SysFont("comicsans", 40)
INST_FNT= p.font.SysFont('arial', 25)
txt=TITLE_FNT.render('Circle Eats Square', 1, (255, 255, 255))
wind.fill((200,75,125))
wind.blit(txt,(50,50))
txt=SUBT_FNT.render("The Game", 1, (255, 255, 255))
wind.blit(txt,(525,125))
txt= MENU_FNT.render("Instructions:", 1, (5, 31, 64))
wind.blit(txt, (80,150))
txt=INST_FNT.render("Control the circle with the arrow keys and absorb the square.", 1,(5, 31, 64))
wind.blit(txt,(90,200))
txt=INST_FNT.render("If there is a second player, control the square with the wasd keys.", 1, (5, 31, 64)) 
wind.blit(txt,(90,225))
p.display.update()

p.time.delay(10000)