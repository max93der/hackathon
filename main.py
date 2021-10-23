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
win2 = Window()

running = True
Ensart = False
Enville = True
#display the first datas
parking_list = decrypt("parking_gen.csv")

for parking in parking_list:
    
    if parking.maxcap/parking.Ocupation > 0.66:
        #print(parking.maxcap/parking.Ocupation)
        
        win.draw_cercle(parking.xCoord, parking.yCoord, parking.areaRadius, RED_trns)
        
    elif parking.maxcap/parking.Ocupation < 0.66 and parking.maxcap/parking.Ocupation > 0.33:
        #print(parking.maxcap/parking.Ocupation)
        #print(days_count)
        
        win.draw_cercle(parking.xCoord, parking.yCoord, parking.areaRadius, GREEN_trns)
    else:
        
        #print(days_count)
        #print(parking.maxcap/parking.Ocupation)
        win.draw_cercle(parking.xCoord, parking.yCoord, parking.areaRadius, ORANGE_trns)



while (running):
    while Ensart:
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
    while Enville:
        win2.window.blit(win2.background2, (0,0))
        win2.draw_backboarder()
        win2.window.blit(win2.iphone, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                
                win2.check_button_click(pos)
        
        win2.draw_timeline()
        win2.draw_button()
        pygame.display.flip()
        