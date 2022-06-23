from pygame import *
from pygame.locals import *

import os
os.chdir('C:/Users/Asus/FinalProjectSirJude')

from permainan import * #importing game progress
from tkinter import *
from ALLFUNC import *
from SCREEN2_PLAYING import *
from characterplat import *

from pygame import mixer

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

inventorys()