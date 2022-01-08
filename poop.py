import turtle #turtle module just to make background and importing image
import os
import pygame
import random

from permainan import * #importing game progress
from tkinter import *
from pygame import *
from ALLFUNC import *
from SCREEN2_PLAYING import *

os.chdir('C:/Users/Asus/FinalProjectSirJude')

mixer.init()

clicking_info, the_coin_text , poops , the_cost_text , the_level_text , clicking_info, popup,the_prestige_text , the_star_text , the_at_text, the_coin_text , the_hp_text , popup_prestige,the_at_cost_text,the_hp_cost_text, the_coin_cost_text , the_coin_percentage_text,wn,poopyz, upgrades, max,prestiges , damage_button,HP_button,coin_button,go_battle_button = playingscreen1()

wn.mainloop()
