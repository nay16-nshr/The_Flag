import pygame
import Screen
pygame.init()

screen = pygame.display.set_mode((1000,500))#each pixel represent 1:20
pygame.display.set_caption("The_Flag")
# Game loop
running = True
while running:
    Screen.draw_game()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
# Quit Pygame
pygame.quit()