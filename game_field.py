import Const
import Screen
from main import screen
import pygame

def create_game_field():
    global game_field
    count_mine = 0
    for row in range(Const.SIZE_ROW):
        for col in range(Const.SIZE_COL):
            while count_mine < Const.MINE_NUMBER:
                pass



    pass
def create_flag():
    pass
def create_mine():
    pass
def draw(soldier_img,flag_img,grass_img):
    screen.fill(Const.color_screen)
    Screen.draw_soldier(soldier_img)
    Screen.draw_flag(flag_img)
    for i in range(Const.GRASS_NUMBER):
        if :
            Screen.draw_grass(grass_img)
    pass