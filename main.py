import pygame

import Game_field
import Screen
import soldier
import Const
state = {  "is_window_open": True,
           "color_screen": Const.COLOR_SCREEN,
           "flag_touch": False,
           "mine_touch": False,
           "soldier": soldier.create(),
           "is_enter": False
}

def main():
    pygame.init()
    Game_field.create_game_field()

    while  state["is_window_open"]:
        handle_user_events()
        if is_flag_touch():
            state["flag_touch"]= True
        if state["mine_touch"]:
            pass

        Screen.draw_game(state)

def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if soldier.position_top_left(state["soldier"])[0]!=0:
                    state["soldier"]["pos"]=( state["soldier"]["pos"][0]-1,  state["soldier"]["pos"][1])
            if event.key == pygame.K_RIGHT:
                if soldier.position_body(state["soldier"])[1][0] != Const.SIZE_COL:
                    state["soldier"]["pos"]=( state["soldier"]["pos"][0]+1,  state["soldier"]["pos"][1])
            if event.key == pygame.K_UP:
                if soldier.position_top_left(state["soldier"])[1] != 0:
                    state["soldier"]["pos"]=( state["soldier"]["pos"][0],  state["soldier"]["pos"][1]-1)
            if event.key == pygame.K_DOWN:
                if soldier.position_legs(state["soldier"])[0] != Const.SIZE_ROW:
                    state["soldier"]["pos"]=( state["soldier"]["pos"][0],  state["soldier"]["pos"][1]+1)
            if event.key == pygame.K_RETURN:
                state["is_enter"] = True

def is_flag_touch():
    position = soldier.position_body(state["soldier"])
    for i in position:
        if Game_field.game_field[i[0]][i[1]] == "flag":
            return True
    return False

def is_mine_touch():
    position = soldier.position_legs(state["soldier"])
    for i in position:
        if Game_field.game_field[i[0]][i[1]] == "mine":
            return True
    return False


if __name__ == '__main__':
    main()






# pygame.display.set_caption("The_Flag")
# pygame.display.update()
# Quit Pygame
# pygame.quit()