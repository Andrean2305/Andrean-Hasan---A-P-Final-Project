import pygame 
import os

from permainan import * #importing game progress
from tkinter import *
from ALLFUNC import *
from SCREEN2_PLAYING import *

os.chdir('C:/Users/Asus/FinalProjectSirJude')
from pygame.locals import *

pygame.init()
screen_width = 1275
screen_height = 650

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Platformer')

bg_img = pygame.image.load(lagu("weather.jpg"))
# sun_img = pygame.image.load()
run = True 
while run == True :
    screen.blit(bg_img,(0,0))
    screen.blit(bg_img,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()  