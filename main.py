from parking import parking
import pygame
import random
from gui import Window

#initialisaiton de pygame et definition de variables nécessaires
pygame.init()


#Parking list for the background :

parking_list = []

parking_list.append()

def fill_parking_data(x_coord, y_coord, pk_list):
    pk_list.append(parking((x_coord, y_coord), random.randint(0, 100), random.randint(1, 4), random.randint(1, 2), 0))
    return pk_list
    
    
win = Window()

running = True


while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    win.window.blit(win.background, (0,0))
    pygame.display.flip()
