from multiprocessing.pool import TERMINATE
from re import A
from pygame import *
from pygame.locals import *

import os
import random
os.chdir('C:/Users/Asus/FinalProjectSirJude')

from permainan import * #importing game progress
from tkinter import *
from ALLFUNC import *
from SCREEN2_PLAYING import *
from characterplat import *
from MAP import *
from MAP3_COLLIDER import *
from ALLANIMATION import *
import datetime
import webbrowser

from pygame import mixer

pygame.init()
mixer.init()

mixer.music.load('CHILL.mp3')
mixer.music.set_volume(0.5)
mixer.music.play(-1)
# mixer.music.load('CHILL.mp3')
# mixer.music.set_volume(0.5)
# mixer.music.play(-1)

screen_width = 1300
screen_height = 650

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Poopyz.World')

world1 = World1(world1_data)
poop = character(6,415,64,64)
run = True
keys = pygame.key.get_pressed()


poop = character(6,415,64,64)
world2 = World1(world2_data)
back2 = World1(back2_data)

home = False
maps1 = True
maps2 = False
maps3 = False
news = True

spawn = [[400,315],[500,275],[600,230],[850,310]]
spawn_random = random.randint(0,4)
spawn_now = spawn[spawn_random-1]
x = spawn_now[0]
y = spawn_now[1]

poop3 = character(x,y,64,64)
font = pygame.font.SysFont("Apple II ALT NEG Pro", 60)
timez = False
off = False
pertamax = False
current_time = datetime.datetime.now()

def pertama():
    screen.blit(idle_img,((1300-500)/2 ,(650-450)/2))

    if jam < 4 :
        text = font.render(f'You"ve been gone for', True, (255,255,255))
        text1 = font.render(f'{jam} Hours     {menit} Minutes', True, black)

        textRect = text.get_rect()
        textRect.center = (655,510)
        
        textRect1 = text1.get_rect()
        textRect1.center = (655,560)

        screen.blit(text1, textRect1)
        screen.blit(text, textRect)

    else :
        text = font.render(f'You"ve been gone for', True, (255,255,255))
        text1 = font.render(f'More than 4 hours T_T', True, black)

        textRect = text.get_rect()
        textRect.center = (655,510)

        textRect1 = text1.get_rect()
        textRect1.center = (655,560)

        screen.blit(text, textRect)
        screen.blit(text1, textRect1)
def sembur():
    keys = pygame.key.get_pressed()

    if (keys[pygame.K_SPACE]) :
        poop.burn = True 

    if (keys[pygame.K_SPACE]) == False :
        poop.burn = False

def gerak() :
    global news
    dx = 0
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

    if (keys[pygame.K_w]) and poop.jump == False:
        poop.vel_y = -10
        poop.jump = True
        noob_effect = effect("jump.wav")
        noob_effect.play()

    if (keys[pygame.K_w]) == False:
        poop.jump = False

    if news == True :
        screen.blit(new,(200,200))
        if (keys[pygame.K_v]):
            print("a")
            news = False

        elif keys[pygame.K_m]:
            webbrowser.open(r"https://decentralizedcreator.com/buy-matic-in-metamask-transak-and-moonpay/")
            news = False
        
        elif keys[pygame.K_i]:
            webbrowser.open(r"https://www.instagram.com/the_poopyz/")
            news = False
    return dx


# def home_screens() :
#     global home
#     global maps1 
#     global maps2
#     global maps3

#     screen.blit(home_screen,(0, 0))

def map1 () :
    global wood
    global the_damage
    global the_hp
    global run
    global home
    global maps1 
    global maps2
    global maps3
    global news
    global keys

    mixer.music.unpause()
    screen.blit(bg_img, (0, 0))
    screen.blit(tree_now,(850,100))
    screen.blit(hellow_img,(250,50))
    screen.blit(chop_tree_img,(650,300))
    screen.blit(back_img,(1200,20))
    screen.blit(trader_img,(65,75))
    world1.draw()
    
    dy = 0
    dx = gerak()

    sembur()

    poop.vel_y += 0.35
    if poop.vel_y > 2.5:
        poop.vel_y = 2.5   
    dy += poop.vel_y

    for tile in world1.tile_list:
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
    
    if news :
        dx = 0
        dy = 0

    poop.rect.x += dx
    poop.rect.y += dy

    poop.x += dx
    poop.y += dy

    if poop.x > screen_width - poop.width - poop.vel:
        pygame.mixer.music.pause()
        fade(1300,650)
        maps2 = True
        maps1 = False
        poop.x = 6
        poop.y = 415

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
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
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

