import pygame 
import os

from permainan import * #importing game progress
from tkinter import *
from ALLFUNC import *
from SCREEN2_PLAYING import *

os.chdir('C:/Users/Asus/FinalProjectSirJude')
from pygame.locals import *

right1 = pygame.image.load('mrpoopyz.png')
right2 = pygame.image.load('mrpoopyz2.png')
right3 = pygame.image.load('mrpoopyz3.png')

left1 = pygame.transform.flip(right1, True, False)
left2 = pygame.transform.flip(right2, True, False)
left3 = pygame.transform.flip(right3, True, False)

walk_now = pygame.image.load('mrpoopyz.png')

walk_left = [left1,left1,left1,left2,left2,left2,left3,left3,left3]
walk_right = [right1,right1,right1,right2,right2,right2,right3,right3,right3]

class character():
    def __init__(self,x,y,width,heigth):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = heigth
        self.vel = 0.7
        self.jump = False
        self.jumpcount = 5
        self.left = False
        self.right = False
        self.walkcount = 0

        self.chop = False
        self.choppin = False
        self.length = 0

        self.vel_y = 0

        self.image = walk_now
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 
        self.rect.width = 33
        self.rect.height = 60

        self.tree_hitbox = (850, 100,441/1.5, 593/1.5)
    
    def draw(self,screen):
        if self.walkcount + 1 >= 27:
            self.walkcount = 0

        if self.left :
            screen.blit(walk_left[self.walkcount//3],(self.x,self.y))
            self.walkcount += 1
            

        elif self.right :
            screen.blit(walk_right[self.walkcount//3], (self.x,self.y))
            self.walkcount += 1
           
        else:
            screen.blit(walk_now, (self.x,self.y))
        # self.hitbox = (self.x + 15.5, self.y,36,60)
        self.rect.x = self.x + 15.5
        self.rect.y = self.y
        # pygame.draw.rect(screen, (255, 255, 255), self.tree_hitbox, 2)
poop = character(6,415,64,64) 
