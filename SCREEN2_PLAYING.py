from ALLFUNC import *
import turtle
import pygame
from pygame import *
from permainan import *
import os
from pygame.locals import *
from characterplat import *
import datetime
from MAP3_COLLIDER import *
from MAP import *
from ALLANIMATION import *
import random


os.chdir('C:/Users/Asus/FinalProjectSirJude')

hero_hp_count = the_hp
enemy_hp_count = the_enemy_hp

def playing2():
    
    mixer.init()
    background_music = lagu('boss.mp3')
    mixer.music.load(background_music)
    mixer.music.set_volume(0.4)
    mixer.music.play(-1)

    def photo(a):
        aa = f'C:/Users/Asus/FinalProjectSirJude/{a}'
        wn1.register_shape(f'C:/Users/Asus/FinalProjectSirJude/{a}')
        return aa

    wn1 = turtle.Screen() #to make a game windows
    wn1.setup(width=0.7, height=0.7, startx=None, starty=None)
    wn1.title("The Poopyz @andreanhasan") #to make the game title
    wn1.bgcolor("firebrick") #to set the background color

    mrpoopyz_photo = photo("mrpoopyz.gif")
    poopyz = turtle.Turtle()
    poopyz.shape(mrpoopyz_photo) 
    tophoto(poopyz,-200,0)

    mrsoap_photo = photo("soap.gif")
    soap = turtle.Turtle()
    soap.shape(mrsoap_photo)
    tophoto(soap,200,-50)

    punch_photo = photo("punch.gif")
    punch = turtle.Turtle()
    punch.shape(punch_photo)
    tophoto(punch,-10,-250)

    hero = "MrPoopyz"
    hero_name = turtle.Turtle()
    towrite(hero_name,"peru",-200,-150,hero,20,1)

    enemy = "Souper Bad"
    enemy_name = turtle.Turtle()
    towrite(enemy_name,"cyan",210,-150,enemy,20,1)

    the_at_text = turtle.Turtle()
    towrite(the_at_text,"white smoke",-200,-170,the_damage,8,"AT") 

    the_hp_text = turtle.Turtle()
    towrite(the_hp_text,"white smoke",-200,-190,the_hp,8,"HP") 

    the_enemy_at_text = turtle.Turtle()
    towrite(the_enemy_at_text,"white smoke",215,-170,the_enemy_at,8,"AT") 

    the_enemy_hp_text = turtle.Turtle()
    towrite(the_enemy_hp_text,"white smoke",215,-190,the_enemy_hp,8,"HP") 

    enemy_hp_max = the_enemy_hp
    hero_hp_max = the_hp
    enemy_hp_count = the_enemy_hp
    hero_hp_count = the_hp

    enemy_hp_percentage = "{:.2f}%".format(enemy_hp_max/enemy_hp_count*100)
    enemy_hp_percentage_text = turtle.Turtle()
    towrite(enemy_hp_percentage_text,"green yellow",215,100,enemy_hp_percentage,25,1) 

    hero_hp_percentage = "{:.2f}%".format(hero_hp_max/hero_hp_count*100)
    hero_hp_percentage_text = turtle.Turtle()
    towrite(hero_hp_percentage_text,"green yellow",-205,190,hero_hp_percentage,25,1) 

    popup_kill = photo("CONGRATSKILL.gif")
    popup = turtle.Turtle()

    popup_dead = photo("NOOB.gif")
    popups = turtle.Turtle()

    back = photo("goback.gif")
    goback = turtle.Turtle()
    goback.shape(back)
    tophoto(goback,-490,270)

    def punches(x,y):
        global the_damage
        global the_hp
        global the_enemy_hp
        global the_enemy_at
        global gacha_coin
        global hero_hp_count
        global enemy_hp_count

        punch_effect = effect("PUNCH.mp3")
        punch_effect.play()

        enemy_hp_max = the_enemy_hp
        hero_hp_max = the_hp

        hero_hp_count = hero_hp_count - the_enemy_at
        enemy_hp_count = enemy_hp_count - the_damage

        enemy_hp_percentage = "{:.2f}%".format(enemy_hp_count/enemy_hp_max*100)
        hero_hp_percentage = "{:.2f}%".format(hero_hp_count/hero_hp_max*100)

        if enemy_hp_count > 0 and hero_hp_count > 0 :
            enemy_hp_percentage_text.clear()
            towrite(enemy_hp_percentage_text,"green yellow",215,100,enemy_hp_percentage,25,1) 
            hero_hp_percentage_text.clear()
            towrite(hero_hp_percentage_text,"green yellow",-205,190,hero_hp_percentage,25,1) 
        
        if hero_hp_count < 0 :
            pygame.mixer.music.pause()
            noob_effect = effect("NOOB.mp3")
            noob_effect.play()
            noob_effect.fadeout(5000)

            popups.shape(popup_dead)
            popups.showturtle()
            enemy_hp_count = the_enemy_hp
            hero_hp_count = the_hp
            
            enemy_hp_percentage = "{:.2f}%".format(enemy_hp_count/enemy_hp_max*100)
            hero_hp_percentage = "{:.2f}%".format(hero_hp_count/hero_hp_max*100)

            enemy_hp_percentage_text.clear()
            hero_hp_percentage_text.clear()

            def closesongss(x,y):
                noob_effect.stop()
                pygame.mixer.music.unpause()
                popups.hideturtle()

                towrite(enemy_hp_percentage_text,"green yellow",215,100,enemy_hp_percentage,25,1) 
                towrite(hero_hp_percentage_text,"green yellow",-205,190,hero_hp_percentage,25,1) 

            popups.onclick(closesongss)

        if enemy_hp_count < 0 :
            gacha_coin = gacha_coin + 1

            the_enemy_hp = the_enemy_hp*5
            the_enemy_at = the_enemy_at*1.15 + 2

            pygame.mixer.music.pause()
            rick_effect = effect("rick.mp3")
            rick_effect.play()
            rick_effect.fadeout(7500)

            popup = turtle.Turtle()

            enemy_hp_count = the_enemy_hp
            hero_hp_count = the_hp

            enemy_hp_max = the_enemy_hp
            hero_hp_max = the_hp

            enemy_hp_percentage = "{:.2f}%".format(enemy_hp_count/enemy_hp_max*100)
            hero_hp_percentage = "{:.2f}%".format(hero_hp_count/hero_hp_max*100)

            enemy_hp_percentage_text.clear()
            towrite(enemy_hp_percentage_text,"green yellow",215,100,enemy_hp_percentage,25,1) 
            hero_hp_percentage_text.clear()
            towrite(hero_hp_percentage_text,"green yellow",-205,190,hero_hp_percentage,25,1) 

            the_enemy_at_text.clear()
            towrite(the_enemy_at_text,"white smoke",215,-170,the_enemy_at,8,"AT") 

            the_enemy_hp_text.clear()
            towrite(the_enemy_hp_text,"white smoke",215,-190,the_enemy_hp,8,"HP") 
            
            popup.shape(popup_kill)
            popup.showturtle()

            def closesongs(x,y):
                pygame.mixer.stop()
                pygame.mixer.music.unpause()
                popup.hideturtle()

            parameter(clicks,the_evolve,the_upgrade,the_cost,the_dream,the_level,the_evolving,the_prestige,the_prestige_prize,the_coin,the_damage,the_coin_cost,the_hp,the_coin_percentage,the_damage_cost,the_hp_cost,the_star,the_enemy_hp,the_enemy_at,gacha_coin)
            popup.onclick(closesongs)
            

    def gobacks(a,b):
        wn1.clear()
        # playing2()
        playingscreen1()

    goback.onclick(gobacks)
    punch.onclick(punches)
    return hero_hp_count, enemy_hp_count , enemy_hp_percentage_text,hero_hp_percentage_text , popups , the_enemy_at_text , the_enemy_hp_text,popup_kill,wn1,goback,punch,popup_dead


# TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
# TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
# TTTTTTTT HANYA PEMBATAS TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
# TTTTTTT SO I CAN FIND THE NEXT FUNCTION EASIER TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
# TTTTT I DONT KNOW IF THIS IS DUMB OR SMART TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
# TTT BUT IF IT WORKS IT WORKS TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
# TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
# TTTTTTTTTTTTTTT THE playingscreen1 FUNCTION IS ACTUALLY THE HOME SCREEN OF MY GAME TTTTTTTTTTTTTTTTTTTTTTTTTTTTT
# TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT WHILE playing2 FUNCTION IS TO CALL SECOND SCREEN TTTTTTTTT
# TTTTTTTTTTTTTTTTTTTTTTTT WHICH IS FOR THE BOOS/ENEMY BATTLE TO EARN GACHA COIN TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
# TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! I CAN EITHER PLAY MY/RUN THE GAMES FROM SECOND OR FIRST SCREEN !!!!!!!!!
# TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT

def playingscreen1():
    def ganti(x,y):
        wn.clear()
        playing2()

    mixer.init()
    background_music = lagu('Happy.mp3') #music bu MaxKoMusic
    mixer.music.load(background_music)
    mixer.music.set_volume(0.2)
    mixer.music.play(-1)

    wn = turtle.Screen() #to make a game windows
    wn.setup(width=0.7, height=0.7, startx=None, starty=None)
    wn.title("The Poopyz @andreanhasan") #to make the game title
    wn.bgcolor("orange") #to set the background color
    turtle.speed(0)

    def photo(a):
        aa = f'C:/Users/Asus/FinalProjectSirJude/{a}'
        wn.register_shape(f'C:/Users/Asus/FinalProjectSirJude/{a}')
        return aa

    mrpoopyz_photo = photo("mrpoopyz.gif")
    UPGRADE_button = photo("UPGRADE.gif")
    PRESTIGE_button = photo("PRESTIGE.gif")
    MAX_button = photo("MAX.gif")
    popup_prestige = photo("prestigepoop.gif")
    characteristic = photo("CHAR.gif")
    at_UPGRADE_BUTTON = photo("damage.gif")
    hp_UPGRADE_BUTTON = photo("HitPoint.gif")
    coin_UPGRADE_BUTTON = photo("coin.upgrade.gif")
    battle_button = photo("battle.gif")
    INVENTORY_button = photo("INVENTORY.gif")
    WORLD_button =  photo("WORLD.gif")
    gacha_button = photo("GACHA.gif")

    poopyz = turtle.Turtle()
    poopyz.shape(mrpoopyz_photo) #using the image from the dir

    upgrades = turtle.Turtle()    
    upgrades.shape(UPGRADE_button)

    prestiges = turtle.Turtle()
    prestiges.shape(PRESTIGE_button)

    max = turtle.Turtle()
    max.shape(MAX_button)

    coin = turtle.Turtle()
    coin.shape(characteristic)

    coin_button = turtle.Turtle()
    coin_button.shape(coin_UPGRADE_BUTTON)

    damage_button = turtle.Turtle()
    damage_button.shape(at_UPGRADE_BUTTON)

    HP_button = turtle.Turtle()
    HP_button.shape(hp_UPGRADE_BUTTON)

    go_battle_button = turtle.Turtle()
    go_battle_button.shape(battle_button)

    the_world = turtle.Turtle()
    the_world.shape(WORLD_button)

    inventory = turtle.Turtle()
    inventory.shape(INVENTORY_button)
    
    gacha = turtle.Turtle()
    gacha.shape(gacha_button)

    popup = turtle.Turtle()
    poops = turtle.Turtle()
    clicking_info = turtle.Turtle()
    the_cost_text = turtle.Turtle()
    the_level_text = turtle.Turtle()
    the_prestige_text = turtle.Turtle()
    the_prestige_info = turtle.Turtle()
    the_coin_text = turtle.Turtle()
    the_coin_cost_text = turtle.Turtle()
    the_coin_percentage_text = turtle.Turtle()
    the_hp_text = turtle.Turtle()
    the_hp_cost_text = turtle.Turtle()
    the_at_text = turtle.Turtle()
    the_at_cost_text = turtle.Turtle()
    the_star_text = turtle.Turtle()

    the_prestige_info_inside = 'Min level 100 to prestige'
    the_prestige_info_how = 'Gain 1% extra upgrades per star'
    click_info = (f'Clicks per click : {(the_upgrade)}')

    tophoto(upgrades,-300,0)
    tophoto(prestiges,0,-215)
    tophoto(max,-325,70)
    tophoto(coin,400,0)
    tophoto(coin_button,295,-115)
    tophoto(damage_button,280,-15)
    tophoto(HP_button,480,-15)
    tophoto(go_battle_button,400,-260)
    tophoto(inventory,-405,-180)
    tophoto(the_world,-403,-270)
    tophoto(gacha,-520,50)

    towrite(poops,"black",0,200,clicks,22,"Clicks")
    towrite(clicking_info,"black",-50,190,click_info,12,0)
    towrite(the_cost_text,"black",-365,-90,the_cost,10,"Cost")
    towrite(the_level_text,"black",0,-150,the_level,20,"Level")
    towrite(the_prestige_text,"black",0,-310,the_prestige,20,"Prestige")
    towrite(the_prestige_info,"black",-49,-170,the_prestige_info_inside,20,0)
    towrite(the_prestige_info,"black",-73,-183,the_prestige_info_how,20,0)
    towrite(the_coin_text,"black",350,-128,the_coin,12,"Coins")
    towrite(the_at_text,"black",350,60,the_damage,8,"AT") 
    towrite(the_at_cost_text,"chocolate",265,-57,the_damage_cost,10,"Cost")
    towrite(the_hp_text,"black",550,60,the_hp,8,"HP") 
    towrite(the_hp_cost_text,"chocolate",465,-57,the_hp_cost,10,"Cost")
    towrite(the_star_text,"gold",0,-265,the_star,8,"Star")
    towrite(the_coin_cost_text,"orange",420,-170,the_coin_cost,8,"Cost"," Stars")
    towrite(the_coin_percentage_text,"orange",470,-185,the_coin_percentage,6,"Chances to get coin per click")

    def clicker(x,y):
        global clicks
        global the_evolve
        global the_upgrade
        global the_dream
        global the_evolving
        global the_coin_percentage
        global the_coin

        fart_effect = effect("fart.wav")
        fart_effect.play()

        if clicks >= the_evolve :
            the_evolve = the_evolve + the_evolving
            the_evolving = the_evolving*2.3
            the_upgrade = the_upgrade + the_dream

            clicking_info.clear()
            clicking_info.write(f'Clicks per click : {(the_upgrade)}')
        
        if the_coin_percentage >= 1 :
            the_coin = the_coin + the_coin_percentage
            the_coin_text.clear()
            towrite(the_coin_text,"black",350,-128,the_coin,12,"Coins")
            cash_effect = effect("cash.mp3")
            cash_effect.play()
            
        elif the_coin_percentage < 1 : 
            if random.randint(0,100) < the_coin_percentage*100:
                the_coin = the_coin + 1
                the_coin_text.clear()
                towrite(the_coin_text,"black",350,-128,the_coin,12,"Coins")
                cash_effect = effect("cash.mp3")
                cash_effect.play()

        clicks = clicks + the_upgrade

        parameter(clicks,the_evolve,the_upgrade,the_cost,the_dream,the_level,the_evolving,the_prestige,the_prestige_prize,the_coin,the_damage,the_hp,the_coin_cost,the_coin_percentage,the_damage_cost,the_hp_cost,the_star)

        poops.clear()
        poops.write(f"Clicks: {(clicks)}",align ="center", font = ("Apple II ALT Pro",22,"bold"))

    def clicker2(x,y):
        global the_dream
        global the_cost 
        global clicks
        global the_level
        global the_prestige_prize
        global the_coin

        if clicks >= the_cost :
            clicks = clicks - the_cost
            the_dream = the_dream * the_prestige_prize
            the_cost = the_cost * 1.4
            the_level = the_level + 1

            upgrade_effect = effect("upgrade.mp3")
            upgrade_effect.set_volume(0.3)
            upgrade_effect.play()

            the_cost_text.clear()
            the_cost_text.write(f"Cost: {(the_cost)}",align ="center", font = ("Apple II ALT Pro",10,"bold"))

            the_level_text.clear()
            the_level_text.write(f"Level: {(the_level)}",align ="center", font = ("Apple II ALT Pro",20,"bold"))

            poops.clear()
            poops.write(f"Clicks: {(clicks)}",align ="center", font = ("Apple II ALT Pro",22,"bold"))

            clicking_info.clear()
            clicking_info.write(f'Clicks per click : {(the_upgrade)}')

        else :
            pass

        parameter(clicks,the_evolve,the_upgrade,the_cost,the_dream,the_level,the_evolving,the_prestige,the_prestige_prize,the_coin,the_damage,the_hp,the_coin_cost,the_coin_percentage,the_damage_cost,the_hp_cost,the_star)

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

            upgrade_effect = effect("upgrade.mp3")
            upgrade_effect.set_volume(0.3)
            upgrade_effect.play()

            the_cost_text.clear()
            the_cost_text.write(f"Cost: {(the_cost)}",align ="center", font = ("Apple II ALT Pro",10,"bold"))

            the_level_text.clear()
            the_level_text.write(f"Level: {(the_level)}",align ="center", font = ("Apple II ALT Pro",20,"bold"))

            poops.clear()
            poops.write(f"Clicks: {(clicks)}",align ="center", font = ("Apple II ALT Pro",22,"bold"))

            clicking_info.clear()
            clicking_info.write(f'Clicks per click : {(the_upgrade)}')

        else :
            pass

        parameter(clicks,the_evolve,the_upgrade,the_cost,the_dream,the_level,the_evolving,the_prestige,the_prestige_prize,the_coin,the_damage,the_hp,the_coin_cost,the_coin_percentage,the_damage_cost,the_hp_cost,the_star)

    def closesong(x,y):
        minang_effect = effect('minang.mp3')
        minang_effect.stop()
        
        popup.hideturtle()

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
        global the_star
        global pygame

        if the_level >= 100 :
            level = the_level /100
            the_prestige_prize = the_prestige_prize + level*1.3

            the_star = the_star + the_level/10
            clicks = 0
            the_evolve = 50
            the_upgrade = 1
            the_cost = 50
            the_dream = 1
            the_level = 111 #JANGAN LUPA GANTI ANDREANNNNNNNNNNNNNNNN
            the_evolving = 1
            the_prestige = the_prestige + 1

            the_cost_text.clear()
            the_cost_text.write(f"Cost: {(the_cost)}",align ="center", font = ("Apple II ALT Pro",10,"bold"))

            the_level_text.clear()
            the_level_text.write(f"Level: {(the_level)}",align ="center", font = ("Apple II ALT Pro",20,"bold"))

            poops.clear()
            poops.write(f"Clicks: {(clicks)}",align ="center", font = ("Apple II ALT Pro",22,"bold"))

            the_prestige_text.clear()
            the_prestige_text.write(f"Prestige: {(the_prestige)}",align ="center", font = ("Apple II ALT Pro",20,"bold"))

            clicking_info.clear()
            clicking_info.write(f'Clicks per click : {(the_upgrade)}')

            the_star_text.clear()
            towrite(the_star_text,"gold",0,-265,the_star,8,"Star")

            pygame.mixer.music.pause()
            minang_effect = effect("minang.mp3")
            minang_effect.play()
            minang_effect.fadeout(7500)
            
            parameter(clicks,the_evolve,the_upgrade,the_cost,the_dream,the_level,the_evolving,the_prestige,the_prestige_prize,the_coin,the_damage,the_hp,the_coin_cost,the_coin_percentage,the_damage_cost,the_hp_cost,the_star)
            
            popup = turtle.Turtle()
            popup.shape(popup_prestige)
            popup.showturtle()

            def closesong(x,y):
                pygame.mixer.stop()
                pygame.mixer.music.unpause()
                popup.hideturtle()
        
        popup.onclick(closesong)
        return popup

    def damage(x,y):
        global the_coin
        global the_damage
        global the_damage_cost

        if the_coin >= the_damage_cost :
            the_damage = the_damage*1.001 + 0.1
            the_coin = the_coin - the_damage_cost
            the_damage_cost = the_damage_cost + 10

            sword_effect = effect("sword.mp3")
            sword_effect.play()

            the_at_text.clear()
            towrite(the_at_text,"black",350,60,the_damage,8,"AT") 

            the_at_cost_text.clear()
            towrite(the_at_cost_text,"chocolate",265,-57,the_damage_cost,10,"Cost")

            the_coin_text.clear()
            towrite(the_coin_text,"black",350,-128,the_coin,12,"Coins")
        else : 
            pass

        parameter(clicks,the_evolve,the_upgrade,the_cost,the_dream,the_level,the_evolving,the_prestige,the_prestige_prize,the_coin,the_damage,the_hp,the_coin_cost,the_coin_percentage,the_damage_cost,the_hp_cost,the_star)

    def hp(x,y):
        global the_coin
        global the_hp
        global the_hp_cost

        if the_coin >= the_hp_cost :
            the_hp = the_hp*1.001 + 0.1
            the_coin = the_coin - the_hp_cost
            the_hp_cost = the_hp_cost + 10

            hp_effect = effect("hp.mp3")
            hp_effect.play()

            the_hp_text.clear()
            towrite(the_hp_text,"black",550,60,the_hp,8,"HP") 

            the_hp_cost_text.clear()
            towrite(the_hp_cost_text,"chocolate",465,-57,the_hp_cost,10,"Cost")

            the_coin_text.clear()
            towrite(the_coin_text,"black",350,-128,the_coin,12,"Coins")
        else : 
            pass

        parameter(clicks,the_evolve,the_upgrade,the_cost,the_dream,the_level,the_evolving,the_prestige,the_prestige_prize,the_coin,the_damage,the_coin_cost,the_hp,the_coin_percentage,the_damage_cost,the_hp_cost,the_star)

    def coins(x,y):
        global the_coin
        global the_coin_cost
        global the_coin_percentage
        global the_star

        if the_star >= the_coin_cost :
            the_coin_percentage = the_coin_percentage + 0.01
            the_star = the_star - the_coin_cost
            the_coin_cost = the_coin_cost*1.1 + 10

            the_coin_text.clear()
            towrite(the_coin_text,"black",350,-128,the_coin,12,"Coins")

            the_star_text.clear()
            towrite(the_star_text,"gold",0,-265,the_star,8,"Star")

            the_coin_cost_text.clear()
            towrite(the_coin_cost_text,"orange",420,-170,the_coin_cost,8,"Cost"," Stars")

            the_coin_percentage_text.clear()
            towrite(the_coin_percentage_text,"orange",470,-185,the_coin_percentage,6,"Chances to get coin per click")

        else : 
            pass

        parameter(clicks,the_evolve,the_upgrade,the_cost,the_dream,the_level,the_evolving,the_prestige,the_prestige_prize,the_coin,the_damage,the_coin_cost,the_hp,the_coin_percentage,the_damage_cost,the_hp_cost,the_star)

    def ganti(x,y):
        wn.clear()
        playing2()

    def ganti2(x,y):
        wn.clear()
        playing3()

    def ganti3(x,y):
        wn.clear()
        mapz1()
    
    def ganti4(x,y):
        wn.clear()
        pygame.mixer.music.stop()
        inventorys()
    
    go_battle_button.onclick(ganti)    
    poopyz.onclick(clicker)
    upgrades.onclick(clicker2)
    max.onclick(clicker2max)
    prestiges.onclick(clicker3)
    damage_button.onclick(damage)
    HP_button.onclick(hp)
    coin_button.onclick(coins)
    gacha.onclick(ganti2)
    the_world.onclick(ganti3)
    inventory.onclick(ganti4)

    popup.onclick(closesong)
    wn.mainloop()
    return clicking_info, the_coin_text , poops , the_cost_text , the_level_text , clicking_info, popup,the_prestige_text , the_star_text , the_at_text, the_coin_text , the_hp_text , popup_prestige,the_at_cost_text,the_hp_cost_text, the_coin_cost_text , the_coin_percentage_text,wn,poopyz, upgrades, max,prestiges , damage_button,HP_button,coin_button,go_battle_button


