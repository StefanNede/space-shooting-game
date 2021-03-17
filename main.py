import pygame
import os
import random
import time

WIDTH, HEIGHT = 400, 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space shooters")
FPS = 60
VEL = 3
BULLET_VEL = 3
MAX_BULLETS = 3
MAX_ENEMY_VEL = 2
# the user starts with 10 lives, aka they can get hit 10 times
LIFE = 10
# stores the current level
LEVEL = 1
# stores the amount of levels the game has
AMOUNT_OF_LEVELS = 5
# this stores the amount of enemies that will be on the screen at a time
# at different levels
LEVELS_TO_ENEMIES = {1: 3, 2: 5, 3: 8, 4: 10, 5: 13}
# these are the amount of seconds to be played at different levels until
# you either die or pass the level
LEVELS_TO_TIME = {1: 10, 2: 11, 3: 12, 4: 13, 5: 14}


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

PLAYER = pygame.Rect(WIDTH//2-15, HEIGHT-50, 30, 30)


class Enemy:
    def __init__(self, xposition, yposition, velocity, width=20, height=10):
        self.width = width
        self.height = height
        self.xposition = xposition
        self.yposition = yposition
        self.velocity = velocity

    def draw_enemy(self):
        enemy = pygame.Rect(self.xposition, self.yposition,
                            self.width, self.height)
        return enemy


def draw_window(bullets, enemies):
    WIN.fill(BLACK)
    for bullet in bullets:
        pygame.draw.rect(WIN, RED, bullet)
    for enemy in enemies:
        # enemy[1] is pygame.Rect
        pygame.draw.rect(WIN, YELLOW, enemy[1])
    pygame.draw.rect(WIN, WHITE, PLAYER)
    pygame.display.update()


def move_player(keys_pressed, player):
    if keys_pressed[pygame.K_RIGHT] and player.x + VEL + player.width < WIDTH:
        player.x += VEL
    if keys_pressed[pygame.K_LEFT] and player.x - VEL > 0:
        player.x -= VEL


def move_enemies(enemies):
    # enemy[1] is pygame.Rect
    # enemy[0] is object
    for enemy in enemies:
        enemy[1].y += enemy[0].velocity
        if enemy[1].y > HEIGHT:
            enemies.remove(enemy)


def generate_bullets(bullets):
    for bullet in bullets:
        bullet.y -= BULLET_VEL
        if bullet.y < 0:
            bullets.remove(bullet)


def main():
    global ENEMY_VEL
    clock = pygame.time.Clock()
    run = True
    bullets = []
    # this will be a 2d list that stores the enemy object at the first nested list index
    # and the pygame rectangle of the enemy at the second index
    enemies = []
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        PLAYER.x + PLAYER.width//2 - 2.5, PLAYER.y, 5, 10)
                    bullets.append(bullet)
        for i in range(10 - len(enemies)):
            ENEMY_VEL = float(random.uniform(1, MAX_ENEMY_VEL))
            print(ENEMY_VEL)
            xlocation = random.randint(0, WIDTH)
            curr_enemy = [Enemy(xlocation, 0, ENEMY_VEL), Enemy(
                xlocation, 0, ENEMY_VEL).draw_enemy()]
            enemies.append(curr_enemy)
        move_enemies(enemies)
        keys_pressed = pygame.key.get_pressed()
        move_player(keys_pressed, PLAYER)
        generate_bullets(bullets)
        draw_window(bullets, enemies)
    pygame.quit()


if __name__ == "__main__":
    main()
