import pygame

class Window():

    def __init__(self):
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.WINDOW_WIDTH = 1430
        self.WINDOW_HEIGHT = 780
        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.background = pygame.image.load("assets/bg.png")
        self.font = pygame.font.SysFont('Arial', 20)
        pygame.display.set_caption("SPOT FINDER")
        self.BUTTON_WIDTH = 15
        self.button_state = []
        self.advanced_enabled = 0

    def draw_advanced_buttons(self, x, y, text):
        pygame.draw.rect(self.window, self.BLACK, pygame.Rect(x, y, self.BUTTON_WIDTH, self.BUTTON_WIDTH),2)

    def draw_toggled_button(self):
        if (self.advanced_enabled == 1):
            self.draw_advanced_buttons()
        else:
            pygame.draw.rect(self.window, self.RED, (0, self.WINDOW_HEIGHT - 20, 50, 20))
            self.window.blit(self.font.render('extra', True, self.BLACK), (5, self.WINDOW_HEIGHT -20))