###################################################################################################################
###################################################################################################################
########oooooo######################ooooooooooo#############oooo####################oooo######ooooooooooooooooooooo
########oooooo####################oooo#######oooo############oooo##################oooo#######ooooooooooooooooooooo
########oooooo##################oooo########## oooo###########oooo################oooo########ooooo################
########oooooo#################oooo##############oooo##########oooo##############oooo#########ooooooooooooooooooooo
########oooooo###############oooo##################oooo#########oooo############oooo##########ooooooooooooooooooooo
########oooooo################oooo###############oooo############oooo##########oooo###########ooooo################
########oooooooooooooooooo#####oooo############oooo###############oooo########oooo############ooooooooooooooooooooo
########oooooooooooooooooo######oooo#########oooo##################oooo######oooo#############ooooooooooooooooooooo
########oooooooooooooooooo########ooooooooooooo#####################oooooooooo################ooooooooooooooooooooo
###################################################################################################################


xaaa = 0
def playing3() :
    mixer.init()
    background_music = lagu('gachatheme.mp3')
    mixer.music.load(background_music)
    mixer.music.set_volume(0.8)
    mixer.music.play(-1)

    def photo(a):
        aa = f'C:/Users/Asus/FinalProjectSirJude/{a}'
        wn2.register_shape(f'C:/Users/Asus/FinalProjectSirJude/{a}')
        return aa

    wn2 = turtle.Screen() #to make a game windows
    wn2.setup(width=0.7, height=0.7, startx=None, starty=None)
    wn2.title("The Poopyz @andreanhasan") #to make the game title
    wn2.bgcolor("firebrick") #to set the background color

    gacha_photo = photo("firstgacha.gif")
    gacha_1_times = photo("gacha1time.gif")
    gacha_10_times = photo("gacha10times.gif")
    popup_creepoops = photo("CREEPOOP.gif")
    popup_illuminashiets = photo('illuminashiet.gif')
    back = photo("goback.gif")

    gacha = turtle.Turtle()
    gacha.shape(gacha_photo) 
    tophoto(gacha,0,110)

    gacha_1_time = turtle.Turtle()
    gacha_1_time.shape(gacha_1_times) 
    tophoto(gacha_1_time,0,-130)

    gacha_10_time = turtle.Turtle()
    gacha_10_time.shape(gacha_10_times) 
    tophoto(gacha_10_time,0,-215)

    popup_creepoop = turtle.Turtle()
    popup_illuminashiet = turtle.Turtle()

    goback = turtle.Turtle()
    goback.shape(back)
    tophoto(goback,-490,270)
            
    def spin1(x,y):
        global gacha_coin
        global illuminashiet_level
        global creepooper_level
        global speed_level
        global chop_level

        if gacha_coin >= 1 :
            gacha_coin = gacha_coin -1
            xa = random.randint(0,100)

            test1(xa,popup_creepoop,popup_creepoops,0,30) 
            if 0<= xa <= 30 :
                creepooper_level = creepooper_level + 1
                speed_level = speed_level + 0.02
                chop_level = chop_level + 0.04

            test1(xa,popup_illuminashiet,popup_illuminashiets,31,100)  
            if 31<= xa <= 100 :
                illuminashiet_level = illuminashiet_level + 1
                speed_level = speed_level + 0.01
                chop_level = chop_level + 0.02

            parameter(clicks,the_evolve,the_upgrade,the_cost,the_dream,the_level,the_evolving,the_prestige,the_prestige_prize,the_coin,the_damage,the_coin_cost,the_hp,the_coin_percentage,the_damage_cost,the_hp_cost,the_star,the_enemy_hp,the_enemy_at,gacha_coin,creepooper_level,illuminashiet_level,speed_level,chop_level)

    def test10(xa,a,b,baba,babas ,c = "gachapull.mp3",d = 5000) :
        global xaaa
        if baba <= xa <= babas :
            a = turtle.Turtle()
            a.shape(b)

            if xaaa >= 10 :
                xaaa = 0

            pygame.mixer.music.pause()
            minang_effect = effect(c)
            minang_effect.play()
            minang_effect.fadeout(d)
            xaaa = xaaa + 1
            xa = random.randint(0,100)
            def closesong_illuminashiet(x,y):
                global creepooper_level
                global illuminashiet_level
                global speed_level
                global chop_level
                
                pygame.mixer.stop()
                pygame.mixer.music.unpause()
                a.hideturtle()

                if xaaa < 10 :
                    if 31<= xa <= 100 :
                      illuminashiet_level = illuminashiet_level + 1
                      speed_level = speed_level + 0.01
                      chop_level = chop_level + 0.02
                    if 0<= xa <= 30 :
                     creepooper_level = creepooper_level + 1
                     speed_level = speed_level + 0.02
                     chop_level = chop_level + 0.04
                    parameter(clicks,the_evolve,the_upgrade,the_cost,the_dream,the_level,the_evolving,the_prestige,the_prestige_prize,the_coin,the_damage,the_coin_cost,the_hp,the_coin_percentage,the_damage_cost,the_hp_cost,the_star,the_enemy_hp,the_enemy_at,gacha_coin,creepooper_level,illuminashiet_level,speed_level,chop_level)
                    
                    test10(xa,popup_creepoop,popup_creepoops,0,30) 
                    test10(xa,popup_illuminashiet,popup_illuminashiets,31,100) 

                
            a.onclick(closesong_illuminashiet)

    def spin2(x,y):
        global gacha_coin
        global illuminashiet_level
        global creepooper_level
        global speed_level
        global chop_level

        xa = random.randint(0,100)
        test10(xa,popup_creepoop,popup_creepoops,0,30) 
        if 0<= xa <= 30 :
            creepooper_level = creepooper_level + 1
            speed_level = speed_level + 0.02
            chop_level = chop_level + 0.04

        test10(xa,popup_illuminashiet,popup_illuminashiets,31,100)  
        if 31<= xa <= 100 :
            illuminashiet_level = illuminashiet_level + 1
            speed_level = speed_level + 0.01
            chop_level = chop_level + 0.02

        parameter(clicks,the_evolve,the_upgrade,the_cost,the_dream,the_level,the_evolving,the_prestige,the_prestige_prize,the_coin,the_damage,the_coin_cost,the_hp,the_coin_percentage,the_damage_cost,the_hp_cost,the_star,the_enemy_hp,the_enemy_at,gacha_coin,creepooper_level,illuminashiet_level,speed_level,chop_level)
    def gobacks(a,b):
        wn2.clear()
        # playing2()
        playingscreen1()

    goback.onclick(gobacks)
    gacha_10_time.onclick(spin2)
    gacha_1_time.onclick(spin1)
    wn2.mainloop()




