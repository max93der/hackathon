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

generate_file(790, 175,900, 165, 960, 145, 1045, 90, 420, 220, 1125, 185, 300, 160, 400, 155)

win = Window()

running = True
#display the first datas
parking_list = decrypt("parking_gen.csv")

    
for parking in parking_list:
    for hours in parking:
        
        if hours.maxcap/hours.Ocupation > 0.66:
            #print(hours.maxcap/hours.Ocupation)
            
            win.draw_cercle(hours.xCoord, hours.yCoord, hours.areaRadius, RED_trns)
            
        elif hours.maxcap/hours.Ocupation < 0.66 and hours.maxcap/hours.Ocupation > 0.33:
            #print(hours.maxcap/hours.Ocupation)
            #print(days_count)
            
            win.draw_cercle(hours.xCoord, hours.yCoord, hours.areaRadius, GREEN_trns)
        else:
            
            #print(days_count)
            #print(hours.maxcap/hours.Ocupation)
            win.draw_cercle(hours.xCoord, hours.yCoord, hours.areaRadius, ORANGE_trns)



while (running):
    win.window.blit(win.background, (0,0))
    win.draw_backboarder()
    win.window.blit(win.iphone, (0, 0))

    #displaying initial data
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            win.check_button_click(pos)
    
    win.draw_timeline()
    win.draw_button()
    pygame.display.flip()
