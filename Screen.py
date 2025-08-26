import pygame
from pygame.examples.music_drop_fade import change_music_position

import Const
import  Game_field

screen = pygame.display.set_mode((Const.SCREEN_HEIGHT,Const.SCREEN_WIDTH))#each pixel represent 1:20
pygame.display.set_caption("The_Flag")
def draw_soldier(soldier):
    screen.blit(soldier["img"],change_pos_field_to_pos(soldier["pos"]))



def draw_grass(grass):
    screen.blit(grass["img"], change_pos_field_to_pos(grass["pos"]))



def draw_flag(flag):
    screen.blit(flag["img"], change_pos_field_to_pos(flag["pos"]))
def draw_mine(pos):
    mine_img = pygame.image.load("mine.png")
    mine_img = pygame.transform.scale(mine_img, (Const.MINE_WIDTH, Const.MINE_HEIGHT))

    screen.blit(mine_img, change_pos_field_to_pos(pos))

def draw(soldier,flag,game_field):
    screen.fill(Const.COLOR_SCREEN)
    draw_soldier(soldier)
    draw_flag(flag)
    for i in range(Const.GRASS_NUMBER):
                draw_grass(Game_field.create_grass())



def draw_dark_mode_game(soldier, game_field):
    screen.fill(Const.COLOR_DARK_SCREEN)

    for i in range (Const.TILE_SIZE,Const.SCREEN_WIDTH,Const.TILE_SIZE):
        pygame.draw.line(screen,Const.LINE_COLOR,(i,0),(i,Const.SCREEN_HEIGHT))
    for i in range(Const.MINE_NUMBER):
        for row in range(len(game_field)):
            for col in range(len(game_field[row])):
                if game_field[row][col] == "mine":
                    pos = (row,col)
                    draw_mine(pos)
                    col += 2
    draw_soldier(soldier)

def draw_game(state):
    soldier = state["soldier"]
    flag = Game_field.create_flag()
    screen.fill(Const.COLOR_SCREEN)
    draw(soldier,flag,Game_field.game_field)
    if state["is_enter"]:
        draw_dark_mode_game(soldier, Game_field.game_field)
def change_pos_field_to_pos(pos):
    return (pos[0]*20,pos[1]*20)