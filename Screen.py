import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((1000,500))#each pixel represent 1:20
color_screen = (0, 200, 0)
screen.fill(color_screen)
pygame.display.set_caption("The_Flag")
# Game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
# Quit Pygame
pygame.quit()
def draw_game():
    screen.fill(color_screen)
    draw_grass()