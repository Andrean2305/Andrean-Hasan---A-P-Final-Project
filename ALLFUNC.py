import turtle #turtle module just to make background and importing image
import pygame

from permainan import * #importing game progress
from tkinter import *
from pygame import *

from MAP3_COLLIDER import *

def lagu(a):    #For making the music background
    music = (f'C:/Users/Asus/FinalProjectsirJude/{a}')
    return music

def effect(a):  #For making sound effect
    c = lagu(a)
    sound_effect = mixer.Sound(c)
    return sound_effect 

def tophoto(a,b,c): #Using the image and make it go to certain destination
    turtle.speed(0)
    a.penup()
    a.goto(b,c)

def towrite(a,b,c,d,e,f,g,h = ""):  #To write something
    turtle.speed(0)
    a.color(b) #color of the font
    a.penup()
    a.goto(c,d) #location of the font
    a.hideturtle()
    a.ht()
    if g != 0 and g != 1:
        a.write(f"{g}: {(round(e,2))}{h}",align ="center", font = ("Apple II ALT Pro",f,"bold"))
    elif g == 0 :
        a.write(e)
    if g == 1 :
        a.write(e,align = "center", font = ("Apple II ALT PRO",f,"bold"))

# parameter(clicks,the_evolve,the_upgrade,the_cost,the_dream,the_level,the_evolving,the_prestige,the_prestige_prize,the_coin,the_damage,the_coin_cost,the_hp,the_coin_percentage,the_damage_cost,the_hp_cost,the_star,the_enemy_hp,the_enemy_at,gacha_coin,creepooper_level,illuminashiet_level,speed_level,chop_level,wood,stone,nft_coin,waktu)
def parameter(a ,b ,c ,d ,e ,f ,g ,h ,i ,j ,k ,l ,m ,n ,o ,p ,q ,r = the_enemy_hp,s = the_enemy_at,t = gacha_coin,u = creepooper_level,v = illuminashiet_level,w = speed_level,x = chop_level,y= wood,z = stone, aa = nft_coin, ab = waktu,ac = tahun , ad = bulan):
    save = open("permainan.py","w")
    save.write("clicks= " + str(a) + '\n')
    save.write("the_evolve= " +str(b) + '\n')
    save.write("the_upgrade= " +str(c) + '\n')
    save.write("the_cost= " +str(d) + '\n')
    save.write("the_dream= " +str(e) + '\n')
    save.write("the_level= " +str(f) + '\n')
    save.write("the_evolving= " +str(g) + '\n')
    save.write("the_prestige= " +str(h) + '\n')
    save.write("the_prestige_prize= " +str(i) + '\n')
    save.write("the_coin= " + str(j)  +'\n')
    save.write("the_damage= " + str(k) + '\n')
    save.write("the_hp= " + str(m) + '\n')
    save.write("the_coin_cost= "+ str(l) + '\n')
    save.write("the_coin_percentage= "+ str(n) + '\n')
    save.write("the_damage_cost= "+ str(o) + '\n')
    save.write("the_hp_cost= "+ str(p) + '\n')
    save.write("the_star= "+ str(q) + '\n')
    save.write("the_enemy_hp= "+ str(r) + '\n')
    save.write("the_enemy_at= "+ str(s) + '\n')
    save.write("gacha_coin= "+ str(t) + '\n')
    save.write("creepooper_level= "+ str(u) + '\n')
    save.write("illuminashiet_level= "+ str(v) + '\n')
    save.write("speed_level= "+ str(w) + '\n')
    save.write("chop_level= "+ str(x) + '\n')
    save.write("wood= "+ str(y) + '\n')
    save.write("stone= "+ str(z) + '\n')
    save.write("nft_coin= "+ str(aa) + '\n')
    save.write("waktu= "+ str(ab) + '\n')
    save.write("tahun= "+ str(ac) + '\n')
    save.write("bulan= "+ str(ad) + '\n')
    save.write('\n'+ '#This is the default[if you want to do a new game]' +'\n' +'#clicks = 0 ' + '\n' + '#the_evolve = 50' + '\n' + '#the_upgrade = 1' + '\n' + '#the_cost = 50' + '\n' + '#the_dream = 1 ' + '\n' + '#the_level = 1 ' + '\n' + '#the_evolving = 50'+'\n' + '#the_prestige = 1')

def test1(xa,a,b,baba,babas ,c = "gachapull.mp3",d = 5000) :
    if baba <= xa <= babas :
        a = turtle.Turtle()
        a.shape(b)

        pygame.mixer.music.pause()
        minang_effect = effect(c)
        minang_effect.play()
        minang_effect.fadeout(d)

        def closesong_illuminashiet(x,y):
            pygame.mixer.stop()
            pygame.mixer.music.unpause()
            a.hideturtle()

        a.onclick(closesong_illuminashiet)   

def fade(width, height): 
    screen = pygame.display.set_mode((1300, 650))
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        redrawWindow()
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(0)

def redrawWindow():
    loading_img = pygame.image.load('loading.png')
    screen = pygame.display.set_mode((1300, 650))
    screen.fill((255,255,255))
    screen.blit(loading_img,(300,75))
