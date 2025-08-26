import Const
import pygame
import random
def create_game_field():
    pass


def create_flag():
    return {"img": pygame.image.load("flag.png"), "pos": Const.FLAG_POS_FIELD}

def create_grass():
    return {"img": pygame.image.load("grass.png"), "pos": (random.randint(0,24), random.randint(0,49))}
