import pygame

state = {  "is_window_open": True,

}
def main():
    pygame.init()
    while  state["is_window_open"]:
        handle_user_events()

def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:









if __name__ == '__main__':
    main()