"""
Created the check_events() and update_screen() methods in pinball.py. Added movement to the flipper for left and right arrows
"""


import sys, pygame
from flipper import Flipper
from settings import Settings


class Game:
	""" This class initializes pygame and the game """
	def __init__(self):
		pygame.init()
		# Creates a Settings instance
		self.settings = Settings()
		# Initialize screen
		self.screen = pygame.display.set_mode((self.settings.screen_size))
		pygame.display.set_caption(self.settings.screen_caption)
		# Creates a Flipper instance. (we pass 'self' so we can create the screen in Flipper __init__())
		self.flipper = Flipper(self)


	def check_events(self):
		""" Checks for key presses """
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					self.flipper.rect.x += self.settings.flipper_speed
				elif event.key == pygame.K_LEFT:
					self.flipper.rect.x -= self.settings.flipper_speed


	def update_screen(self):
		""" Updates screen """
		# Fill screen with color
		self.screen.fill(self.settings.screen_color)
		# Blits the flipper on screen
		self.flipper.blitme()
		# Update the full display Surface to the screen
		pygame.display.flip()


	def run_game(self):
		""" Main loop of the game """
		while True:
			self.check_events()
			self.update_screen()


def main():
	pinball = Game()
	pinball.run_game()


if __name__ == "__main__": main()