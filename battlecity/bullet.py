import pygame

from battlecity.game import Direction


class Bullet(pygame.sprite.Sprite):
    vsize = (5, 10)
    hsize = (10, 5)
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

    def update(self, *args, **kwargs) -> None:
        if self.direction == Direction.UP:
            self.rect.move_ip(0, -self.speed)
        elif self.direction == Direction.DOWN:
            self.rect.move_ip(0, self.speed)
        elif self.direction == Direction.LEFT:
            self.rect.move_ip(-self.speed, 0)
        elif self.direction == Direction.RIGHT:
            self.rect.move_ip(self.speed, 0)
