from parking import parking
import pygame
from gui import Window

#initialisaiton de pygame et definition de variables nécessaires
pygame.init()

<<<<<<< HEAD
pk = pk
=======
win = Window()
>>>>>>> 13baabb03d3dc6fba158c6061afd52c32699ce73

running = True


while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    win.window.blit(win.background, (0,0))
    pygame.display.flip()
