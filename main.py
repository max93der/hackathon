from parking import parking as pk
import pygame

# initialisation des variables
BLACK = (0,0,0)
WINDOW_WIDTH = 1430
WINDOW_HEIGHT = 780

#initialisaiton de pygame et definition de variables nécessaires
pygame.init()


running = True
window = pygame.display.set_mode((WINDOW_WIDTH ,WINDOW_HEIGHT))
background = pygame.image.load("assets/bg.png")
pygame.display.set_caption("IDETA")

while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    window.blit(background, (0,0))
    pygame.display.flip()
