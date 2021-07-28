import enum
import http

import pygame
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_LEFT, K_RIGHT, K_UP, K_DOWN, RLEACCEL

pygame.init()
WINDOW_SIZE = WIDTH, HEIGHT = 1560, 960
# screen = pygame.display.set_mode(WINDOW_SIZE)

clock = pygame.time.Clock()


class Direction(enum.IntEnum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Block(pygame.sprite.Sprite):
    SIZE = W, H, = 30, 30
    # COLOR = pygame.Color("#FF524A")

    def __init__(self, x, y):
        super(Block, self).__init__()
        self.x = x
        self.y = y

        # self.image = pygame.Surface(Block.SIZE)
        self.image = pygame.image.load('data/img/wall.bmp').convert()
        self.image.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.image.get_rect()

        self.rect.topleft = x, y
        # self.image.fill(Block.COLOR)

    def __repr__(self):
        return f"Block({self.x}, {self.y})"


class Player(pygame.sprite.Sprite):
    SIZE = W, H, = 60, 60
    # COLOR = pygame.Color("#6288FA")
    SPEED = 3

    def __init__(self, x, y):
        super(Player, self).__init__()
        # self.image = pygame.Surface(Player.SIZE)

        self.sprites = {
            Direction.UP: pygame.image.load('data/img/p1-little-up.bmp').convert(),
            Direction.DOWN: pygame.image.load('data/img/p1-little-down.bmp').convert(),
            Direction.LEFT: pygame.image.load('data/img/p1-little-left.bmp').convert(),
            Direction.RIGHT: pygame.image.load('data/img/p1-little-right.bmp').convert(),
        }

        self.direction = Direction.UP

        self.image = self.sprites[self.direction]
        self.rect = self.image.get_rect()

        self.rect.topleft = x, y
        # self.image.fill(Player.COLOR)

        self.vx = 0
        self.vy = 0

    def move(self, keys):
        if not keys[K_UP] and not keys[K_DOWN]:
            self.vy = 0
        elif keys[K_UP] and not keys[K_LEFT] and not keys[K_RIGHT]:
            self.vy = -self.SPEED
            self.direction = Direction.UP
        elif keys[K_DOWN] and not keys[K_LEFT] and not keys[K_RIGHT]:
            self.vy = self.SPEED
            self.direction = Direction.DOWN

        if not keys[K_LEFT] and not keys[K_RIGHT]:
            self.vx = 0
        elif keys[K_LEFT] and not keys[K_UP] and not keys[K_DOWN]:
            self.vx = -self.SPEED
            self.direction = Direction.LEFT
        elif keys[K_RIGHT] and not keys[K_UP] and not keys[K_DOWN]:
            self.vx = self.SPEED
            self.direction = Direction.RIGHT

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        self.image = self.sprites[self.direction]


class Game:
    def __init__(self, width, height):
        self.w_size = self.w_width, self.w_height = width, height
        self.running = False
        self.screen = pygame.display.set_mode(self.w_size)
        pygame.display.set_caption('Battle tanks')

    def start(self):
        self.running = True

    def quit(self):
        self.running = False

    def is_running(self):
        return self.running


game = Game(*WINDOW_SIZE)
game.start()


with open('test-level.map') as fd:
    map_data = fd.readlines()

cords = 0, 0
blocks = []
for row in map_data:
    for el in row:
        if el == '0':
            bl = Block(*cords)
            blocks.append(bl)
        cords = cords[0] + Block.SIZE[0], cords[1]
    cords = 0, cords[1] + Block.SIZE[1]

player = Player(WINDOW_SIZE[0] / 2 - 60 * 3, WINDOW_SIZE[1] - 60 * 2)


while game.is_running():
    for event in pygame.event.get():
        if event.type == QUIT:
            game.quit()
        if event.type == KEYDOWN:
            player.move(pygame.key.get_pressed())
        if event.type == KEYUP:
            player.move(pygame.key.get_pressed())

    # player.move(pygame.key.get_pressed())

    game.screen.fill((0, 0, 0))

    block = pygame.Surface((60, 60))
    block.fill(pygame.Color("#FB4D3B"))

    for bl in blocks:
        game.screen.blit(bl.image, bl.rect)

    player.update()
    game.screen.blit(player.image, player.rect)

    pygame.display.flip()
    clock.tick(40)
