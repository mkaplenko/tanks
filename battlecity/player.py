import pygame
import pyganim
from pygame import constants

from battlecity import Direction, bullets, all_sprites, blocks
from battlecity.bullet import Bullet
from battlecity.config import PLAYER1_IMG_UP, PLAYER1_IMG_DOWN, PLAYER1_IMG_LEFT, PLAYER1_IMG_RIGHT, PLAYER1_IMG_UP2, \
    PLAYER1_IMG_DOWN2, PLAYER1_IMG_LEFT2, PLAYER1_IMG_RIGHT2
from battlecity.events import REFILL_AMMO_EVENT


class Player(pygame.sprite.Sprite):
    SIZE = W, H, = 60, 60
    SPEED = 3
    AMMO_TRUNK_SIZE = 2
    AMMO_PREPARE_SEC = 0.4

    def __init__(self, x, y):
        super(Player, self).__init__()

        self.animations = {
            Direction.UP: pyganim.PygAnimation([(PLAYER1_IMG_UP, 100), (PLAYER1_IMG_UP2, 100)]),
            Direction.DOWN: pyganim.PygAnimation([(PLAYER1_IMG_DOWN, 100), (PLAYER1_IMG_DOWN2, 100)]),
            Direction.LEFT: pyganim.PygAnimation([(PLAYER1_IMG_LEFT, 100), (PLAYER1_IMG_LEFT2, 100)]),
            Direction.RIGHT: pyganim.PygAnimation([(PLAYER1_IMG_RIGHT, 100), (PLAYER1_IMG_RIGHT2, 100)]),
        }

        self.direction = Direction.UP

        self.animation = self.animations[self.direction]
        self.animation.pause()
        self.image = pygame.Surface(self.SIZE)

        self.rect = self.image.get_rect()
        self.rect.topleft = x, y

        self.ammo_count = self.AMMO_TRUNK_SIZE

        self.vx = 0
        self.vy = 0

    def refill_ammo(self):
        self.ammo_count = self.AMMO_TRUNK_SIZE

    def move(self, keys):

        if not keys[constants.K_UP] and not keys[constants.K_DOWN]:
            self.vy = 0
        elif keys[constants.K_UP] and not keys[constants.K_LEFT] and not keys[constants.K_RIGHT]:
            self.vy = -self.SPEED
            self.direction = Direction.UP
            self.animation = self.animations[self.direction]
            self.animation.play()
        elif keys[constants.K_DOWN] and not keys[constants.K_LEFT] and not keys[constants.K_RIGHT]:
            self.vy = self.SPEED
            self.direction = Direction.DOWN
            self.animation = self.animations[self.direction]
            self.animation.play()

        if not keys[constants.K_LEFT] and not keys[constants.K_RIGHT]:
            self.vx = 0
        elif keys[constants.K_LEFT] and not keys[constants.K_UP] and not keys[constants.K_DOWN]:
            self.vx = -self.SPEED
            self.direction = Direction.LEFT
            self.animation = self.animations[self.direction]
            self.animation.play()
        elif keys[constants.K_RIGHT] and not keys[constants.K_UP] and not keys[constants.K_DOWN]:
            self.vx = self.SPEED
            self.direction = Direction.RIGHT
            self.animation = self.animations[self.direction]
            self.animation.play()

        if not keys[constants.K_UP] and not keys[constants.K_DOWN] and not keys[constants.K_LEFT] \
                and not keys[constants.K_RIGHT]:
            self.animation.pause()

    def stop(self):
        self.vy = 0
        self.vx = 0
        self.animation.pause()

    def fire(self):
        if self.ammo_count > 0:
            if self.direction == Direction.UP:
                pos = self.rect.midtop
                pos = pos[0] - 4, pos[1]
            elif self.direction == Direction.DOWN:
                pos = self.rect.midbottom
                pos = pos[0] - 4, pos[1]
            elif self.direction == Direction.LEFT:
                pos = self.rect.midleft
                pos = pos[0], pos[1] - 4
            else:
                pos = self.rect.midright
                pos = pos[0], pos[1] - 4
            bullet = Bullet(*pos, self.direction)
            bullets.add(bullet)
            all_sprites.add(bullet)
            self.ammo_count -= 1
            if self.ammo_count <= 0:
                self.make_refill_ammo_event()

    @classmethod
    def make_refill_ammo_event(cls):
        pygame.time.set_timer(REFILL_AMMO_EVENT, int(cls.AMMO_PREPARE_SEC * 1000), loops=1)

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
        # self.image = self.sprites[self.direction]
        self.animation.blit(self.image)
        self.check_block_collision()
