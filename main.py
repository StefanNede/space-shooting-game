import game
import pygame
import os
import high_score

pygame.init()

screen = pygame.display.set_mode((game.WIDTH, game.HEIGHT))

WIN = game.WIN
ENTRY_FONT = pygame.font.SysFont('comicsans', 50)


def draw_window():
    WIN.fill((0, 0, 0))
    life_text = ENTRY_FONT.render(
        "press any key to start...", 1, (255, 255, 255))
    WIN.blit(life_text, (0, 200))
    pygame.display.update()


if __name__ == '__main__':
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                game.main()
        draw_window()
    pygame.quit()
