from decryptor import decrypt
from generator import generate_file
from parking import parking
import pygame
import random
from gui import Window

#initialisaiton de pygame et definition de variables nécessaires
pygame.init()
RED_trns   = (255,  0,  0, 100)    # red
GREEN_trns = (0  ,255, 0 , 100) #green
ORANGE_trns  = (255  ,128 , 0, 128) #blue

generate_file()
parking_list = decrypt("parking_gen.csv")
win = Window()

running = True


while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            win.check_button_click(pos)
    win.window.blit(win.background, (0,0))

   # draw all parlkings on the map
    
    # for parking in parking_list:
    #     if parking.noonOCC/parking.maxcap > 0.66:
    #         win.draw_cercle(parking.xCoord, parking.yCoord, parking.areaRadius, RED_trns)

    #     elif parking.noonOCC/parking.maxcap < 0.66 and parking.noonOCC/parking.maxcap > 0.33:

    #         win.draw_cercle(parking.xCoord, parking.yCoord, parking.areaRadius, GREEN_trns)
    #     else:
           
    #         win.draw_cercle(parking.xCoord, parking.yCoord, parking.areaRadius, ORANGE_trns)

    win.draw_button()
    pygame.display.flip()
