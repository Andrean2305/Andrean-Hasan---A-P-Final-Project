from ALLFUNC import *
import turtle
import pygame
from pygame import *
from permainan import *
import os
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
            
        if the_coin_percentage < 1 : 
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

            # the_damage = the_damage*1.001 + 0.1
            # the_coin = the_coin - the_damage_cost
            # the_damage_cost = the_damage_cost + 10

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
        pygame.mixer.music.stop()
        turtle.bye()
        import platformer_test
    
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
   