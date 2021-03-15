import pygame
import os
from random import randint
import time

WIDTH, HEIGHT = 400, 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space shooters")
FPS = 60
VEL = 3
BULLET_VEL = 2
MAX_BULLETS = 3
ENEMY_VEL = 1

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

PLAYER = pygame.Rect(WIDTH//2-15, HEIGHT-50, 30, 30)


class Enemy:
    def __init__(self, xposition, yposition, width=10, height=10, velocity=ENEMY_VEL):
        self.width = width
        self.height = height
        self.xposition = xposition
        self.yposition = yposition
        self.velocity = velocity

    def draw_enemy(self):
        enemy = pygame.Rect(self.xposition, self.yposition,
                            self.width, self.height)
        return enemy


def draw_window(bullets, enemy):
    WIN.fill(BLACK)
    for bullet in bullets:
        pygame.draw.rect(WIN, RED, bullet)
    pygame.draw.rect(WIN, YELLOW, enemy)
    pygame.draw.rect(WIN, WHITE, PLAYER)
    pygame.display.update()


def move_player(keys_pressed, player):
    if keys_pressed[pygame.K_RIGHT] and player.x + VEL + player.width < WIDTH:
        player.x += VEL
    if keys_pressed[pygame.K_LEFT] and player.x - VEL > 0:
        player.x -= VEL


def move_enemy(enemy): 
    # need to check for collisions with the bullet, the player, and if it goes off the screen
    enemy.y += 1


def generate_bullets(bullets):
    for bullet in bullets:
        bullet.y -= BULLET_VEL
        if bullet.y < 0:
            bullets.remove(bullet)


def main():
    clock = pygame.time.Clock()
    run = True
    bullets = []
    enemy = Enemy(WIDTH//2, 100).draw_enemy()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        PLAYER.x + PLAYER.width//2 - 2.5, PLAYER.y, 5, 10)
                    bullets.append(bullet)

        move_enemy(enemy)
        keys_pressed = pygame.key.get_pressed()
        move_player(keys_pressed, PLAYER)
        generate_bullets(bullets)
        draw_window(bullets, enemy)
    pygame.quit()


if __name__ == "__main__":
    main()
