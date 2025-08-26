import pygame.image

import Const


def create():
    img_soldier = pygame.image.load("soldier.png")
    img_soldier = pygame.transform.scale(img_soldier,(Const.SOLDIER_WIDTH,Const.SOLDIER_HEIGHT))
    return {"img" : img_soldier, "pos" : (0,0)}

def move_in_direction(direction):
    pass
def should_stop():
    pass
def position_top_left():
    pass
def position_body():
    pass
def position_legs():
    pass
def is_in_game_field():
    pass