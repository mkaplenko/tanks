import os

import pygame
from pygame import constants

from battlecity.config import DATA_DIR
from battlecity.game import Game
from battlecity.player import Player, Direction
from battlecity.block import Block

pygame.init()
WINDOW_SIZE = WIDTH, HEIGHT = 1560, 960
LEVEL_FILENAME = 'test-level.map'

clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
enemies = pygame.sprite.Group()
blocks = pygame.sprite.Group()


def main():
    game = Game(*WINDOW_SIZE)
    game.start()

    # Render level
    with open(os.path.join(DATA_DIR, LEVEL_FILENAME)) as fd:
        map_data = fd.readlines()

    cords = 0, 0
    for row in map_data:
        for el in row:
            if el == '0':
                bl = Block(*cords)
                all_sprites.add(bl)
                blocks.add(bl)
            cords = cords[0] + Block.SIZE[0], cords[1]
        cords = 0, cords[1] + Block.SIZE[1]

    player = Player(WINDOW_SIZE[0] / 2 - 60 * 3, WINDOW_SIZE[1] - 60 * 2)
    all_sprites.add(player)
    players.add(player)

    while game.is_running():
        block_collided = pygame.sprite.spritecollideany(player, blocks)
        if block_collided:
            if player.direction == Direction.UP:
                player.rect.top = block_collided.rect.bottom
            elif player.direction == Direction.DOWN:
                player.rect.bottom = block_collided.rect.top
            elif player.direction == Direction.LEFT:
                player.rect.left = block_collided.rect.right
            elif player.direction == Direction.RIGHT:
                player.rect.right = block_collided.rect.left

            player.stop()
        for event in pygame.event.get():
            if event.type == constants.QUIT:
                game.quit()
            if event.type == constants.KEYDOWN:
                player.move(pygame.key.get_pressed())
            if event.type == constants.KEYUP:
                player.move(pygame.key.get_pressed())

        game.screen.fill((0, 0, 0))
        all_sprites.draw(game.screen)
        all_sprites.update()
        pygame.display.update()
        clock.tick(40)
    pygame.quit()


if __name__ == '__main__':
    main()
