import pygame
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
        self.ICON_WIDTH = 75
        self.ICON_HEIGHT = 75
        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.background = pygame.image.load("assets/bg.png")
        self.background2 = pygame.image.load("assets/ath.png")
        self.pmrblanc = pygame.transform.scale(pygame.image.load("assets/PMRblanc.png"), (self.ICON_WIDTH, self.ICON_HEIGHT))

        self.pmrbleu = pygame.transform.scale(pygame.image.load("assets/PMRbleu.png"),(self.ICON_WIDTH, self.ICON_HEIGHT))
        self.pmrrect = self.pmrbleu.get_rect()
        self.prise = pygame.transform.scale(pygame.image.load("assets/prise.png"),(self.ICON_WIDTH, self.ICON_HEIGHT))
        self.prise_blanc = pygame.transform.scale(pygame.image.load("assets/prise_blanc.png"),(self.ICON_WIDTH, self.ICON_HEIGHT))
        self.iphone = pygame.transform.scale(pygame.image.load("assets/iphone.png"), (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.font = pygame.font.SysFont('Arial', 25)
        pygame.display.set_caption("SPOT FINDER")
        self.BUTTON_WIDTH = 15
        self.button_state = []
        self.advanced_enabled = 0
        self.advanced_enabled = 0
        self.buttons = []
        self.buttons.append(self.pmrblanc)
        self.buttons.append(self.prise_blanc)
        self.blue_prise = 0
        self.pushed = 0
        self.blue_pmr = 0

        self.elc_vis = 0
        self.pmr_vis = 0


    def draw_backboarder(self):
        s = pygame.Surface((self.WINDOW_WIDTH, 140), pygame.SRCALPHA)
        s.fill((200, 200, 200, 0))
        self.window.blit(s, (0, self.WINDOW_HEIGHT - 140))

    def draw_button(self):
        parking_list = decrypt("parking_gen.csv")

        if (self.blue_pmr == 0):
            self.window.blit(self.pmrblanc, (self.WINDOW_WIDTH - self.ICON_WIDTH - 100, self.WINDOW_HEIGHT - self.ICON_HEIGHT - 50))
        else:
            self.window.blit(self.pmrbleu, (
                self.WINDOW_WIDTH - self.ICON_WIDTH - 100, self.WINDOW_HEIGHT - self.ICON_HEIGHT - 50))

        if (self.blue_prise == 0):
            self.window.blit(self.prise_blanc, (self.WINDOW_WIDTH - self.ICON_WIDTH - 300, self.WINDOW_HEIGHT - self.ICON_HEIGHT - 50))
        else:
            self.window.blit(self.prise, (
                self.WINDOW_WIDTH - self.ICON_WIDTH - 300, self.WINDOW_HEIGHT - self.ICON_HEIGHT - 50))

        for parking in parking_list:

            if parking.maxcap / parking.Ocupation > 5:
                # print(parking.maxcap/parking.Ocupation)

                self.draw_cercle(parking.xCoord, parking.yCoord, parking.areaRadius, RED_trns)

            elif parking.maxcap / parking.Ocupation < 5 and parking.maxcap / parking.Ocupation > 3:
                # print(parking.maxcap/parking.Ocupation)
                # print(days_count)

                self.draw_cercle(parking.xCoord, parking.yCoord, parking.areaRadius, GREEN_trns)
            else:

                # print(days_count)
                # print(parking.maxcap/parking.Ocupation)
                self.draw_cercle(parking.xCoord, parking.yCoord, parking.areaRadius, ORANGE_trns)

    def draw_cercle(self, x, y, radius, color):

        circle = pygame.Surface((self.WINDOW_WIDTH*2 , self.WINDOW_HEIGHT*2), pygame.SRCALPHA)
        pygame.draw.circle(circle, color, (x, y), radius)
        self.window.blit(circle, (0, 0))

    def check_button_click(self, eventpos):

        parking_list = decrypt("parking_gen.csv")

        pmrblanc_rect = self.pmrblanc.get_rect()
        pmrblanc_rect.x = self.WINDOW_WIDTH - self.ICON_WIDTH - 100
        pmrblanc_rect.y = self.WINDOW_HEIGHT - self.ICON_HEIGHT - 50


        priseblanc_rect = self.prise_blanc.get_rect()
        priseblanc_rect.x = self.WINDOW_WIDTH - self.ICON_WIDTH - 300
        priseblanc_rect.y = self.WINDOW_HEIGHT - self.ICON_HEIGHT - 50

        if pmrblanc_rect.collidepoint(eventpos):
            self.pushed = 1
            if self.blue_pmr == 1:
                self.blue_pmr = 0
                self.pmr_vis = 0
            else:
                self.blue_pmr = 1
                self.pmr_vis = 1

            #generate_file(790, 175,900, 165, 960, 145, 1045, 90, 420, 220, 1125, 185, 300, 160, 400, 155)

        if priseblanc_rect.collidepoint(eventpos):
            self.pushed = 1

            if self.blue_prise == 1:
                self.blue_prise = 0
                self.elc_vis=0
            else:
                self.blue_prise = 1
                self.elc_vis = 1

        #generate_file(790, 175, 900, 165, 960, 145, 1045, 90, 420, 220, 1125, 185, 300, 160, 400, 155)


                    
    def draw_icon(self):

        if self.elc_vis ==1:
            image_elec = self.prise
            image_elec = pygame.transform.scale(image_elec, (25,25))
            self.window.blit(image_elec, (715,210))
            self.window.blit(image_elec, (415, 195))

        if self.pmr_vis ==1:
            image_pmr = self.pmrbleu
            image_pmr = pygame.transform.scale(image_pmr, (25,25))
            self.window.blit(image_pmr, (790,215))
            self.window.blit(image_pmr, (455, 155))
            self.window.blit(image_pmr, (310, 145))
            self.window.blit(image_pmr, (1090, 170))







RED_trns   = (255,  0,  0, 120)    # red
GREEN_trns = (0  ,255, 0 , 140) #green
ORANGE_trns  = (255  ,128 , 0, 140) #blue
