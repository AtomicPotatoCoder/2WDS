import pygame
import sys

pygame.init()
pygame.font.init()

class Game():
	violet = (255, 0, 150)
	black = (0, 0, 0)
	white = (250, 250, 250)
	light_gray = (190, 190, 190)

	gameDisplay = pygame.display.set_mode((800,600))
	title_font = pygame.font.SysFont("Merryweather", 50)
	button = pygame.Rect(100, 100, 50, 50)
	button_font = pygame.font.SysFont("Times New Roman", 25)

	def __init__(self):
		pygame.display.set_caption("2W Druk Spil")
		self.gameDisplay.fill(self.violet)
		pygame.display.set_caption("2W Druk Spil")
		Title = self.title_font.render("2W Druk Spil", 1, (0,0,0))
		self.gameDisplay.blit(Title, (300,200))
		self.start_screen()

	def start_screen(self):
		pygame.draw.rect(self.gameDisplay, [255, 0, 0], self.button)
		self.StartButton = self.button_font.render("Start Spillet", 1, (0,0,0))
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONUP:
					if self.button.collidepoint(event.pos):
						print("collide")

    		#Button interaction color
			mouse = pygame.mouse.get_pos()
			if 310+200 > mouse[0] > 310 and 270+50 > mouse[1] > 270:
				pygame.draw.rect(self.gameDisplay, self.light_gray, [310, 270, 200, 50])
			else:
				pygame.draw.rect(self.gameDisplay, self.white, [310, 270, 200, 50])

    		#Start button text
			self.gameDisplay.blit(self.StartButton, (350, 280))

			pygame.display.update()

if __name__ == '__main__':
	game = Game()

pygame.quit()
quit()
