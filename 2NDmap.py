from pygame import *
from pygame.locals import *

import os
os.chdir('C:/Users/Asus/FinalProjectSirJude')

from permainan import * #importing game progress
from tkinter import *
from ALLFUNC import *
from SCREEN2_PLAYING import *
from characterplat import *
from MAP import *

from pygame import mixer


pygame.init()

mixer.init()
mixer.music.load('CHILL.mp3')
mixer.music.set_volume(1)
mixer.music.play(-1)

poop2 = character(6,415,64,64)
world2 = World1(world2_data)
back2 = World1(back2_data)
run = True

while run:
    def map2():
        global run
        global wood
        global stone
        screen.blit(bg_img, (0, 0))
        screen.blit(back_img,(1200,20))
        back2.draw()
        screen.blit(stone_img,(stone_rect.x,stone_rect.y))

        if poop2.house :
            screen.blit(house_img,(800,0))

        world2.draw()
        poop2.map2 = True
        dx = 0
        dy = 0
        screen.blit(build_img,(build_rect.x,build_rect.y))

        keys = pygame.key.get_pressed()


        keys = pygame.key.get_pressed()

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and poop2.x > poop2.vel:
            dx -= (poop2.vel + 0.7 + speed_level)
            poop2.left = True
            poop2.right = False

        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and poop2.x < screen_width - poop2.width - poop2.vel:
            dx += (poop2.vel +0.2 +speed_level)
            poop2.right = True
            poop2.left = False

        else :
            poop2.right = False
            poop2.left = False
            poop2.walkcount = 0
        
        if (keys[pygame.K_w]) and poop2.jump == False:
            poop2.vel_y = -10
            poop2.jump = True
            noob_effect = effect("jump.wav")
            noob_effect.play()

        if (keys[pygame.K_w]) == False:
            poop2.jump = False

        if (keys[pygame.K_SPACE]) :
            poop2.burn = True 

        if (keys[pygame.K_SPACE]) ==False :
            poop2.burn = False    
            poop2.burn_count = 0

        poop2.vel_y += 0.35
        if poop2.vel_y > 2.5:
            poop2.vel_y = 2.5   
        dy += poop2.vel_y

        for tile in world2.tile_list:
            if tile[2] == 2 :
                if tile[1].colliderect(poop2.rect.x + dx +1, poop2.rect.y, poop2.rect.width, poop2.rect.height):
                    dx = -0

                if tile[1].colliderect(poop2.rect.x +dx -1, poop2.rect.y, poop2.rect.width, poop2.rect.height):
                    dx = 0
                    if keys[pygame.K_RIGHT] and poop2.x < screen_width - poop2.width - poop2.vel:
                        dx += (poop2.vel + 0.7 + speed_level)
                        poop2.right = True
                        poop2.left = False

                if tile[1].colliderect(poop2.rect.x, poop2.rect.y + dy, poop2.rect.width, poop2.rect.height):

                    if poop2.vel_y < 0 :                      #tidak bisa tembus ketika lompat
                        dy = tile[1].bottom - poop2.rect.top
                        poop2.vel_y = 0

                    elif poop2.vel_y >= 0 :                   #stay on top of the platform while gravity pulling the poop2yz
                        dy = tile[1].top - poop2.rect.bottom
                        poop2.vel_y = 0

            if tile[2] == 1 :
                if tile[1].colliderect(poop2.rect.x, poop2.rect.y +dy+0.5 , poop2.rect.width, poop2.rect.height):
                    if poop2.rect.bottom    <= tile[1].top <= poop2.rect.bottom + 2 :                         #stay on top of the platform while gravity pulling the poop2yz
                        dy = 0
                        poop2.y = tile[1].top - 61
                        dy = 0

        if poop2.rect.bottom > screen_height:
            poop2.rect.bottom = screen_height
            # poop2.y = 0
            dy = 0
        
        poop2.rect.x += dx
        poop2.rect.y += dy

        poop2.x += dx
        poop2.y += dy

        if poop2.chop and poop2.length < 200 :
            poop2.length += chop_level
        elif poop2.length >= 200 :
            pygame.mixer.stop()
            stone += 1
            poop2.length = 0
            poop2.chop = False
            poop2.stone_animation = True
            parameter(clicks,the_evolve,the_upgrade,the_cost,the_dream,the_level,the_evolving,the_prestige,the_prestige_prize,the_coin,the_damage,the_coin_cost,the_hp,the_coin_percentage,the_damage_cost,the_hp_cost,the_star,the_enemy_hp,the_enemy_at,gacha_coin,creepoop2er_level,illuminashiet_level,speed_level,chop_level,wood,stone)
        
        if poop2.stone_animation and poop2.animation_length < 500 :
            poop2.animation_length += 10
            screen.blit(plus_one_stone_img,(poop2.x - 20,poop2.y))
        
        if poop2.animation_length >= 500 :
            poop2.stone_animation = False
            poop2.animation_length = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if stone_rect.collidepoint(event.pos)and poop2.chop ==False and stone_rect.x - 50 < poop2.x < stone_rect.x + 160 and stone_rect.y < poop2.y:
                    axe_effect = effect("axe.mp3")
                    axe_effect.play()
                    poop2.chop = True
                    parameter(clicks,the_evolve,the_upgrade,the_cost,the_dream,the_level,the_evolving,the_prestige,the_prestige_prize,the_coin,the_damage,the_coin_cost,the_hp,the_coin_percentage,the_damage_cost,the_hp_cost,the_star,the_enemy_hp,the_enemy_at,gacha_coin,creepoop2er_level,illuminashiet_level,speed_level,chop_level,wood,stone)

                if build_rect.collidepoint(event.pos)and poop2.house ==False and wood >= 200 and stone >= 200:
                    poop2.house = True
                    wood -= 200
                    stone -= 200
                    parameter(clicks,the_evolve,the_upgrade,the_cost,the_dream,the_level,the_evolving,the_prestige,the_prestige_prize,the_coin,the_damage,the_coin_cost,the_hp,the_coin_percentage,the_damage_cost,the_hp_cost,the_star,the_enemy_hp,the_enemy_at,gacha_coin,creepoop2er_level,illuminashiet_level,speed_level,chop_level,wood,stone)

                if back_rect.collidepoint(event.pos) :
                    pygame.quit()
                    playingscreen1()
            
            elif event.type == pygame.MOUSEBUTTONUP:
                poop2.trade_wait = False

        pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)
        pygame.draw.rect(screen,(255,0,0),poop2.rect,2)

        poop2.draw(screen)
    map2()
    pygame.display.update()

pygame.quit()

