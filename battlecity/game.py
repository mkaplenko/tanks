from typing import Optional

import pygame
from pygame import constants

from battlecity import all_sprites, players, blocks, Direction
from battlecity.level import Level
from battlecity.player import Player


class Game:
    def __init__(self, width, height):
        self.w_size = self.w_width, self.w_height = width, height
        self.running = False
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.w_size)
        self.level: Level = Level()
        self.player: Optional[Player] = None

        pygame.display.set_caption('Battle tanks')

    def start(self):
        self.render_level()
        player = Player(self.w_width / 2 - 60 * 3, self.w_height - 60 * 2)
        all_sprites.add(player)
        players.add(player)
        self.player = player
        self.running = True
        while self.is_running():
            self.make_scene()
        pygame.quit()

    def stop(self):
        self.running = False

    def is_running(self):
        return self.running

    def render_level(self):
        self.level.render_map()

    def make_scene(self):
        for event in pygame.event.get():
            if event.type == constants.QUIT:
                self.stop()
            if event.type == constants.KEYDOWN:
                if event.key == constants.K_SPACE:
                    self.player.fire()
                else:
                    self.player.move(pygame.key.get_pressed())
            if event.type == constants.KEYUP:
                self.player.move(pygame.key.get_pressed())

        self.screen.fill((0, 0, 0))
        all_sprites.draw(self.screen)
        all_sprites.update()
        pygame.display.update()
        self.clock.tick(40)
