import enum

import pygame
from pygame import constants

from battlecity.config import PLAYER1_IMG_UP, PLAYER1_IMG_DOWN, PLAYER1_IMG_LEFT, PLAYER1_IMG_RIGHT


class Direction(enum.IntEnum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Player(pygame.sprite.Sprite):
    SIZE = W, H, = 60, 60
    # COLOR = pygame.Color("#6288FA")
    SPEED = 3

    def __init__(self, x, y):
        super(Player, self).__init__()
        # self.image = pygame.Surface(Player.SIZE)

        self.sprites = {
            Direction.UP: pygame.image.load(PLAYER1_IMG_UP).convert(),
            Direction.DOWN: pygame.image.load(PLAYER1_IMG_DOWN).convert(),
            Direction.LEFT: pygame.image.load(PLAYER1_IMG_LEFT).convert(),
            Direction.RIGHT: pygame.image.load(PLAYER1_IMG_RIGHT).convert(),
        }

        self.direction = Direction.UP

        self.image = self.sprites[self.direction]
        self.rect = self.image.get_rect()

        self.rect.topleft = x, y
        # self.image.fill(Player.COLOR)

        self.vx = 0
        self.vy = 0

    def move(self, keys):
        if not keys[constants.K_UP] and not keys[constants.K_DOWN]:
            self.vy = 0
        elif keys[constants.K_UP] and not keys[constants.K_LEFT] and not keys[constants.K_RIGHT]:
            self.vy = -self.SPEED
            self.direction = Direction.UP
        elif keys[constants.K_DOWN] and not keys[constants.K_LEFT] and not keys[constants.K_RIGHT]:
            self.vy = self.SPEED
            self.direction = Direction.DOWN

        if not keys[constants.K_LEFT] and not keys[constants.K_RIGHT]:
            self.vx = 0
        elif keys[constants.K_LEFT] and not keys[constants.K_UP] and not keys[constants.K_DOWN]:
            self.vx = -self.SPEED
            self.direction = Direction.LEFT
        elif keys[constants.K_RIGHT] and not keys[constants.K_UP] and not keys[constants.K_DOWN]:
            self.vx = self.SPEED
            self.direction = Direction.RIGHT

    def stop(self):
        self.vy = 0
        self.vx = 0

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        self.image = self.sprites[self.direction]