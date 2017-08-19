import pygame

#test

pygame.init()

violet = (255, 0, 150)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("2W Druk Spil")

pygame.display.update()

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    gameDisplay.fill(violet)
    pygame.display.update()

pygame.quit()
quit()