###################################################################################################################
###################################################################################################################
########oooooo######################ooooooooooo#############oooo####################oooo######ooooooooooooooooooooo
########oooooo####################oooo#######oooo############oooo##################oooo#######ooooooooooooooooooooo
########oooooo##################oooo########## oooo###########oooo################oooo########ooooo################
########oooooo#################oooo##############oooo##########oooo##############oooo#########ooooooooooooooooooooo
########oooooo###############oooo##################oooo#########oooo############oooo##########ooooooooooooooooooooo
########oooooo################oooo###############oooo############oooo##########oooo###########ooooo################
########oooooooooooooooooo#####oooo############oooo###############oooo########oooo############ooooooooooooooooooooo
########oooooooooooooooooo######oooo#########oooo##################oooo######oooo#############ooooooooooooooooooooo
########oooooooooooooooooo########ooooooooooooo#####################oooooooooo################ooooooooooooooooooooo
###################################################################################################################

###################################################################################################################
###################################################################################################################
########oooooo######################ooooooooooo#############oooo####################oooo######ooooooooooooooooooooo
########oooooo####################oooo#######oooo############oooo##################oooo#######ooooooooooooooooooooo
########oooooo##################oooo########## oooo###########oooo################oooo########ooooo################
########oooooo#################oooo##############oooo##########oooo##############oooo#########ooooooooooooooooooooo
########oooooo###############oooo##################oooo#########oooo############oooo##########ooooooooooooooooooooo
########oooooo################oooo###############oooo############oooo##########oooo###########ooooo################
########oooooooooooooooooo#####oooo############oooo###############oooo########oooo############ooooooooooooooooooooo
########oooooooooooooooooo######oooo#########oooo##################oooo######oooo#############ooooooooooooooooooooo
########oooooooooooooooooo########ooooooooooooo#####################oooooooooo################ooooooooooooooooooooo
###################################################################################################################



