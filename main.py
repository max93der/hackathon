from parking import parking
import pygame
import random
from gui import Window

#initialisaiton de pygame et definition de variables nécessaires
pygame.init()

win = Window()

running = True


while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    win.window.blit(win.background, (0,0))
    win.draw_advanced_buttons(5, 100, "tetx")
    win.draw_toggled_button()
    pygame.display.flip()


#test
