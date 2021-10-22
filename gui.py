import pygame

class Window():

    def __init__(self):
        self.BLACK = (0, 0, 0)
        self.WINDOW_WIDTH = 1430
        self.WINDOW_HEIGHT = 780
        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.background = pygame.image.load("assets/bg.png")
        pygame.display.set_caption("SPOT FINDER")