def inventorys():
    pygame.init()

    mixer.init()
    mixer.music.load('campfire.mp3')
    mixer.music.set_volume(1)
    mixer.music.play(-1)

    screen_width = 1300
    screen_height = 650

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Poopyz.World')
    screen.fill((74,98,110))
    pygame.display.flip
    #define game variables
    tile_size = 80

    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    black = (16,16,16)

    illuminablank_img = pygame.image.load('illuminablank.png')
    illuminablank_img_rect = illuminablank_img.get_rect()
    illuminablank_img_rect.x = 1300-145
    illuminablank_img_rect.y = 650-20

    creepoopblank_img = pygame.image.load('creepblank.png')
    creepoopblank_img_rect = creepoopblank_img.get_rect()

    class World():
        def __init__(self, data):
            self.tile_list = []

            #load images
            bingkai_img = pygame.image.load('bingkai.png')
            bingkai1_img = pygame.image.load('bingkai1.png')
            creepooper_level_img = pygame.image.load('creepooperinvent.png')
            illuminashiet_level_img = pygame.image.load('illuminavent.png')
            row_count = 0
            for row in data:
                col_count = 0
                for tile in row:
                    if tile == 1:
                        img = pygame.transform.scale(bingkai_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect,2)
                        self.tile_list.append(tile)
                    if tile == 2:
                        img = pygame.transform.scale(bingkai1_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect,2)
                        self.tile_list.append(tile)
                    if tile == 3:
                        img = pygame.transform.scale(bingkai_img, (20,tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect,2)
                        self.tile_list.append(tile)
                    if tile == 928:
                        img = pygame.transform.scale(creepooper_level_img, (tile_size,tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect,2)
                        self.tile_list.append(tile) 
                    if tile == 929:
                        img = pygame.transform.scale(illuminashiet_level_img, (tile_size,tile_size))
                        illuminashiet_rect = img.get_rect()
                        illuminashiet_rect.x = col_count * tile_size
                        illuminashiet_rect.y = row_count * tile_size
                        tile = (img, illuminashiet_rect,2)
                        self.tile_list.append(tile) 
                    col_count += 1
                row_count += 1 

        def draw(self):
            for tile in self.tile_list:
                screen.blit(tile[0], tile[1])

    world_data = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 0], 
    [0, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 0], 
    [0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 0]
    ]

    if creepooper_level > 0 :
        world_data[5][1] = 928
        img = pygame.transform.scale(illuminablank_img, (tile_size,tile_size))
        creepooper_img1_rect = img.get_rect()
        creepooper_img1_rect.x = 1*tile_size
        creepooper_img1_rect.y = 5*tile_size

    if illuminashiet_level > 0 :
        world_data[5][2] = 929
        illuminablank_img1_rect = img.get_rect()
        illuminablank_img1_rect.x = 2*tile_size
        illuminablank_img1_rect.y = 5*tile_size

    world = World(world_data)
    run = True

    illu = inventory(illuminablank_img)
    creepoop = inventory(creepoopblank_img)

    while run :
        screen.fill((74,98,110))
        world.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        if creepoop.muncul == True and illu.muncul == False :
            creepoop.tulisan(42,black,creepooper_level,round(creepooper_level*0.02,2),round(creepooper_level*0.04,2),"Creepooper")
            creepoop.countdowns += 5
            pygame.draw.rect(screen,(255,0,0),creepooper_img1_rect,2)

        if creepoop.muncul == False  and creepoop.baba <= 105:
            creepoop.baba += 3

        if illu.muncul == True and creepoop.muncul == False:
            illu.tulisan(42,black,illuminashiet_level,illuminashiet_level*0.01,illuminashiet_level*0.02,"Illuminashiet")
            illu.countdowns += 5
            pygame.draw.rect(screen,(255,0,0),illuminablank_img1_rect,2)
        
        if illu.muncul == False and illu.baba <= 105 :
            illu.baba += 5

        if event.type == pygame.MOUSEBUTTONDOWN:
            if creepooper_img1_rect.collidepoint(event.pos) and creepoop.muncul == False  :
                creepoop.muncul = True
                creepoop.baba = 0
                illu.muncul = False

            elif creepooper_img1_rect.collidepoint(event.pos) and creepoop.muncul == True and creepoop.countdowns > 100:
                creepoop.countdowns = 0
                creepoop.muncul = False
            
            if illuminablank_img1_rect.collidepoint(event.pos) and illu.muncul == False  :
                illu.baba = 0
                illu.muncul = True
                creepoop.muncul = False

            elif illuminablank_img1_rect.collidepoint(event.pos) and illu.muncul == True and illu.countdowns > 100:
                illu.countdowns = 0
                illu.muncul = False

        pygame.display.update()

        world.draw()
    pygame.quit()
    turtle.bye()

