import turtle #turtle module just to make background and importing image
import os
import pygame
import random

from permainan import * #importing game progress
from tkinter import *
from pygame import *
from ALLFUNC import *
from sys import *
from SCREEN2_PLAYING import playing2

os.chdir('C:/Users/Asus/FinalProjectSirJude')

mixer.init()

hero_hp_count, enemy_hp_count , enemy_hp_percentage_text,hero_hp_percentage_text , popups , the_enemy_at_text , the_enemy_hp_text,popup_kill,wn1,goback,punch ,popup_dead= playing2()




wn1.mainloop()


