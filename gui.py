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
        self.iphone = pygame.transform.scale(pygame.image.load("assets/iphone.png"), (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.font = pygame.font.SysFont('Arial', 25)
        pygame.display.set_caption("SPOT FINDER")
        self.BUTTON_WIDTH = 15
        self.button_state = []
        self.advanced_enabled = 0
        self.advanced_enabled = 0   
        self.buttons = []
        self.add_button()


    def add_button(self):

        self.buttons.append((Button(self.WINDOW_WIDTH - 400, self.WINDOW_HEIGHT - 100 ,self.BLACK, "PMR",self.BLACK,  self, 15, 15, 1, 2, 20)))
        self.buttons.append((Button(self.WINDOW_WIDTH - 200, self.WINDOW_HEIGHT - 100, self.BLACK, "Electricité",self.BLACK, self, 15, 15, 1, 2, 20)))

    def draw_backboarder(self):
        s = pygame.Surface((self.WINDOW_WIDTH, 140), pygame.SRCALPHA)
        s.fill((200, 200, 200, 180))
        self.window.blit(s, (0, self.WINDOW_HEIGHT - 140))

    def draw_button(self):
            for button in self.buttons:
                if button.visibility == 1:
                    button.draw_button()
                    button.draw_text()

    def draw_timeline(self):
        i = 150
        while i <= 570:
            pygame.draw.line(self.window, (0, 0, 0), (150, 680), (570, 680), 6)
            pygame.draw.line(self.window, (0, 0, 0), (i, 700), (i, 660), 6)
            i += 35

    def draw_cercle(self, x, y, radius, color):

        circle = pygame.Surface((self.WINDOW_WIDTH*2 , self.WINDOW_HEIGHT*2), pygame.SRCALPHA)
        pygame.draw.circle(circle, color, (x, y), radius)
        self.window.blit(circle, (0, 0))

    def check_button_click(self, pos):
        for button in self.buttons:
            self.button_click(button, pos)

            # ---- displaying color circles 
            parking_list = decrypt("parking_gen.csv")

            for parking in parking_list:
                for hours in parking:
                    
                    if hours.maxcap/hours.Ocupation > 0.66:
                        #print(hours.maxcap/hours.Ocupation)
                        
                        self.draw_cercle(hours.xCoord, hours.yCoord, hours.areaRadius, RED_trns)
                        
                    elif hours.maxcap/hours.Ocupation < 0.66 and hours.maxcap/hours.Ocupation > 0.33:
                        #print(hours.maxcap/hours.Ocupation)
                        #print(days_count)
                        
                        self.draw_cercle(hours.xCoord, hours.yCoord, hours.areaRadius, GREEN_trns)
                    else:
                        
                        #print(days_count)
                        #print(hours.maxcap/hours.Ocupation)
                        self.draw_cercle(hours.xCoord, hours.yCoord, hours.areaRadius, ORANGE_trns)


        else:
            self.advanced_enabled = 0
        generate_file(790, 175,900, 165, 960, 145, 1045, 90, 420, 220, 1125, 185, 300, 160, 400, 155)
        
        


    def button_click(self,button, pos):
        parking_list = decrypt("parking_gen.csv")
        if (pos[0] > button.coord[0] and pos[0] < button.coord[0]+button.BUTTON_WIDTH):
            if (pos[1] > button.coord[1] and pos[1] < button.coord[1] + button.BUTTON_WIDTH):
                if button.pushed == 0:
                    button.pushed = 1
                    """for parking in parking_list:
                        for hours in parking:
                            
                            if hours.maxcap/hours.Ocupation > 0.66:
                                #print(hours.maxcap/hours.Ocupation)
                                
                                self.draw_cercle(hours.xCoord, hours.yCoord, hours.areaRadius, RED_trns)
                                
                            elif hours.maxcap/hours.Ocupation < 0.66 and hours.maxcap/hours.Ocupation > 0.33:
                                #print(hours.maxcap/hours.Ocupation)
                                #print(days_count)
                                
                                self.draw_cercle(hours.xCoord, hours.yCoord, hours.areaRadius, GREEN_trns)
                            else:
                                
                                #print(days_count)
                                #print(hours.maxcap/hours.Ocupation)
                                self.draw_cercle(hours.xCoord, hours.yCoord, hours.areaRadius, ORANGE_trns)
                  """
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
        parking_list = decrypt("parking_gen.csv")
        if self.pushed == 1:
            pygame.draw.rect(self.window.window, self.window.GREEN, (self.coord[0], self.coord[1], self.BUTTON_WIDTH, self.BUTTON_HEIGHT), 0)
            # --- drawing circles
            for parking in parking_list:
                for hours in parking:
                    print(hours.maxcap/hours.Ocupation)
                    if hours.maxcap/hours.Ocupation > 5:
                        #print(hours.maxcap/hours.Ocupation)
                        
                        self.window.draw_cercle(hours.xCoord, hours.yCoord, hours.areaRadius, RED_trns)
                        
                    elif hours.maxcap/hours.Ocupation < 5 and hours.maxcap/hours.Ocupation > 2:
                        #print(hours.maxcap/hours.Ocupation)
                        #print(days_count)
                        
                        self.window.draw_cercle(hours.xCoord, hours.yCoord, hours.areaRadius, GREEN_trns)
                    else:
                        
                        #print(days_count)
                        #print(hours.maxcap/hours.Ocupation)
                        self.window.draw_cercle(hours.xCoord, hours.yCoord, hours.areaRadius, ORANGE_trns)

        pygame.draw.rect(self.window.window, self.color,(self.coord[0], self.coord[1], self.BUTTON_WIDTH, self.BUTTON_HEIGHT), self.filled)

    def draw_text(self):
        self.window.window.blit(self.window.font.render(self.text, True, self.window.BLACK), (self.coord[0] + self.offset, self.coord[1] - 5))


RED_trns   = (255,  0,  0, 100)    # red
GREEN_trns = (0  ,255, 0 , 100) #green
ORANGE_trns  = (255  ,128 , 0, 128) #blue
