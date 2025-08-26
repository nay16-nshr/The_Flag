import pygame.image

import Const


def create():
    img_soldier = pygame.image.load("soldier.png")
    img_soldier = pygame.transform.scale(img_soldier,(Const.SOLDIER_WIDTH,Const.SOLDIER_HEIGHT))
    return {"img" : img_soldier, "pos" : (0,0)}

# def move_in_direction(direction):
#     if direction == "left":
#         pass
#     elif direction == "right":
#         pass
#     elif direction == "up":
#         pass
#     elif direction == "down":
#         pass

def should_stop():
    pass
def position_top_left(soldier):
    return soldier["pos"]
def position_body(soldier):
    top_pos =position_top_left(soldier)
    return [top_pos,(top_pos[0],top_pos[1]+1),(top_pos[0]+1,top_pos[1]),(top_pos[0]+1,top_pos[1]+1),(top_pos[0]+2,top_pos[1]),(top_pos[0]+2,top_pos[1]+1),]
def position_legs(soldier):
    top_pos = position_top_left(soldier)
    return [(top_pos[0]+3,top_pos[1]),(top_pos[0]+3,top_pos[1]+1)]
def is_in_game_field():
    pass