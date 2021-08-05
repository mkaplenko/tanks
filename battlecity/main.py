import pygame
from battlecity.game import Game

pygame.init()
WINDOW_SIZE = WIDTH, HEIGHT = 1560, 960


def main():
    game = Game(*WINDOW_SIZE)
    game.start()


if __name__ == '__main__':
    main()
