import pygame
from pygame import draw

from decryptor import decrypt

class Window():

    def __init__(self):
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.WHITE = (255, 255, 255)
        self.WINDOW_WIDTH = 1430
        self.WINDOW_HEIGHT = 780
        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.background = pygame.image.load("assets/bg.png")
        self.font = pygame.font.SysFont('Arial', 20)
        pygame.display.set_caption("SPOT FINDER")
        self.BUTTON_WIDTH = 15
        self.button_state = []
        self.advanced_enabled = 0
        self.advanced_enabled = 1
        self.buttons = []
        self.add_button()

    def draw_advanced_buttons(self, x, y, text):
        pygame.draw.rect(self.window, self.BLACK, pygame.Rect(x, y, self.BUTTON_WIDTH, self.BUTTON_WIDTH),2)

    def draw_toggled_button(self):
        if (self.advanced_enabled == 1):
            pygame.draw.rect(self.window, self.WHITE, (0, self.WINDOW_HEIGHT - 180, self.WINDOW_WIDTH, 200))
            pygame.draw.rect(self.window, self.RED, (0, self.WINDOW_HEIGHT - 20, 50, 20))
            self.window.blit(self.font.render('extra', True, self.BLACK), (5, self.WINDOW_HEIGHT - 20))
        else:
            pygame.draw.rect(self.window, self.RED, (0, self.WINDOW_HEIGHT - 20, 50, 20))
            self.window.blit(self.font.render('extra', True, self.BLACK), (5, self.WINDOW_HEIGHT -20))

    def add_button(self):
        self.buttons.append(Button(0, self.WINDOW_HEIGHT, self.RED,"extra", self.window))
        self.buttons.append((Button(0, self.WINDOW_HEIGHT - 100 ,self.BLACK, "Matin", self.window)))
        self.buttons.append((Button(0,self.WINDOW_HEIGHT - 70, self.BLACK, "Midi", self.window)))
        self.buttons.append((Button(0, self.WINDOW_HEIGHT - 40, self.BLACK, "Soir", self.window)))

    def draw_button(self):
        for button in self.buttons:
            #print(button.coord)
            button.draw_button()

    def draw_cercle(self, x, y, radius, color):
        circle = pygame.Surface((x*2 , y*2 ), pygame.SRCALPHA)
        pygame.draw.circle(circle, color, (x, y), radius)
        self.window.blit(circle, (100, 100))

    
        

class Button():
    def __init__(self,x, y, color, text, window):
        self.state = 0
        self.coord = (x,y)
        self.BUTTON_WIDTH = 15
        self.text = text
        self.color = color
        self.window = window

    def draw_button(self):
        pygame.draw.rect(self.window, self.color, (self.coord[0], self.coord[1], self.BUTTON_WIDTH, self.BUTTON_WIDTH,), 2)

