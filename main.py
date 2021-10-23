from parking import parking
import pygame
import random
from gui import Window

#initialisaiton de pygame et definition de variables nécessaires
pygame.init()
RED_trns   = (255,  0,  0,100)    # red
GREEN_trns = (0  ,255, 0 , 100) #green
BLUE_trns  = (0  ,0 , 255, 100) #blue

win = Window()

running = True


while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    win.window.blit(win.background, (0,0))
    win.draw_toggled_button()
    win.draw_button()
    win.draw_cercle(800, 80, 40, RED_trns)
    pygame.display.flip()

