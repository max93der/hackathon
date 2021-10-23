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
    win.window.blit(win.background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            win.check_button_click(pos)
    

    win.draw_button()
    pygame.display.flip()