def map2():
        global run
        global wood
        global stone
        global home
        global maps1
        global maps2
        global maps3

        mixer.music.unpause()

        screen.blit(bg_img, (0, 0))
        screen.blit(back_img,(1200,20))
        back2.draw()
        screen.blit(stone_img,(stone_rect.x,stone_rect.y))

        if poop.house :
            screen.blit(house_img,(800,0))

        world2.draw()
        poop.map2 = True
        dx = 0
        dy = 0
        screen.blit(build_img,(build_rect.x,build_rect.y))

        keys = pygame.key.get_pressed()

        dx = gerak()
        sembur()

        if poop.x < poop.vel :
            pygame.mixer.music.pause()
            fade(1300,650)
            maps2 = False
            maps1 = True
            poop.map2 = False
            poop.x = 1189
            poop.y = 440

        poop.vel_y += 0.35
        if poop.vel_y > 2.5:
            poop.vel_y = 2.5   
        dy += poop.vel_y

        for tile in world2.tile_list:
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

                    if poop.vel_y < 0 :                      #tidak bisa tembus ketika lompat
                        dy = tile[1].bottom - poop.rect.top
                        poop.vel_y = 0

                    elif poop.vel_y >= 0 :                   #stay on top of the platform while gravity pulling the poopyz
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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
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
                
                if house_img_rect.collidepoint(event.pos) and poop.house and poop.x > 875 and poop.y > 180  :
                    pygame.mixer.music.pause()
                    fade(1300,650)
                    maps2 = False
                    maps3 = True
            
            elif event.type == pygame.MOUSEBUTTONUP:
                poop.trade_wait = False

        pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)
        pygame.draw.rect(screen,(255,0,0),house_img_rect,2)

        poop.draw(screen)

