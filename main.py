from parking import parking as pk
import pygame


#initialisaiton de pygame et definition de variables nécessaires
pygame.init()


running = True
pygame.display.set_caption("IDETA")

while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    window.blit(background, (0,0))
    pygame.display.flip()
