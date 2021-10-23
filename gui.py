import pygame
from pygame import draw
from pygame.draw import circle

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


    def add_button(self):
        self.buttons.append(Button(0, self.WINDOW_HEIGHT - 20, self.RED ,"Extra",self.WHITE, self, 50, 20, 1, 0, 5))
        self.buttons.append((Button(0, self.WINDOW_HEIGHT - 100 ,self.BLACK, "Matin",self.BLACK,  self, 15, 15, 1, 2, 20)))
        self.buttons.append((Button(0,self.WINDOW_HEIGHT - 70, self.BLACK, "Midi",self.BLACK, self, 15, 15, 1, 2, 20)))
        self.buttons.append((Button(0, self.WINDOW_HEIGHT - 40, self.BLACK, "Soir",self.BLACK, self, 15, 15, 1, 2, 20)))

    def draw_button(self):
        if self.advanced_enabled == 1:
            pygame.draw.rect(self.window, self.WHITE, (0, self.WINDOW_HEIGHT - 180, self.WINDOW_WIDTH, 200))
            for button in self.buttons[1:]:
                if button.visibility == 1:
                    button.draw_button()
                    button.draw_text()

        self.buttons[0].draw_button()
        self.buttons[0].draw_text()

    def draw_cercle(self, x, y, radius, color):

        circle = pygame.Surface((self.WINDOW_WIDTH*2 , self.WINDOW_HEIGHT*2), pygame.SRCALPHA)
        pygame.draw.circle(circle, color, (x, y), radius)
        self.window.blit(circle, (0, 0))

    
        

class Button():
    def __init__(self,x, y, color, text, text_color, window, BUTTON_WIDTH, BUTTON_HEIGHT, visivility, filled, offset):

        self.coord = (x,y)
        self.text = text
        self.color = color
        self.window = window
        self.text_color = text_color
        self.BUTTON_WIDTH = BUTTON_WIDTH
        self.BUTTON_HEIGHT = BUTTON_HEIGHT
        self.visibility = visivility
        self.filled = filled
        self.offset = offset

    def draw_button(self):
        pygame.draw.rect(self.window.window, self.color, (self.coord[0], self.coord[1], self.BUTTON_WIDTH, self.BUTTON_HEIGHT), self.filled)


    def draw_text(self):
        self.window.window.blit(self.window.font.render(self.text, True, self.window.BLACK), (self.coord[0] + self.offset, self.coord[1] - 5))

    def button_click(coord, state, width, event):
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            if pos(0)>coord(0) and pos(0)<coord(0) + width:
                if pos(1)>coord(1) and pos(1)<coord(1) + width:

                    if state == 1:
                        state = 0
                    if state == 0:
                        state = 1

        return state