def map3() :
    global nft_coin
    global off
    global pertamax
    global run
    global jam
    global menit
    global sekarang
    global current_time
    global bulan
    global tahun
    global waktu
    global home
    global maps3
    global maps2
    global maps1

    pygame.mixer.music.unpause()
    poop3.map3 = True
    screen.fill((37,19,26))
    screen.blit(back_img,(1200,20))
    screen.blit(floor_img,((1300-600)/2 ,(650-600)/2))

    if off == False : 
        current_time = datetime.datetime.now()
        if current_time.month == bulan :
            bulan_apa_sekarang = 0
        else :
            bulan_apa_sekarang = (waktu//(24*60))*24*60
        
        if current_time.year == tahun :
            tahun_apa_sekarang = 0
        else : 
            tahun_apa_sekarang = 365*24*60
            bulan_apa_sekarang = 0
        calculate = (tahun_apa_sekarang + bulan_apa_sekarang + current_time.day*24*60 + current_time.hour*60 + current_time.minute) - waktu
        off = True
        jam = calculate//60
        menit = calculate - jam*60 
        (waktu//(24*60))

    if wall11.colliderect(poop.rect1):
        nft_coin += 1
        spawn_random = random.randint(0,4)
        spawn_now = spawn[spawn_random-1]
        poop3.x = spawn_now[0]
        poop3.y = spawn_now[1]

        poop3.rect1.x = spawn_now[0]
        poop3.rect1.y = spawn_now[1]
        parameter(clicks,the_evolve,the_upgrade,the_cost,the_dream,the_level,the_evolving,the_prestige,the_prestige_prize,the_coin,the_damage,the_coin_cost,the_hp,the_coin_percentage,the_damage_cost,the_hp_cost,the_star,the_enemy_hp,the_enemy_at,gacha_coin,creepooper_level,illuminashiet_level,speed_level,chop_level,wood,stone,nft_coin,waktu)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            current_time = datetime.datetime.now()
            waktu = current_time.day*24*60 + current_time.hour*60 + current_time.minute
            tahun = current_time.year
            bulan = current_time.month
            parameter(clicks,the_evolve,the_upgrade,the_cost,the_dream,the_level,the_evolving,the_prestige,the_prestige_prize,the_coin,the_damage,the_coin_cost,the_hp,the_coin_percentage,the_damage_cost,the_hp_cost,the_star,the_enemy_hp,the_enemy_at,gacha_coin,creepooper_level,illuminashiet_level,speed_level,chop_level,stone,wood,nft_coin,waktu,tahun,bulan)
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:

            if back_rect.collidepoint(event.pos) :
                current_time = datetime.datetime.now()
                waktu = current_time.day*24*60 + current_time.hour*60 + current_time.minute
                tahun = current_time.year
                bulan = current_time.month
                parameter(clicks,the_evolve,the_upgrade,the_cost,the_dream,the_level,the_evolving,the_prestige,the_prestige_prize,the_coin,the_damage,the_coin_cost,the_hp,the_coin_percentage,the_damage_cost,the_hp_cost,the_star,the_enemy_hp,the_enemy_at,gacha_coin,creepooper_level,illuminashiet_level,speed_level,chop_level,stone,wood,nft_coin,waktu,tahun,bulan)  
                pygame.mixer.music.pause()
                pertamax = False
                off = False
                fade(1300,650)
                maps3 = False
                maps2 = True
            if idle_rect.collidepoint(event.pos) :
                pertamax = True
    
        elif event.type == pygame.MOUSEBUTTONUP:
            poop3.trade_wait = None

    if poop3.hitung_jalan >= 50:
        poop3.hitung_jalan = 0

    list_gerak = ['atas','bawah','kiri','kanan']
    if poop3.hitung_jalan == 0 :
        sekarang = list_gerak[(random.randint(0,3))]

    if sekarang == 'atas' :
        poop3.plusy = -0.1
        poop3.hitung_jalan += 0.1

    elif sekarang == 'bawah' :
        poop3.plusy = 0.1
        poop3.hitung_jalan += 0.1

    elif sekarang == 'kiri' :
        poop3.plusx = -0.1
        poop3.hitung_jalan += 0.1

    elif sekarang == 'kanan' :
        poop3.plusx = 0.1
        poop3.hitung_jalan += 0.1

    for i in collider :
        if i.colliderect(poop3.rect1.x + poop3.plusx, poop3.rect1.y, poop3.rect1.width, poop3.rect1.height):
                poop3.plusx = 0
                poop3.x += 4
                poop3.hitung_jalan += 5

        if i.colliderect(poop3.rect1.x - poop3.plusx, poop3.rect1.y, poop3.rect1.width, poop3.rect1.height):
                poop3.plusx = 0
                poop3.x -= 4
                poop3.hitung_jalan += 5

        if i.colliderect(poop3.rect1.x , poop3.rect1.y + poop3.plusy , poop3.rect1.width, poop3.rect1.height):
                poop3.plusy = 0
                poop3.y += 4
                poop3.hitung_jalan += 5

        if i.colliderect(poop3.rect1.x , poop3.rect1.y - poop3.plusy , poop3.rect1.width, poop3.rect1.height):
                poop3.plusy = 0
                poop3.y -= 4
                poop3.hitung_jalan += 5

    poop3.x += poop3.plusx
    poop3.y += poop3.plusy

    poop3.rect1.x += poop3.plusx
    poop3.rect1.y += poop3.plusy

    poop3.plusx = 0
    poop3.plusy = 0
    poop3.draw(screen)

    if pertamax == False :
        pertama()

while run:
    # if home :
    #     home_screens()

    if maps1 :
        map1()

    elif maps2:
        map2()
    
    elif maps3 :
        map3()

    pygame.display.update()

pygame.quit()
turtle.bye()
