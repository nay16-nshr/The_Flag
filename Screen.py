import pygame
import  game_filed
from main import screen, color_screen

pygame.init()






def draw_soldier():
    pass


def draw_grass():
    pass


def draw_flag():
    pass


def draw_game():
    screen.fill(color_screen)
    game_filed.draw()
    draw_soldier()
    draw_grass()
    draw_flag()