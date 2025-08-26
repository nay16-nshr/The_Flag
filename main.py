import pygame

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
    while  state["is_window_open"]:
        handle_user_events()
        if state["flag_touch"]:
            pass
        if state["mine_touch"]:
            pass

    Screen.draw_game(state)

def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                state["soldier"]["pos"][0]-=1
                soldier.move_in_direction("left")
            if event.key == pygame.K_RIGHT:
                state["soldier"]["pos"][0] += 1
                soldier.move_in_direction("right")
            if event.key == pygame.K_UP:
                state["soldier"]["pos"][1] += 1
                soldier.move_in_direction("up")
            if event.key == pygame.K_DOWN:
                state["soldier"]["pos"][1] -= 1
                soldier.move_in_direction("down")
            if event.key == pygame.K_RETURN:
                state["is_enter"] = True










if __name__ == '__main__':
    main()






# pygame.display.set_caption("The_Flag")
# pygame.display.update()
# Quit Pygame
# pygame.quit()