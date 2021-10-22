from parking import parking
import pygame
import random
from gui import Window

#initialisaiton de pygame et definition de variables nécessaires
pygame.init()


#Parking list for the background :
# parking_list = [

#     parking((1045, 90), random.randint(0, 100), random.randint(1, 4), random.randint(1, 2), 0),
#     parking((960, 145), random.randint(0, 100), random.randint(1, 4), random.randint(1, 2), 0),
#     parking((900, 165), random.randint(0, 100), random.randint(1, 4), random.randint(1, 2), 0),
#     parking((790, 175), random.randint(0, 100), random.randint(1, 4), random.randint(1, 2), 0),
#     parking((400, 175), random.randint(0, 100), random.randint(1, 4), random.randint(1, 2), 0),
#     parking((420, 220), random.randint(0, 100), random.randint(1, 4), random.randint(1, 2), 0),
#     parking((1125, 185), random.randint(0, 100), random.randint(1, 4), random.randint(1, 2), 0),
#     parking((300, 160), random.randint(0, 100), random.randint(1, 4), random.randint(1, 2), 0),
# ]


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