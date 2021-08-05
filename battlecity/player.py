import pygame
from pygame import constants

from battlecity import Direction, bullets, all_sprites, blocks
from battlecity.bullet import Bullet
from battlecity.config import PLAYER1_IMG_UP, PLAYER1_IMG_DOWN, PLAYER1_IMG_LEFT, PLAYER1_IMG_RIGHT


class Player(pygame.sprite.Sprite):
    SIZE = W, H, = 60, 60
    SPEED = 3

    def __init__(self, x, y):
        super(Player, self).__init__()

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

    def fire(self):
        if self.direction == Direction.UP:
            pos = self.rect.midtop
            pos = pos[0] - 2, pos[1]
        elif self.direction == Direction.DOWN:
            pos = self.rect.midbottom
            pos = pos[0] - 2, pos[1]
        elif self.direction == Direction.LEFT:
            pos = self.rect.midleft
            pos = pos[0], pos[1] - 2
        else:
            pos = self.rect.midright
            pos = pos[0], pos[1] - 2
        bullet = Bullet(*pos, self.direction)
        bullets.add(bullet)
        all_sprites.add(bullet)

    def check_block_collision(self):
        block_collided = pygame.sprite.spritecollideany(self, blocks)
        if block_collided:
            if self.direction == Direction.UP:
                self.rect.top = block_collided.rect.bottom
            elif self.direction == Direction.DOWN:
                self.rect.bottom = block_collided.rect.top
            elif self.direction == Direction.LEFT:
                self.rect.left = block_collided.rect.right
            elif self.direction == Direction.RIGHT:
                self.rect.right = block_collided.rect.left

            self.stop()

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        self.image = self.sprites[self.direction]
        self.check_block_collision()
