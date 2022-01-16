from pygame import *
from pygame.locals import *

import os
os.chdir('C:/Users/Asus/FinalProjectSirJude')

from permainan import * #importing game progress
from tkinter import *
from ALLFUNC import *
from SCREEN2_PLAYING import *
from characterplat import *

from pygame import mixer

def map2():
    pygame.init()

    mixer.init()
    mixer.music.load('CHILL.mp3')
    mixer.music.set_volume(1)
    mixer.music.play(-1)

    global wood
    global stone
    global the_damage
    global the_hp


    clock = pygame.time.Clock()
    screen_width = 1300
    screen_height = 650

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Poopyz.World')

    #define game variables
    tile_size = 25

    #load background images
    bg_img = pygame.image.load('weather.jpg')
    stone_img = pygame.image.load('stone.png')
    # stone_img = pygame.transform.scale(stone_img1, (500, 500))
    stone_rect = stone_img.get_rect()
    stone_rect.x = 12*25
    stone_rect.y = 20*25

    build_img = pygame.image.load('build.png')

    build_rect = build_img.get_rect()
    build_rect.x = 35
    build_rect.y = 3*25

    plus_one_stone_img = pygame.image.load('plus1_stone.png')

    house1_img = pygame.image.load('house.png')
    house_img = pygame.transform.scale(house1_img, (500, 500))

    back_img = pygame.image.load('back.png')
    back_rect = back_img.get_rect()
    back_rect.x = 1200
    back_rect.y = 20

    #Shoutout Tech With Tim, i watched his video to understand how to make the platformer game.

    class World():

        def __init__(self, data):
            self.tile_list = []
            self.back_list = []

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
                screen.blit(tile[0], tile[1])

    back_data = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0, 0, 0,  0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 15,  15, 15, 15, 15, 15, 15, 15, 15, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 15, 15, 15, 15, 15, 15, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 15, 15, 15, 15, 15, 15, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 15, 15, 15, 15, 15, 15, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    world_data = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 7, 7, 7, 7, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 7, 7, 7, 7, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 
    [0, 0, 0, 0, 0, 4, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 0, 0], 
    [0, 0, 0, 0, 4, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 9, 9, 9,10, 0, 0, 4, 4], 
    [4, 4, 4, 4, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 6, 4, 4], 
    [2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 9, 9, 9,10, 0, 0, 7, 4, 4, 4, 4, 4, 7, 12, 1, 2, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 5, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 12, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 0, 0, 0, 0, 0, 0, 0, 0, 5, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 0, 0, 0, 0, 0, 0, 0, 0, 12, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 4, 4, 4, 4, 4, 4, 4, 4, 12, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    poop = character(6,415,64,64)
    world = World(world_data)
    back = World(back_data)
    run = True

    while run:
        screen.blit(bg_img, (0, 0))
        screen.blit(back_img,(1200,20))
        back.draw()
        screen.blit(stone_img,(stone_rect.x,stone_rect.y))

        if poop.house :
            screen.blit(house_img,(800,0))

        world.draw()
        poop.map2 = True
        dx = 0
        dy = 0
        screen.blit(build_img,(build_rect.x,build_rect.y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and poop.x > poop.vel:
            dx -= (poop.vel + 0.7 + speed_level)
            poop.left = True
            poop.right = False

        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and poop.x < screen_width - poop.width - poop.vel:
            dx += (poop.vel +0.2 +speed_level)
            poop.right = True
            poop.left = False

        else :
            poop.right = False
            poop.left = False
            poop.walkcount = 0
        

        # if keys[pygame.K_UP] and y > vel:                             #GOD MODE / GameMaster MODE
            #     y -= vel                                          
            
            # if keys[pygame.K_DOWN] and y < screen_height - height - vel:
            #     y += vel


        if (keys[pygame.K_SPACE] or keys[pygame.K_w]) and poop.jump == False:
            poop.vel_y = -10
            poop.jump = True
            noob_effect = effect("jump.wav")
            noob_effect.play()

        if (keys[pygame.K_SPACE] or keys[pygame.K_w]) == False:
            poop.jump = False
            
        
        poop.vel_y += 0.35
        if poop.vel_y > 2.5:
            poop.vel_y = 2.5   
        dy += poop.vel_y

        for tile in world.tile_list:
            if tile[2] == 2 :
                if tile[1].colliderect(poop.rect.x + dx +1, poop.rect.y, poop.rect.width, poop.rect.height):
                    dx = -0

                if tile[1].colliderect(poop.rect.x +dx -1, poop.rect.y, poop.rect.width, poop.rect.height):
                    dx = 0
                    if keys[pygame.K_RIGHT] and poop.x < screen_width - poop.width - poop.vel:
                        dx += (poop.vel + 0.7 + speed_level)
                        poop.right = True
                        poop.left = False

                if tile[1].colliderect(poop.rect.x, poop.rect.y + dy, poop.rect.width, poop.rect.height):

                    if poop.vel_y < 0:                      #tidak bisa tembus ketika lompat
                        dy = tile[1].bottom - poop.rect.top
                        poop.vel_y = 0

                    elif poop.vel_y >= 0:                   #stay on top of the platform while gravity pulling the poopyz
                        dy = tile[1].top - poop.rect.bottom
                        poop.vel_y = 0

            if tile[2] == 1 :
                if tile[1].colliderect(poop.rect.x, poop.rect.y +dy+0.5 , poop.rect.width, poop.rect.height):
                    if poop.rect.bottom    <= tile[1].top <= poop.rect.bottom + 2 :                         #stay on top of the platform while gravity pulling the poopyz
                        dy = 0
                        poop.y = tile[1].top - 61
                        dy = 0

        if poop.rect.bottom > screen_height:
            poop.rect.bottom = screen_height
            # poop.y = 0
            dy = 0
        

        poop.rect.x += dx
        poop.rect.y += dy

        poop.x += dx
        poop.y += dy

        if poop.chop and poop.length < 200 :
            poop.length += chop_level
        elif poop.length >= 200 :
            pygame.mixer.stop()
            stone += 1
            poop.length = 0
            poop.chop = False
            poop.stone_animation = True
            parameter(clicks,the_evolve,the_upgrade,the_cost,the_dream,the_level,the_evolving,the_prestige,the_prestige_prize,the_coin,the_damage,the_coin_cost,the_hp,the_coin_percentage,the_damage_cost,the_hp_cost,the_star,the_enemy_hp,the_enemy_at,gacha_coin,creepooper_level,illuminashiet_level,speed_level,chop_level,wood,stone)
        
        if poop.stone_animation and poop.animation_length < 500 :
            poop.animation_length += 10
            screen.blit(plus_one_stone_img,(poop.x - 20,poop.y))
        
        if poop.animation_length >= 500 :
            poop.stone_animation = False
            poop.animation_length = 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            if stone_rect.collidepoint(event.pos)and poop.chop ==False and stone_rect.x - 50 < poop.x < stone_rect.x + 160 and stone_rect.y < poop.y:
                axe_effect = effect("axe.mp3")
                axe_effect.play()
                poop.chop = True
                parameter(clicks,the_evolve,the_upgrade,the_cost,the_dream,the_level,the_evolving,the_prestige,the_prestige_prize,the_coin,the_damage,the_coin_cost,the_hp,the_coin_percentage,the_damage_cost,the_hp_cost,the_star,the_enemy_hp,the_enemy_at,gacha_coin,creepooper_level,illuminashiet_level,speed_level,chop_level,wood,stone)

            if build_rect.collidepoint(event.pos)and poop.house ==False and wood >= 200 and stone >= 200:
                poop.house = True
                wood -= 200
                stone -= 200
                parameter(clicks,the_evolve,the_upgrade,the_cost,the_dream,the_level,the_evolving,the_prestige,the_prestige_prize,the_coin,the_damage,the_coin_cost,the_hp,the_coin_percentage,the_damage_cost,the_hp_cost,the_star,the_enemy_hp,the_enemy_at,gacha_coin,creepooper_level,illuminashiet_level,speed_level,chop_level,wood,stone)

            if back_rect.collidepoint(event.pos) :
                pygame.quit()
                playingscreen1()
        
        elif event.type == pygame.MOUSEBUTTONUP:
            poop.trade_wait = False

        pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)
        pygame.draw.rect(screen,(255,0,0),poop.rect,2)

        poop.draw(screen)
        pygame.display.update()

    pygame.quit()