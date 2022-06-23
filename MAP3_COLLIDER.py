from pygame import *
from pygame.locals import *

from ALLFUNC import *
import pygame
import os
os.chdir('C:/Users/Asus/FinalProjectSirJude')
pygame.init()

floor_img1 = pygame.image.load('dungeon_nft.png')
floor_img = pygame.transform.scale(floor_img1,(600,600))

floor_img_1 = pygame.transform.scale(floor_img1,(10,300))
wall = floor_img_1.get_rect()
wall.x = 375
wall.y = 150

floor_img_2 = pygame.transform.scale(floor_img1,(10,300))
wall2 = floor_img_2.get_rect()
wall2.x = 915
wall2.y = 150

floor_img_2 = pygame.transform.scale(floor_img1,(700,100))
wall3 = floor_img_2.get_rect()
wall3.x = 300
wall3.y = 185

floor_img_2 = pygame.transform.scale(floor_img1,(75,100))
wall4 = floor_img_2.get_rect()
wall4.x = 500
wall4.y = 222

floor_img_2 = pygame.transform.scale(floor_img1,(75,100))
wall5 = floor_img_2.get_rect()
wall5.x = 725
wall5.y = 222

floor_img_2 = pygame.transform.scale(floor_img1,(75,250))
wall6 = floor_img_2.get_rect()
wall6.x = 500
wall6.y = 361

floor_img_2 = pygame.transform.scale(floor_img1,(75,250))
wall7 = floor_img_2.get_rect()
wall7.x = 725
wall7.y = 361

floor_img_2 = pygame.transform.scale(floor_img1,(240,75))
wall8 = floor_img_2.get_rect()
wall8.x = 370
wall8.y = 400

floor_img_2 = pygame.transform.scale(floor_img1,(240,75))
wall9 = floor_img_2.get_rect()
wall9.x = 685
wall9.y = 400

floor_img_2 = pygame.transform.scale(floor_img1,(700,100))
wall10 = floor_img_2.get_rect()
wall10.x = 300
wall10.y = 585

floor_img_2 = pygame.transform.scale(floor_img1,(75,40))
wall11 = floor_img_2.get_rect()
wall11.x = 610
wall11.y = 435

collider = [wall,wall2,wall3,wall4,wall5,wall6,wall7,wall8,wall9,wall10,wall11]