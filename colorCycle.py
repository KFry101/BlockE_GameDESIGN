#katie frymire
#3/3/22


import pygame, os,time

os.system('cls')
pygame.init()

PURPLE=(49, 16, 115)
FOREST=(16, 46, 12)
NAVY=(5, 31, 64)
YELLOW=(240, 180, 14)



running=True
while running:
    global screen
    screen= pygame.display.set_mode([500,500])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#COLOR 1
    screen.fill(PURPLE)
    pygame.display.update()
    time.sleep(2)
#COLOR 2
    screen.fill(FOREST)
    pygame.display.update()
    time.sleep(2)
#COLOR3
    screen.fill(NAVY)
    pygame.display.update()
    time.sleep(2)
#COLOR 4
    screen.fill(YELLOW)
    pygame.display.update()
    time.sleep(2)


 
        
 



