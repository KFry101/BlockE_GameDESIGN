#katie frymire
#the level one of the final gmae

import os, time, datetime, math 
import pygame as p
os.system('cls')

#intailize p
p.init()

#Constants
JUMP=False
MAX=12
WIDTH=700
HEIGHT=700
DEATH=False

#screen
screen=p.display.set_mode((WIDTH,HEIGHT))
p.display.set_caption("Final Project")

