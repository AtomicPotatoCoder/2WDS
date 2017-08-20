import pygame

#test

pygame.init()
pygame.font.init()

violet = (255, 0, 150)
black = (0, 0, 0)
white = (250, 250, 250)
light_gray = (190, 190, 190)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("2W Druk Spil")

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    gameDisplay.fill(violet)
    #Title layout
    Title_text = pygame.font.SysFont("Merryweather", 50)
    Title = Title_text.render("2W Druk Spil", 1, (0,0,0))
    gameDisplay.blit(Title, (300,200))
    #Button interaction color
    mouse = pygame.mouse.get_pos()
    
    if 310+200 > mouse[0] > 310 and 270+50 > mouse[1] > 270:
        pygame.draw.rect(gameDisplay, light_gray, [310, 270, 200, 50])
    else:
        pygame.draw.rect(gameDisplay, white, [310, 270, 200, 50])
    #Start button text
    start_button = pygame.font.SysFont("Times New Roman", 25)
    StartButton = start_button.render("Start Spillet", 1, (0,0,0))
    gameDisplay.blit(StartButton, (350, 280))

    pygame.display.update()

pygame.quit()
quit()