###################################################################################################################
###################################################################################################################
########oooooo######################ooooooooooo#############oooo####################oooo######ooooooooooooooooooooo
########oooooo####################oooo#######oooo############oooo##################oooo#######ooooooooooooooooooooo
########oooooo##################oooo########## oooo###########oooo################oooo########ooooo################
########oooooo#################oooo##############oooo##########oooo##############oooo#########ooooooooooooooooooooo
########oooooo###############oooo##################oooo#########oooo############oooo##########ooooooooooooooooooooo
########oooooo################oooo###############oooo############oooo##########oooo###########ooooo################
########oooooooooooooooooo#####oooo############oooo###############oooo########oooo############ooooooooooooooooooooo
########oooooooooooooooooo######oooo#########oooo##################oooo######oooo#############ooooooooooooooooooooo
########oooooooooooooooooo########ooooooooooooo#####################oooooooooo################ooooooooooooooooooooo
###################################################################################################################
maps1 = True
maps2 = False
maps3 = False
off = False
pertamax = False
def mapz1() :
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

    # maps1 = True
    # maps2 = False
    # maps3 = False

    spawn = [[400,315],[500,275],[600,230],[850,310]]
    spawn_random = random.randint(0,4)
    spawn_now = spawn[spawn_random-1]
    x = spawn_now[0]
    y = spawn_now[1]

    poop3 = character(x,y,64,64)
    font = pygame.font.SysFont("Apple II ALT NEG Pro", 60)
    # timez = False
    # off = False
    # pertamax = False
    # current_time = datetime.datetime.now()

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
        return dx

    def map1 () :
        global wood
        global the_damage
        global the_hp
        global run
        global maps1 
        global maps2
        global maps3

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
        global maps3
        global maps2
        global maps1
        global hour

        current_time = datetime.datetime.now()

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
        if maps1 :
            map1()

        elif maps2:
            map2()
        
        elif maps3 :
            map3()
        pygame.display.update()

    pygame.quit()
    turtle.bye()

