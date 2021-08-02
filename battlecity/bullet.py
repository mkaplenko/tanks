import pygame

from battlecity.game import Direction


class Bullet(pygame.sprite.Sprite):
    size = (5, 5)
    speed = 5

    def __init__(self, x: int, y: int, direction: Direction) -> None:
        super(Bullet, self).__init__()
        self.image = pygame.surface.Surface(Bullet.size)
        self.image.fill(pygame.Color("#FF524A"))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction: Direction = direction

    def update(self, *args, **kwargs) -> None:
        if self.direction == Direction.UP:
            self.rect.move_ip(0, -self.speed)
        elif self.direction == Direction.DOWN:
            self.rect.move_ip(0, self.speed)
        elif self.direction == Direction.LEFT:
            self.rect.move_ip(-self.speed, 0)
        elif self.direction == Direction.RIGHT:
            self.rect.move_ip(self.speed, 0)
