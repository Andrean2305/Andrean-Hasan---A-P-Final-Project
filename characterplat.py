import pygame 
import os

from permainan import * #importing game progress
from tkinter import *
from ALLFUNC import *
from ALLANIMATION import *

os.chdir('C:/Users/Asus/FinalProjectSirJude')
from pygame.locals import *


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
        self.walkbat = 0

        self.time = False

        self.trade = False
        self.trade_wait = False

        self.chop = False
        self.choppin = False
        self.length = 0

        self.stone_animation = False
        self.animation_length = 0 
        self.vel_y = 0
        self.barumuncul = False

        self.burn = False
        self.burn_count = 0
        self.marah = 0

        self.house = False

        self.atas = False
        self.bawah = False
        self.kiri = False
        self.kanan = False
        self.plusx = 0
        self.plusy = 0
        self.hitung_jalan = 0

        self.image = walk_now
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y + 15
        self.rect.width = 33
        self.rect.height = 45

        self.rect1 = self.image.get_rect()
        self.rect1.x = x + 9
        self.rect1.y = y + 60
        self.rect1.width = 28
        self.rect1.height = 15

        self.tree_hitbox = (850, 100,441/1.5, 593/1.5)
        self.map2 = False
        self.map3 = False

        self.news = True
        
    def draw(self,screen):
        if self.map3 == False :
            if self.walkcount + 1 >= 27:
                self.walkcount = 0
            
            if self.burn_count + 1 >= 69:
                self.burn_count = 0

            if self.marah + 1 >= 36:
                self.marah = 0
        
            if self.walkbat +1 >= 27 :
                self.walkbat = 0

            if self.map2 :
                if self.right  and 190 < self.x < 661 and 439 < self.y:
                    screen.blit(bat_right[self.walkbat//3], (self.x,self.y -25))
                    self.walkbat += 1
                elif self.left  and 190 < self.x < 661 and 439 < self.y:
                    screen.blit(bat_left[self.walkbat//3], (self.x,self.y -25))
                    self.walkbat += 1
                elif ((self.x < 190 and self.y < 426) or (self.x > 661 and self.y < 526) or (190 < self.x < 661 and self.y < 426)) :
                    screen.blit(sleep_img,(22*25,18*25))
                else :
                    screen.blit(bat_now,(self.x,self.y -25))

            if self.left and self.burn == False:
                screen.blit(walk_left[self.walkcount//3],(self.x,self.y))
                self.walkcount += 1
                
            elif self.left and self.burn :
                screen.blit(tbl_left[self.marah//3],(self.x,self.y))
                self.marah += 1

            elif self.right and self.burn :
                screen.blit(tbl[self.marah//3],(self.x,self.y))
                self.marah += 1

            elif self.right and self.burn == False:
                screen.blit(walk_right[self.walkcount//3], (self.x,self.y))
    
                self.walkcount += 1
            
            elif self.right == False and self.left == False and self.burn == False:
                screen.blit(walk_now, (self.x,self.y))

            else :
                screen.blit(tbl[self.marah//3],(self.x,self.y))
                self.marah += 1

            if self.burn and self.left == False :
                screen.blit(hinokami_kagura[self.burn_count//3], (self.x+35,self.y+32))
                self.burn_count += 1
            
            elif self.burn and self.left :
                screen.blit(hinokami_kagura_left[self.burn_count//3], (self.x-35,self.y+32))
                self.burn_count += 1
            
            elif self.burn : 
                screen.blit(hinokami_kagura_left[self.burn_count//3], (self.x-35,self.y+32))
                self.burn_count += 1

        elif self.map3 == True:
            if self.walkcount + 1 >= 54:
                self.walkcount = 0

            screen.blit(bounch[self.walkcount//3],(self.x,self.y))
            self.walkcount += 1

        self.rect.x = self.x + 15.5
        self.rect.y = self.y + 15

        self.rect1.x = self.x + 9
        self.rect1.y = self.y + 60

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

tile_size = 25
# screen_width = 1300
# screen_height = 650

# screen = pygame.display.set_mode((screen_width, screen_height))
class World1():

        def __init__(self, data):
            self.tile_list = []
            self.back_list = []
            self.screen_width = 1300
            self.screen_height = 650

            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
            #load images
            dirt_img = pygame.image.load('dirt.png')
            grass_img = pygame.image.load('grass.png')
            platform_img = pygame.image.load('platform.png')
            grass1_img = pygame.image.load('grass1.png')
            grass2_img = pygame.image.load('grass-left.png')
            grass3_img = pygame.image.load('grass-right.png')
            flowers_img = pygame.image.load('flowers.png')
            side_only_img = pygame.image.load('side_only.png')
            down_only_img = pygame.image.load('down_only.png')
            right_down_img = pygame.image.load('right_down.png')
            left_down_img = pygame.image.load('left_down.png')
            left_img = pygame.image.load('left.png')
            sleep_img = pygame.image.load('bat_sleep.png')
            background_img = pygame.image.load('background.png')

            row_count = 0
            for row in data:
                col_count = 0
                for tile in row:
                    if tile == 1:
                        img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect,2)
                        self.tile_list.append(tile)
                    if tile == 2:
                        img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect,2)
                        self.tile_list.append(tile)
                    if tile == 5:
                        img = pygame.transform.scale(grass2_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect,2)   
                        self.tile_list.append(tile)
                    if tile == 6:
                        img = pygame.transform.scale(grass3_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect,2)   
                        self.tile_list.append(tile)
                    if tile == 7:
                        img = pygame.transform.scale(flowers_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect,0)   
                        self.tile_list.append(tile)
                    if tile == 3:
                        img = pygame.transform.scale(platform_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect,1,img_rect.y,img_rect.x)    #1 = for platform
                        self.tile_list.append(tile)
                    if tile == 4:
                        img = pygame.transform.scale(grass1_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect,0)    #0 = no collider/furniture/background
                        self.tile_list.append(tile)
                    if tile == 8:
                        img = pygame.transform.scale(side_only_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect,2)
                        self.tile_list.append(tile)
                    if tile == 9:
                        img = pygame.transform.scale(down_only_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect,2)
                        self.tile_list.append(tile)
                    if tile == 10:
                        img = pygame.transform.scale(right_down_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect,2)
                        self.tile_list.append(tile)
                    if tile == 11:
                        img = pygame.transform.scale(left_down_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect,2)
                        self.tile_list.append(tile)
                    if tile == 12:
                        img = pygame.transform.scale(left_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect,2)
                        self.tile_list.append(tile)
                    if tile == 13:
                        img = pygame.transform.scale(sleep_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect,0)
                        self.tile_list.append(tile)
                    if tile == 15:
                        img = pygame.transform.scale(background_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect,0)
                        self.tile_list.append(tile)
                    col_count += 1
                row_count += 1 

        def draw(self):
            for tile in self.tile_list:
                
                self.screen.blit(tile[0], tile[1])