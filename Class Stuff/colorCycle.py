#katie frymire
#3/3/22


import pygame, os,time

os.system('cls')
pygame.init()

purple=(49, 16, 115)
forest=(16, 46, 12)
navy=(5, 31, 64)
yellow=(240, 180, 14)
white=[255, 255, 255]
aqua=[51, 153, 255]
blood=(102,0,0)
litpur=(203,195,227)
mag=[255, 0, 255]
orange=(255, 85, 0)

running=True
while running:
    screen= pygame.display.set_mode([500,500])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#COLOR 1
    screen.fill(purple)
    pygame.display.update()
    time.sleep(2)
#COLOR 2
    screen.fill(forest)
    pygame.display.update()
    time.sleep(2)
#COLOR3
    screen.fill(navy)
    pygame.display.update()
    time.sleep(2)
#COLOR 4
    screen.fill(yellow)
    pygame.display.update()
    time.sleep(2)


 
        
 



