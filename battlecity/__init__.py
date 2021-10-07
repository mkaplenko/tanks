import enum

import pygame

all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
enemies = pygame.sprite.Group()
tank_blocks = pygame.sprite.Group()
bullet_blocks = pygame.sprite.Group()
forests = pygame.sprite.Group()
bullets = pygame.sprite.Group()


class Direction(enum.IntEnum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
