from decryptor import decrypt
from generator import generate_file
from parking import parking
import pygame
import random
from gui import Button, Window

#initialisaiton de pygame et definition de variables nécessaires
pygame.init()

RED_trns   = (255,  0,  0, 100)    # red
GREEN_trns = (0  ,255, 0 , 100) #green
ORANGE_trns  = (255  ,128 , 0, 128) #blue

generate_file(1, 2,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)

win = Window()

running = True
#display the first datas
parking_list = decrypt("parking_gen.csv")

print(parking_list[0][0][0].name)

while (running):
    win.window.blit(win.background, (0,0))
    win.draw_backborder()
    win.window.blit(win.iphone, (0, 0))

    """"#displaying initial data
    for parking in parking_list:
        for days in parking:
            for hours in days:
                if hours.Ocupation/hours.Ocupation > 0.66:
                    pass
                    #win.draw_cercle(hours.xCoord, hours.yCoord, hours.areaRadius, RED_trns)

                elif hours.Ocupation/hours.maxcap < 0.66 and hours.Ocupation/hours.maxcap > 0.33:
                    pass
                    #win.draw_cercle(hours.xCoord, hours.yCoord, hours.areaRadius, GREEN_trns)
                else:
                    pass
                    #win.draw_cercle(hours.xCoord, hours.yCoord, hours.areaRadius, ORANGE_trns)
"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            win.check_button_click(pos)
    

    win.draw_button()
    pygame.display.flip()
