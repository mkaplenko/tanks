from abc import ABC, abstractmethod

import pygame
from pygame import constants

from battlecity.config import WALL_IMG, ARM_WALL, FOREST


class Block(ABC, pygame.sprite.Sprite):
    SIZE = W, H, = 30, 30
    WALL = '0'
    ARM_WALL = 'X'
    FOREST = 'F'

    def __init__(self, x, y, hp):
        super(Block, self).__init__()
        self.x = x
        self.y = y

        self.image = pygame.image.load(self.image_file).convert()
        self.image.set_colorkey((0, 0, 0), constants.RLEACCEL)
        self.rect = self.image.get_rect()

        self.rect.topleft = x, y
        self.hp = hp

    @property
    @abstractmethod
    def image_file(self) -> str:
        pass

    def kill(self) -> None:
        if self.hp is not None:
            self.hp -= 1
            if self.hp <= 0:
                super(Block, self).kill()


class Wall(Block):
    def __init__(self, x, y):
        super(Wall, self).__init__(x, y, hp=1)

    @property
    def image_file(self) -> str:
        return WALL_IMG


class ArmoredWall(Block):
    def __init__(self, x, y):
        super(ArmoredWall, self).__init__(x, y, hp=None)

    @property
    def image_file(self) -> str:
        return ARM_WALL


class Forest(Block):
    def __init__(self, x, y):
        super(Forest, self).__init__(x, y, hp=None)

    @property
    def image_file(self) -> str:
        return FOREST
