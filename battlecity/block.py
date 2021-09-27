import pygame
from pygame import constants

from battlecity.config import WALL_IMG


class Block(pygame.sprite.Sprite):
    SIZE = W, H, = 30, 30

    def __init__(self, x, y):
        super(Block, self).__init__()
        self.x = x
        self.y = y

        self.image = pygame.image.load(WALL_IMG).convert()
        self.image.set_colorkey((0, 0, 0), constants.RLEACCEL)
        self.rect = self.image.get_rect()

        self.rect.topleft = x, y
        self.hp = 1

    def kill(self) -> None:
        self.hp -= 1
        if self.hp <= 0:
            super(Block, self).kill()
