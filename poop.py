import turtle #turtle module just to make background and importing image
import os
import time
import pygame

from permainan import * #importing game progress
from tkinter import *
from pygame import *
 
os.chdir('C:/Users/Asus/FinalProjectSirJude')

mixer.init()
def lagu(a):
    music = (f'C:/Users/Asus/FinalProjectsirJude/{a}')
    return music

background_music = lagu('Happy.mp3') #music bu MaxKoMusic
mixer.music.load(background_music)
mixer.music.set_volume(0.2)
mixer.music.play(-1)

sound_effect = lagu('fart/wav')

def effect(a):
    c = lagu(a)
    sound_effect = mixer.Sound(c)
    return sound_effect 

wn = turtle.Screen() #to make a game windows
wn.title("The Poopyz @andreanhasan") #to make the game title
wn.bgcolor("orange") #to set the background color

def photo(a):
    aa = f'C:/Users/Asus/FinalProjectSirJude/{a}'
    wn.register_shape(f'C:/Users/Asus/FinalProjectSirJude/{a}')
    return aa

mrpoopyz_photo = photo("mrpoopyz.gif")
UPGRADE_button = photo("UPGRADE.gif")
PRESTIGE_button = photo("PRESTIGE.gif")
MAX_button = photo("MAX.gif")
popup_prestige = photo("prestigepoop.gif")

poopyz = turtle.Turtle()
poopyz.shape(mrpoopyz_photo) #using the image from the dir

upgrades = turtle.Turtle()    
upgrades.shape(UPGRADE_button)

prestiges = turtle.Turtle()
prestiges.shape(PRESTIGE_button)

max = turtle.Turtle()
max.shape(MAX_button)

# popup.shape(popup_prestige)

poops = turtle.Turtle()
clicking_info = turtle.Turtle()
the_cost_text = turtle.Turtle()
the_level_text = turtle.Turtle()
the_prestige_text = turtle.Turtle()
the_prestige_info = turtle.Turtle()

the_prestige_info_inside = 'Min level 100 to prestige'
the_prestige_info_how = 'Gain 1% extra upgrades per level'
click_info = (f'Clicks per click : {(the_upgrade)}')

def tophoto(a,b,c):
    a.penup()
    a.goto(b,c)

tophoto(upgrades,-310,0)
tophoto(prestiges,0,-215)
tophoto(max,-335,70)

def towrite(a,b,c,d,e,f,g):
    a.color(b) #color of the font
    a.penup()
    a.goto(c,d) #location of the font
    a.hideturtle()
    a.ht()
    if g != 0 :
        a.write(f"{g}: {(e)}",align ="center", font = ("Courier New",f,"bold"))
    else:
        a.write(e)

towrite(poops,"black",0,200,clicks,37,"Clicks")
towrite(clicking_info,"black",-50,190,click_info,22,0)
towrite(the_cost_text,"black",-365,-90,the_cost,15,"Cost")
towrite(the_level_text,"black",0,-150,the_level,30,"Level")
towrite(the_prestige_text,"black",0,-300,the_prestige,30,"Prestige")
towrite(the_prestige_info,"black",-49,-165,the_prestige_info_inside,20,0)
towrite(the_prestige_info,"black",-73,-178,the_prestige_info_how,20,0)

def parameter(a,b,c,d,e,f,g,h,i):
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
    save.write('\n'+ '#This is the default[if you want to do a new game]' +'\n' +'#clicks = 0 ' + '\n' + '#the_evolve = 50' + '\n' + '#the_upgrade = 1' + '\n' + '#the_cost = 50' + '\n' + '#the_dream = 1 ' + '\n' + '#the_level = 1 ' + '\n' + '#the_evolving = 50'+'\n' + '#the_prestige = 1')

def clicker(x,y):
    global clicks
    global the_evolve
    global the_upgrade
    global the_dream
    global the_evolving

    fart_effect = effect("fart.wav")
    fart_effect.play()

    if clicks >= the_evolve :
        the_evolve = the_evolve + the_evolving
        the_evolving = the_evolving*2.3
        the_upgrade = the_upgrade + the_dream

        clicking_info.clear()
        clicking_info.write(f'Clicks per click : {(the_upgrade)}')

    clicks = clicks + the_upgrade

    parameter(clicks,the_evolve,the_upgrade,the_cost,the_dream,the_level,the_evolving,the_prestige,the_prestige_prize)

    poops.clear()
    poops.write(f"Clicks: {(clicks)}",align ="center", font = ("Courier New",37,"bold"))

