import pygame 
import os

from permainan import * #importing game progress
from tkinter import *
from ALLFUNC import *

os.chdir('C:/Users/Asus/FinalProjectSirJude')
from pygame.locals import *


right1 = pygame.image.load('mrpoopyz.png')
right2 = pygame.image.load('mrpoopyz2.png')
right3 = pygame.image.load('mrpoopyz3.png')

left1 = pygame.transform.flip(right1, True, False)
left2 = pygame.transform.flip(right2, True, False)
left3 = pygame.transform.flip(right3, True, False)

walk_now = pygame.image.load('mrpoopyz.png')

walk_left = [left1,left1,left1,left2,left2,left2,left3,left3,left3,left1,left1,left1,left2,left2,left2,left3,left3]
walk_right = [right1,right1,right1,right2,right2,right2,right3,right3,right3]

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

ba1 = pygame.image.load('bat1.png')
ba2 = pygame.image.load('bat2.png')
ba3 = pygame.image.load('bat3.png')
ba4 = pygame.image.load('bat4.png')

bat1 = pygame.transform.scale(ba1, (100,100))
bat2 = pygame.transform.scale(ba2, (100,100))
bat3 = pygame.transform.scale(ba3, (100,100))
bat4 = pygame.transform.scale(ba4, (100,100))

bat11 = pygame.transform.flip(bat1, True, False)
bat22 = pygame.transform.flip(bat2, True, False)
bat33 = pygame.transform.flip(bat3, True, False)
bat44 = pygame.transform.flip(bat4, True, False)

bat_now1 = pygame.image.load('bat.png')
bat_now = pygame.transform.scale(bat_now1, (100,100))

bat_left = [bat1,bat1,bat2,bat2,bat3,bat3,bat4,bat4,bat4]
bat_right = [bat11,bat11,bat22,bat22,bat33,bat33,bat44,bat44,bat44]
sleep1_img = pygame.image.load('bat_sleep.png')
sleep_img = pygame.transform.scale(sleep1_img, (25, 25))


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

iluu11 = pygame.image.load('ILLUMINATI_ANI_1.png')
iluu12 = pygame.image.load('ILLUMINATI_ANI_2.png')
iluu13 = pygame.image.load('ILLUMINATI_ANI_3.png')
iluu14 = pygame.image.load('ILLUMINATI_ANI_4.png')
iluu15 = pygame.image.load('ILLUMINATI_ANI_5.png')
iluu16 = pygame.image.load('ILLUMINATI_ANI_6.png')

iluu1 = pygame.transform.scale(iluu11, (45,75))
iluu2 = pygame.transform.scale(iluu12, (45,75))
iluu3 = pygame.transform.scale(iluu13, (45,75))
iluu4 = pygame.transform.scale(iluu14, (45,75))
iluu5 = pygame.transform.scale(iluu15, (45,75))
iluu6 = pygame.transform.scale(iluu16, (45,75))

bounch = [iluu1,iluu1,iluu1,iluu1,iluu1,iluu1,iluu2,iluu2,iluu2,iluu2,iluu2,iluu2,iluu3,iluu3,iluu3,iluu3,iluu3,iluu3,iluu4,iluu4,iluu4,iluu4,iluu4,iluu4,iluu5,iluu5,iluu5,iluu5,iluu5,iluu5,iluu6,iluu6,iluu6,iluu6,iluu6,iluu6]

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (16,16,16)

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

#Fire ANIMASIONG TELL ME THAT YOU LOVE ME EVEN IT IS FAKE CAUSE I DONT FUCKING CARE AT ALL

fire1 = pygame.image.load('fire1.png')
fire2 = pygame.image.load('fire2.png')
fire3 = pygame.image.load('fire3.png')
fire4 = pygame.image.load('fire4.png')
fire5 = pygame.image.load('fire5.png')
fire6 = pygame.image.load('fire6.png')
fire7 = pygame.image.load('fire7.png')
fire8 = pygame.image.load('fire8.png')
fire9 = pygame.image.load('fire9.png')
fire10 = pygame.image.load('fire10.png')
fire11 = pygame.image.load('fire11.png')
fire12 = pygame.image.load('fire12.png')

hinokami_kagura = [fire1,fire1,fire2,fire2,fire3,fire3,fire4,fire4,fire5,fire5,fire6,fire6,fire7,fire7,fire8,fire8,fire9,fire9,fire10,fire10,fire11,fire11,fire12,fire12]

fire1_left = pygame.transform.flip(fire1, True, False)
fire2_left = pygame.transform.flip(fire2, True, False)
fire3_left = pygame.transform.flip(fire3, True, False)
fire4_left = pygame.transform.flip(fire4, True, False)
fire5_left = pygame.transform.flip(fire5, True, False)
fire6_left = pygame.transform.flip(fire6, True, False)
fire7_left = pygame.transform.flip(fire7, True, False)
fire8_left = pygame.transform.flip(fire8, True, False)
fire9_left = pygame.transform.flip(fire9, True, False)
fire10_left = pygame.transform.flip(fire10, True, False)
fire11_left = pygame.transform.flip(fire11, True, False)
fire12_left = pygame.transform.flip(fire12, True, False)

hinokami_kagura_left = [fire1_left,fire1_left,fire2_left,fire2_left,fire3_left,fire3_left,fire4_left,fire4_left,fire5_left,fire5_left,fire6_left,fire6_left,fire7_left,fire7_left,fire8_left,fire8_left,fire9_left,fire9_left,fire10_left,fire10_left,fire11_left,fire11_left,fire12_left,fire12_left]

###################################################################################################################
###################################################################################################################
########oooooo######################ooooooooooo#############oooo####################oooo######ooooooooooooooooooooo
########oooooo####################oooo#######oooo############oooo##################oooo#######ooooooooooooooooooooo
########oooooo##################oooo###########oooo###########oooo################oooo########ooooo################
########oooooo#################oooo##############oooo##########oooo##############oooo#########ooooooooooooooooooooo
########oooooo###############oooo##################oooo#########oooo############oooo##########ooooooooooooooooooooo
########oooooo################oooo###############oooo############oooo##########oooo###########ooooo################
########oooooooooooooooooo#####oooo############oooo###############oooo########oooo############ooooooooooooooooooooo
########oooooooooooooooooo######oooo#########oooo##################oooo######oooo#############ooooooooooooooooooooo
########oooooooooooooooooo########ooooooooooooo#####################oooooooooo################ooooooooooooooooooooo
###################################################################################################################

marah1 = pygame.image.load('marah1.png')
marah2 = pygame.image.load('marah2.png')
marah3 = pygame.image.load('marah3.png')
marah4 = pygame.image.load('marah4.png')
marah5 = pygame.image.load('marah5.png')
marah6 = pygame.image.load('marah6.png')

tbl = [marah1,marah1,marah2,marah2,marah3,marah3,marah4,marah4,marah5,marah5,marah6,marah6]

marah1_left = pygame.transform.flip(marah1, True, False)
marah2_left = pygame.transform.flip(marah2, True, False)
marah3_left = pygame.transform.flip(marah3, True, False)
marah4_left = pygame.transform.flip(marah4, True, False)
marah5_left = pygame.transform.flip(marah5, True, False)
marah6_left = pygame.transform.flip(marah6, True, False)

tbl_left = [marah1_left,marah1_left,marah2_left,marah2_left,marah3_left,marah3_left,marah4_left,marah4_left,marah5_left,marah5_left,marah6_left,marah6_left]