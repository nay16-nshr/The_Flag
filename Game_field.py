import Const
import Screen
import pygame
import random
game_field = []

def create_empty_field():
    for row in range(Const.SIZE_ROW):
        game_field.append(["empty"]*Const.SIZE_COL)


def create_game_field():
    global game_field
    create_empty_field()
    for i in range(Const.FLAG_WIDTH_FIELD):
        for j in range(Const.FLAG_HEIGHT_FIELD):
            game_field[Const.FLAG_POS_FIELD[0] + i][Const.FLAG_POS_FIELD[1]+j] = "flag"
    count_mine = 0
    while count_mine < Const.MINE_NUMBER:
        mine_index = (random.randint(0, 22),random.randint(0,49))
        is_empty = True
        for i in range(3):
            if game_field[mine_index[0]+i][mine_index[1]] != "empty":
                is_empty=False
        if is_empty:
            for i in range(3):
                game_field[mine_index[0] + i][mine_index[1]] = "mine"
            count_mine += 1


def create_flag():
    img_flag = pygame.image.load("flag.png")
    img_flag = pygame.transform.scale(img_flag, (Const.FLAG_WIDTH, Const.FLAG_HEIGHT))
    return {"img": img_flag ,"pos": Const.FLAG_POS_FIELD}

def create_grass():
    img_grass = pygame.image.load("grass.png")
    img_grass = pygame.transform.scale(img_grass, (Const.GRASS_WIDTH, Const.GRASS_HEIGHT))
    return {"img": img_grass, "pos": (random.randint(0,24), random.randint(0,49))}
