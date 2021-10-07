from abc import ABC
from typing import Optional

import pygame
import pyganim
from pygame import constants

from battlecity.config import WALL_IMG, ARM_WALL, FOREST, SEA


class Block(ABC, pygame.sprite.Sprite):
    SIZE = W, H, = 30, 30
    WALL = '0'
    ARM_WALL = 'X'
    FOREST = 'F'
    SEA = 'S'

    def __init__(self, x, y, hp):
        super(Block, self).__init__()
        self.x = x
        self.y = y

        self.animation = self.make_animation()
        if self.image_file is not None:
            self.image = pygame.image.load(self.image_file).convert()
            self.image.set_colorkey((0, 0, 0), constants.RLEACCEL)
            self.anim = None
        elif self.animation is not None:
            self.image = pygame.Surface(self.SIZE)
            self.animation.play()
        else:
            raise TypeError('At least one of image_file property or make_animation method should be implemented.')
        self.rect = self.image.get_rect()

        self.rect.topleft = x, y
        self.hp = hp

    @property
    def image_file(self) -> Optional[str]:
        return None

    def make_animation(self) -> Optional[pyganim.PygAnimation]:
        return None

    def update(self, *args, **kwargs) -> None:
        if self.animation is not None:
            self.animation.blit(self.image)

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


class Sea(Block):
    def __init__(self, x, y):
        super(Sea, self).__init__(x, y, hp=None)

    def make_animation(self) -> Optional[pyganim.PygAnimation]:
        images = pyganim.getImagesFromSpriteSheet(SEA, rows=1, cols=3, rects=[])
        return pyganim.PygAnimation(list(zip(images, (300, 300, 300))))

