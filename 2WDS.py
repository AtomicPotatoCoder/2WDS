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
	button = pygame.Rect(310, 270, 200, 50)
	button_font = pygame.font.SysFont("Times New Roman", 25)

	screen = "start"

	def __init__(self):
		pygame.display.set_caption("2W Druk Spil")
		self.gameDisplay.fill(self.violet)
		pygame.display.set_caption("2W Druk Spil")
		Title = self.title_font.render("2W Druk Spil", 1, (0,0,0))
		self.gameDisplay.blit(Title, (300,200))
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			if self.screen == "start":
				self.start_screen()
			if self.screen == "test":
				self.test_screen()
	
	def test_screen(self):
		print("TEST")
		pygame.display.update()

	def start_screen(self):
		print("START")
		pygame.draw.rect(self.gameDisplay, [250, 250, 250], self.button)
		self.start_button_text = self.button_font.render("Start Spillet", 1, (0,0,0))
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONUP:
					if self.button.collidepoint(event.pos):
						self.screen = "test"
						return
			self.gameDisplay.blit(self.start_button_text, (350, 280))
			pygame.display.update()

if __name__ == '__main__':
	game = Game()

pygame.quit()
quit()