def clicker2(x,y):
    global the_dream
    global the_cost 
    global clicks
    global the_level
    global the_prestige_prize

    if clicks >= the_cost :
        clicks = clicks - the_cost
        the_dream = the_dream * the_prestige_prize
        the_cost = the_cost * 1.4
        the_level = the_level + 1

        the_cost_text.clear()
        the_cost_text.write(f"Cost: {(the_cost)}",align ="center", font = ("Courier New",15,"bold"))

        the_level_text.clear()
        the_level_text.write(f"Level: {(the_level)}",align ="center", font = ("Courier New",30,"bold"))

        poops.clear()
        poops.write(f"Clicks: {(clicks)}",align ="center", font = ("Courier New",37,"bold"))

        clicking_info.clear()
        clicking_info.write(f'Clicks per click : {(the_upgrade)}')

    else :
        pass

    parameter(clicks,the_evolve,the_upgrade,the_cost,the_dream,the_level,the_evolving,the_prestige,the_prestige_prize)

def clicker2max(x,y):
    global the_dream
    global the_cost 
    global clicks
    global the_level
    global the_prestige_prize

    if clicks >= the_cost :
        getcost = the_cost
        countloops = 0
        while getcost < clicks:
            getcost = getcost*1.4
            countloops = countloops + 1

        for i in range (countloops -2):
            clicks = clicks - the_cost*1.4
            the_dream = the_dream * the_prestige_prize 
            the_cost = the_cost * 1.4 
            the_level = the_level + 1 

        the_cost_text.clear()
        the_cost_text.write(f"Cost: {(the_cost)}",align ="center", font = ("Courier New",15,"bold"))

        the_level_text.clear()
        the_level_text.write(f"Level: {(the_level)}",align ="center", font = ("Courier New",30,"bold"))

        poops.clear()
        poops.write(f"Clicks: {(clicks)}",align ="center", font = ("Courier New",37,"bold"))

        clicking_info.clear()
        clicking_info.write(f'Clicks per click : {(the_upgrade)}')

    else :
        pass

    parameter(clicks,the_evolve,the_upgrade,the_cost,the_dream,the_level,the_evolving,the_prestige,the_prestige_prize)

def closesong(x,y):
    minang_effect = effect('minang.mp3')
    minang_effect.stop()
    
    popup.hideturtle()

popup = turtle.Turtle()
def clicker3(x,y):
    global the_cost
    global the_dream
    global clicks
    global the_evolve
    global the_prestige
    global the_upgrade
    global the_evolving
    global the_level
    global the_prestige_prize
    global pygame

    if the_level >= 100 :
        level = the_level /100
        the_prestige_prize = the_prestige_prize + level*1.3

        clicks = 0
        the_evolve = 50
        the_upgrade = 1
        the_cost = 50
        the_dream = 1
        the_level = 111 #JANGAN LUPA GANTI ANDREANNNNNNNNNNNNNNNN
        the_evolving = 1
        the_prestige = the_prestige + 1

        the_cost_text.clear()
        the_cost_text.write(f"Cost: {(the_cost)}",align ="center", font = ("Courier New",15,"bold"))

        the_level_text.clear()
        the_level_text.write(f"Level: {(the_level)}",align ="center", font = ("Courier New",30,"bold"))

        poops.clear()
        poops.write(f"Clicks: {(clicks)}",align ="center", font = ("Courier New",37,"bold"))

        the_prestige_text.clear()
        the_prestige_text.write(f"Prestige: {(the_prestige)}",align ="center", font = ("Courier New",30,"bold"))

        clicking_info.clear()
        clicking_info.write(f'Clicks per click : {(the_upgrade)}')

        pygame.mixer.music.pause()
        minang_effect = effect("minang.mp3")
        minang_effect.play()
        minang_effect.fadeout(7500)
        
        parameter(clicks,the_evolve,the_upgrade,the_cost,the_dream,the_level,the_evolving,the_prestige,the_prestige_prize)
        
        popup = turtle.Turtle()
        popup.shape(popup_prestige)
        popup.showturtle()

        def closesong(x,y):
         pygame.mixer.stop()
         pygame.mixer.music.unpause()
         popup.hideturtle()
    
    popup.onclick(closesong)
    return popup

poopyz.onclick(clicker)
upgrades.onclick(clicker2)
max.onclick(clicker2max)
prestiges.onclick(clicker3)

popup.onclick(closesong)

wn.mainloop()
