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

ba1 = pygame.image.load('bat1.png')
ba2 = pygame.image.load('bat2.png')
ba3 = pygame.image.load('bat3.png')
ba4 = pygame.image.load('bat4.png')

bat1 = pygame.transform.scale(ba1, (100,100))
bat2 = pygame.transform.scale(ba2, (100,100))
bat3 = pygame.transform.scale(ba3, (100,100))
bat4 = pygame.transform.scale(ba4, (100,100))

bat11 = pygame.transform.flip(bat1, True, False)
bat22 = pygame.transform.flip(bat2, True, False)
bat33 = pygame.transform.flip(bat3, True, False)
bat44 = pygame.transform.flip(bat4, True, False)

bat_now1 = pygame.image.load('bat.png')
bat_now = pygame.transform.scale(bat_now1, (100,100))

bat_left = [bat1,bat1,bat2,bat2,bat3,bat3,bat4,bat4,bat4]
bat_right = [bat11,bat11,bat22,bat22,bat33,bat33,bat44,bat44,bat44]
sleep1_img = pygame.image.load('bat_sleep.png')
sleep_img = pygame.transform.scale(sleep1_img, (25, 25))

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (16,16,16)

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

        self.trade = False
        self.trade_wait = False
        self.chop = False
        self.choppin = False
        self.length = 0
        self.stone_animation = False
        self.animation_length = 0 
        self.vel_y = 0
        self.barumuncul = False

        self.house = False

        self.image = walk_now
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y + 15
        self.rect.width = 33
        self.rect.height = 45

        self.tree_hitbox = (850, 100,441/1.5, 593/1.5)
        self.map2 = False
        
    def draw(self,screen):
        if self.walkcount + 1 >= 27:
            self.walkcount = 0

        if self.left :
            screen.blit(walk_left[self.walkcount//3],(self.x,self.y))
            if self.map2 and 190 < self.x < 661 and 439 < self.y:
             screen.blit(bat_left[self.walkcount//3],(self.x,self.y -25))
            if self.map2 == True and ((self.x < 190 and self.y < 426) or (self.x > 661 and self.y < 526) or (190 < self.x < 661 and self.y < 426)) :
                screen.blit(sleep_img,(22*25,18*25))

            self.walkcount += 1
            

        elif self.right :
            screen.blit(walk_right[self.walkcount//3], (self.x,self.y))
            if self.map2 and 190 < self.x < 661 and 439 < self.y:
                screen.blit(bat_right[self.walkcount//3], (self.x,self.y -25))
            if self.map2 == True and ((self.x < 190 and self.y < 426) or (self.x > 661 and self.y < 526) or (190 < self.x < 661 and self.y < 426)) :
                screen.blit(sleep_img,(22*25,18*25))
 
            self.walkcount += 1
           
        else:
            screen.blit(walk_now, (self.x,self.y))
            if self.map2 and 190 < self.x < 661 and 439 < self.y :
                screen.blit(bat_now, (self.x,self.y -25))
            if self.map2 == True and ((self.x < 190 and self.y < 426) or (self.x > 661 and self.y < 526) or (190 < self.x < 661 and self.y < 426)) :
                screen.blit(sleep_img,(22*25,18*25))

        # self.hitbox = (self.x + 15.5, self.y,36,60)
        self.rect.x = self.x + 15.5
        self.rect.y = self.y + 15
        # pygame.draw.rect(screen, (255, 255, 255), self.tree_hitbox, 2)
poop = character(6,415,64,64) 

# screen = pygame.display.set_mode((1300, 650))
class inventory():
    def __init__(self,img):
        self.countdowns = 0
        self.baba = 1300//2
        self.x = 1300//2
        self.y = 0
        self.img = img

        self.muncul = False
        self.screen = pygame.display.set_mode((1300, 650))
    
    def tulisan(self,size,color,a,b,c,name):
        if self.muncul == True :
            self.screen.blit(self.img, (self.x-145, self.y-20))

            font = pygame.font.SysFont('Apple II ALT Pro', size)
            font1 = pygame.font.SysFont('Apple II ALT Pro', size+20)

            text = font1.render(f'{name}', True, white)
            text1 = font.render(f'Level : {a}', True, color)
            text2 = font.render(f'Movement Speed : {b}', True, color)
            text3 = font.render(f'Chopping Speed : {c}', True, color)

            textRect = text.get_rect()
            textRect.center = (self.x,self.y +340)
            
            textRect1 = text1.get_rect()
            textRect1.center = (self.x,self.y+210)

            textRect2 = text2.get_rect()
            textRect2.center = (self.x,self.y+250)

            textRect3 = text3.get_rect()
            textRect3.center = (self.x,self.y+290)

            self.screen.blit(text1, textRect1)
            self.screen.blit(text2, textRect2)
            self.screen.blit(text3, textRect3)
            self.screen.blit(text, textRect)
    
