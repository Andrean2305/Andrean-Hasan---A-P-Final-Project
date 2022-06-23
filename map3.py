from pygame import *
from pygame.locals import *
import random
import datetime
import os
os.chdir('C:/Users/Asus/FinalProjectSirJude')

from permainan import * #importing game progress
from tkinter import *
from ALLFUNC import *
from SCREEN2_PLAYING import *
from characterplat import *
from MAP3_COLLIDER import *
from ALLANIMATION import *

from pygame import mixer
from MAP import *

pygame.init()

mixer.init()
mixer.music.load('CHILL.mp3')
mixer.music.set_volume(1)
mixer.music.play(-1)

#load background images

hour = 0
minutes = 0
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

#Shoutout Tech With Tim, i watched his video to understand how to make the platformer game.

spawn = [[400,315],[500,275],[600,230],[850,310]]
spawn_random = random.randint(0,4)
spawn_now = spawn[spawn_random-1]
x = spawn_now[0]
y = spawn_now[1]

poop = character(x,y,64,64)
run = True
timez = False
off = False
pertamax = False
def map3() :
        global nft_coin
        global off
        global pertamax
        global run
        global jam
        global menit
        global sekarang

        poop.map3 = True
        screen.fill((37,19,26))
        screen.blit(back_img,(1200,20))
        screen.blit(floor_img,((1300-600)/2 ,(650-600)/2))
        dx = 0
        dy = 0

        if off == False : 
            
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
            poop.x = spawn_now[0]
            poop.y = spawn_now[1]

            poop.rect1.x = spawn_now[0]
            poop.rect1.y = spawn_now[1]
            parameter(clicks,the_evolve,the_upgrade,the_cost,the_dream,the_level,the_evolving,the_prestige,the_prestige_prize,the_coin,the_damage,the_coin_cost,the_hp,the_coin_percentage,the_damage_cost,the_hp_cost,the_star,the_enemy_hp,the_enemy_at,gacha_coin,creepooper_level,illuminashiet_level,speed_level,chop_level,wood,stone,nft_coin,waktu)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:

                if back_rect.collidepoint(event.pos) :
                    pygame.quit()
                    playingscreen1()    

                if idle_rect.collidepoint(event.pos) :
                    pertamax = True
        
            elif event.type == pygame.MOUSEBUTTONUP:
                poop.trade_wait = None

        if poop.hitung_jalan >= 50:
            poop.hitung_jalan = 0

        list_gerak = ['atas','bawah','kiri','kanan']
        if poop.hitung_jalan == 0 :
            sekarang = list_gerak[(random.randint(0,3))]

        if sekarang == 'atas' :
            poop.plusy = -0.1
            poop.hitung_jalan += 0.1

        elif sekarang == 'bawah' :
            poop.plusy = 0.1
            poop.hitung_jalan += 0.1

        elif sekarang == 'kiri' :
            poop.plusx = -0.1
            poop.hitung_jalan += 0.1

        elif sekarang == 'kanan' :
            poop.plusx = 0.1
            poop.hitung_jalan += 0.1

        for i in collider :
            if i.colliderect(poop.rect1.x + poop.plusx, poop.rect1.y, poop.rect1.width, poop.rect1.height):
                    poop.plusx = 0
                    poop.x += 4
                    poop.hitung_jalan += 5

            if i.colliderect(poop.rect1.x - poop.plusx, poop.rect1.y, poop.rect1.width, poop.rect1.height):
                    poop.plusx = 0
                    poop.x -= 4
                    poop.hitung_jalan += 5

            if i.colliderect(poop.rect1.x , poop.rect1.y + poop.plusy , poop.rect1.width, poop.rect1.height):
                    poop.plusy = 0
                    poop.y += 4
                    poop.hitung_jalan += 5

            if i.colliderect(poop.rect1.x , poop.rect1.y - poop.plusy , poop.rect1.width, poop.rect1.height):
                    poop.plusy = 0
                    poop.y -= 4
                    poop.hitung_jalan += 5

        poop.x += poop.plusx
        poop.y += poop.plusy

        poop.rect1.x += poop.plusx
        poop.rect1.y += poop.plusy

        poop.plusx = 0
        poop.plusy = 0
        poop.draw(screen)

        if pertamax == False :
            pertama()
current_time = datetime.datetime.now()

while run:
    map3()
    pygame.display.update()

current_time = datetime.datetime.now()
waktu = current_time.day*24*60 + current_time.hour*60 + current_time.minute
tahun = current_time.year
bulan = current_time.month
parameter(clicks,the_evolve,the_upgrade,the_cost,the_dream,the_level,the_evolving,the_prestige,the_prestige_prize,the_coin,the_damage,the_coin_cost,the_hp,the_coin_percentage,the_damage_cost,the_hp_cost,the_star,the_enemy_hp,the_enemy_at,gacha_coin,creepooper_level,illuminashiet_level,speed_level,chop_level,stone,wood,nft_coin,waktu,tahun,bulan)
pygame.quit()