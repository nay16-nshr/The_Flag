import pygame
import soldier

state = {  "is_window_open": True,
           "color_screen": (0, 200, 0),
           "flag_touch": False,
           "mine_touch": False

}

def main():
    pygame.init()
    while  state["is_window_open"]:
        handle_user_events()
        if state["flag_touch"]:
            pass
        if state["mine_touch"]:
            pass



def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                soldier.move_in_direction("left")
            if event.key == pygame.K_RIGHT:
                soldier.move_in_direction("right")
            if event.key == pygame.K_UP:
                soldier.move_in_direction("up")
            if event.key == pygame.K_DOWN:
                soldier.move_in_direction("down")








if __name__ == '__main__':
    main()





screen = pygame.display.set_mode((1000,500))#each pixel represent 1:20
pygame.display.set_caption("The_Flag")
# Game loop




    pygame.display.update()
# Quit Pygame
pygame.quit()