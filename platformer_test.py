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

def map1():
    pygame.init()
    mixer.init()
    mixer.music.load('CHILL.mp3')
    mixer.music.set_volume(1)
    mixer.music.play(-1)

    global wood
    global stone
    global the_damage
    global the_hp

    screen_width = 1300
    screen_height = 650

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Poopyz.World')

    #define game variables
    tile_size = 25

    #load background images
    bg_img = pygame.image.load('weather.jpg')
    tree_img = pygame.image.load('tree.png')
    hellow_img = pygame.image.load('hellow.png')
    chop_tree_img = pygame.image.load('clicktree.png')
    plus1_img = pygame.image.load('plus1.png')
    back_img = pygame.image.load('back.png')
    back_rect = back_img.get_rect()
    back_rect.x = 1200
    back_rect.y = 20

    tree_now = pygame.transform.scale(tree_img, (441/1.5, 593/1.5))
    trader_img = pygame.image.load('TRADER.png')
    trader_rect = trader_img.get_rect()
    trader_rect.x = 65
    trader_rect.y = 75

    traded_img = pygame.image.load('TRADED.png')
    # screen.blit(tradenow_img,(565,150))
    # screen.blit(backtrade_img,(375,120))
    tradenow_img = pygame.image.load('tradenow.png')
    tradenow_rect = tradenow_img.get_rect()
    tradenow_rect.x = 565
    tradenow_rect.y = 150

    backtrade_img = pygame.image.load('backtrade.png')
    backtrade_rect = backtrade_img.get_rect()
    backtrade_rect.x = 375
    backtrade_rect.y = 120

    #Shoutout Tech With Tim, i watched his video to understand how to make the platformer game.

    class World():
        def __init__(self, data):
            self.tile_list = []

            #load images
            dirt_img = pygame.image.load('dirt.png')
            grass_img = pygame.image.load('grass.png')
            platform_img = pygame.image.load('platform.png')
            grass1_img = pygame.image.load('grass1.png')
            grass2_img = pygame.image.load('grass-left.png')
            grass3_img = pygame.image.load('grass-right.png')
            flowers_img = pygame.image.load('flowers.png')

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
                    col_count += 1
                row_count += 1 

        def draw(self):
            for tile in self.tile_list:
                screen.blit(tile[0], tile[1])

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
    [0, 0, 7, 7, 7, 7, 7, 7, 7, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4], 
    [0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 5, 2, 2, 2, 2, 6, 4, 4, 4, 4, 4], 
    [0, 0, 0, 0, 0, 4, 5, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 6, 4, 4], 
    [0, 0, 0, 0, 4, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 6, 4, 4], 
    [4, 4, 4, 4, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 6, 4, 4], 
    [2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    world = World(world_data)
    poop = character(6,415,64,64)
    run = True

    while run:
        screen.blit(bg_img, (0, 0))
        screen.blit(tree_now,(850,100))
        screen.blit(hellow_img,(250,50))
        screen.blit(chop_tree_img,(650,300))
        screen.blit(back_img,(1200,20))
        screen.blit(trader_img,(65,75))
        world.draw()

        dx = 0
        dy = 0

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

        if poop.x > screen_width - poop.width - poop.vel:
            pygame.mixer.music.stop()
            fade(1300,650)
            pygame.quit()
            map2()

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
        
        screen.blit(plus1_img,(850,65))
        pygame.draw.rect(screen,(50,205,50),pygame.Rect(895,65,200,30),)
        pygame.draw.rect(screen,(144,238,144),pygame.Rect(898,68,195,24))
        pygame.draw.rect(screen,(0,255,127),pygame.Rect(895,65,poop.length,30))

        if poop.trade :
            screen.blit(traded_img,(300,50))
            screen.blit(tradenow_img,(565,150))
            screen.blit(backtrade_img,(375,120))
            dx = 0

        poop.rect.x += dx
        poop.rect.y += dy

        poop.x += dx
        poop.y += dy

        chopping = tree_now.get_rect()
        chopping.x = 850
        chopping.y = 100

        if poop.chop and poop.length < 200 :
            poop.length += chop_level
        elif poop.length >= 200 :
            pygame.mixer.stop()
            wood += 1
            poop.length = 0
            poop.chop = False
            
            parameter(clicks,the_evolve,the_upgrade,the_cost,the_dream,the_level,the_evolving,the_prestige,the_prestige_prize,the_coin,the_damage,the_coin_cost,the_hp,the_coin_percentage,the_damage_cost,the_hp_cost,the_star,the_enemy_hp,the_enemy_at,gacha_coin,creepooper_level,illuminashiet_level,speed_level,chop_level,wood)
        poop.draw(screen)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if chopping.collidepoint(event.pos)and poop.chop ==False and 590 < poop.x:
                axe_effect = effect("axe.mp3")
                axe_effect.play()
                poop.chop = True
                parameter(clicks,the_evolve,the_upgrade,the_cost,the_dream,the_level,the_evolving,the_prestige,the_prestige_prize,the_coin,the_damage,the_coin_cost,the_hp,the_coin_percentage,the_damage_cost,the_hp_cost,the_star,the_enemy_hp,the_enemy_at,gacha_coin,creepooper_level,illuminashiet_level,speed_level,chop_level,wood)

            if trader_rect.collidepoint(event.pos) and poop.trade == False and 0< poop.x < 250 and 0 < poop.y < 250 :
                poop.trade = True
            
            if backtrade_rect.collidepoint(event.pos) and poop.trade == True :
                poop.trade = False
            
            if tradenow_rect.collidepoint(event.pos) and poop.trade == True and wood >= 150 and poop.trade_wait == False:
                poop.trade_wait = True
                wood -= 150
                the_damage += 15
                the_hp += 100
                trade_effect = effect("trade.mp3")
                trade_effect.play()
                trade_effect.set_volume(0.5)

                parameter(clicks,the_evolve,the_upgrade,the_cost,the_dream,the_level,the_evolving,the_prestige,the_prestige_prize,the_coin,the_damage,the_coin_cost,the_hp,the_coin_percentage,the_damage_cost,the_hp_cost,the_star,the_enemy_hp,the_enemy_at,gacha_coin,creepooper_level,illuminashiet_level,speed_level,chop_level,wood)

            if back_rect.collidepoint(event.pos) :
                pygame.quit()
                playingscreen1()
        
        elif event.type == pygame.MOUSEBUTTONUP:
            poop.trade_wait = False

        pygame.display.update()

    pygame.quit()
    turtle.bye()

map1()