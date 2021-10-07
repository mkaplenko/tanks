import pygame
import pyganim

from battlecity import Direction, bullet_blocks, all_sprites
from battlecity.config import HIT_SPRITES


class Hit(pygame.sprite.Sprite):
    SIZE = (50, 50)

    def __init__(self, x: int, y: int):
        super(Hit, self).__init__()
        self.image = pygame.surface.Surface(self.SIZE)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

        images = pyganim.getImagesFromSpriteSheet(HIT_SPRITES, rows=1, cols=3, rects=[])
        self.anim = pyganim.PygAnimation(list(zip(images, (50, 50, 50))))
        self.anim.loop = False
        self.anim.play()

    def update(self, *args, **kwargs) -> None:
        self.anim.blit(self.image, (0, 0))
        if self.anim.state == pyganim.STOPPED:
            self.kill()

    def check_block_collide(self):
        block = pygame.sprite.spritecollideany(self, bullet_blocks)
        if block:
            block.kill()


class Bullet(pygame.sprite.Sprite):
    vsize = (8, 15)
    hsize = (15, 8)
    speed = 7

    def __init__(self, x: int, y: int, direction: Direction) -> None:
        super(Bullet, self).__init__()
        self.direction: Direction = direction
        if direction in (Direction.RIGHT, Direction.LEFT):
            size = Bullet.hsize
        else:
            size = Bullet.vsize
        self.image = pygame.surface.Surface(size)
        self.image.fill(pygame.Color((255, 255, 255)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def check_block_collide(self):
        block = pygame.sprite.spritecollideany(self, bullet_blocks)
        if block:
            self.kill()
            hit = Hit(*block.rect.topleft)
            all_sprites.add(hit)
            block.kill()

    def update(self, *args, **kwargs) -> None:
        if self.direction == Direction.UP:
            self.rect.move_ip(0, -self.speed)
        elif self.direction == Direction.DOWN:
            self.rect.move_ip(0, self.speed)
        elif self.direction == Direction.LEFT:
            self.rect.move_ip(-self.speed, 0)
        elif self.direction == Direction.RIGHT:
            self.rect.move_ip(self.speed, 0)
        self.check_block_collide()
