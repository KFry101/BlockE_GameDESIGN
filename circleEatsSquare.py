#Katie Frymire
#3/8/22
#make a pacman like game, move thing around screen, how to draw shape, how to use keys to move objects, dictionary

#objective of game: rectange to run away from circle;if the 2 collide, rect didappears and circle gets bigger

import os, time, random
import pygame

os.system('cls')

#intailize pygame
pygame.init()

#declare consants,variables, lists and dictionary
#screen size
WIDTH=700
HEIGHT= 700
check=True
move=1
#square variables
xs=20
ys=20
wbox=30
hbox=30
#circle variables
rad=15
xc=random.randint(rad, WIDTH-rad)
yc=random.randint(rad, HEIGHT-rad)
#create the rect object
square=pygame.Rect(xs, ys, wbox, hbox)

#create the screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))

#Define Colors
colors={'white': [255,255,255], 'red': [255,0,0], 'orange':[255, 85, 0], 'navy':[5, 31, 64], 
'forest':[16, 46, 12],'aqua':[51, 153, 255], 'pink': [200,75,125], 'litpur':[203,195,227],
'mag':[255, 0, 255], 'yellow':[240, 180, 14] }

#Get colors
background=colors.get('pink')
sq_color=colors.get('navy')
cr_color=colors.get('white')

#THE GAME
while check:
    screen.fill(background)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            check = False
        
    keys=pygame.key.get_pressed()
    #square control
    if keys[pygame.K_a] and square.x>=move :
        square.x -= move 
    if keys[pygame.K_d] and square.x <WIDTH-wbox:
        square.x += move
    if keys[pygame.K_w] and square.y>=move:
        square.y -= move  
    if keys[pygame.K_s] and square.y<=HEIGHT-hbox:
        square.y += move 
    #circle control
    if keys[pygame.K_LEFT] and xc >=rad:
        xc -= move
    if keys[pygame.K_RIGHT] and xc<=WIDTH-rad:
        xc += move
    if keys[pygame.K_UP] and yc>=rad:
        yc -= move
    if keys[pygame.K_DOWN] and yc<=HEIGHT-rad:
        yc+= move
    pygame.draw.rect(screen,sq_color, square)
    pygame.draw.circle(screen,cr_color, (xc,yc), rad)

    pygame.display.update()
 