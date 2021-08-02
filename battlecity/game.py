import pygame


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
