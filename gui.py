import pygame
from pygame import draw
from pygame.draw import circle
from generator import generate_file
from decryptor import decrypt

class Window():

    def __init__(self):
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0,255, 0)
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
        self.advanced_enabled = 0
        self.buttons = []
        self.add_button()


    def add_button(self):
        self.buttons.append(Button(0, self.WINDOW_HEIGHT - 20, self.RED ,"Extra ",self.WHITE, self, 50, 20, 1, 0, 5))
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

    def check_button_click(self, pos):
        for button in self.buttons:
            self.button_click(button, pos)
        if self.buttons[0].pushed == 1:
            self.advanced_enabled = 1
        else:
            self.advanced_enabled = 0


    def button_click(self,button, pos):
        if (pos[0] > button.coord[0] and pos[0] < button.coord[0]+button.BUTTON_WIDTH):
            if (pos[1] > button.coord[1] and pos[1] < button.coord[1] + button.BUTTON_WIDTH):
                if button.pushed == 0:
                    button.pushed = 1
                    generate_file()
                    parking_list = decrypt("parking_gen.csv")
                    print("generated")
                    for parking in parking_list:
                        print("intopk")
                        if parking.noonOCC/parking.maxcap > 0.66:
                            self.draw_cercle(parking.xCoord, parking.yCoord, parking.areaRadius, RED_trns)

                        elif parking.noonOCC/parking.maxcap < 0.66 and parking.noonOCC/parking.maxcap > 0.33:

                            self.draw_cercle(parking.xCoord, parking.yCoord, parking.areaRadius, GREEN_trns)
                        else:
                            self.draw_cercle(parking.xCoord, parking.yCoord, parking.areaRadius, ORANGE_trns)
                else:
                    button.pushed = 0



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
        self.pushed = 0

    def draw_button(self):
        if self.pushed == 1:
            pygame.draw.rect(self.window.window, self.window.GREEN, (self.coord[0], self.coord[1], self.BUTTON_WIDTH, self.BUTTON_HEIGHT), 0)
        pygame.draw.rect(self.window.window, self.color, (self.coord[0], self.coord[1], self.BUTTON_WIDTH, self.BUTTON_HEIGHT), self.filled)


    def draw_text(self):
        self.window.window.blit(self.window.font.render(self.text, True, self.window.BLACK), (self.coord[0] + self.offset, self.coord[1] - 5))


RED_trns   = (255,  0,  0, 100)    # red
GREEN_trns = (0  ,255, 0 , 100) #green
ORANGE_trns  = (255  ,128 , 0, 128) #blue