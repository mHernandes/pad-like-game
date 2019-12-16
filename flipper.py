import pygame
from settings import Settings


class Flipper:
	""" A Class to manage the flipper """

	def __init__(self, game):
		""" Initialize the flipper and set it to its starting position """
		# Assign the screen from pinball.py to Flipper in order to access it
		self.screen = game.screen
		# Gets the screen's rect to match the flipper's rect
		self.screen_rect = self.screen.get_rect()

		# Flipper's size and positioning
		self.flipper_size = (self.flipper_width, self.flipper_height) = (100, 20)
		self.flipper = pygame.Surface(self.flipper_size)
		self.rect = self.flipper.get_rect()
		# Matches the center of the flipper's rect to the center of screen's rect
		self.rect.center = self.screen_rect.center

		# Creates a Settings instance
		self.settings = Settings()

		# Positions the flipper at 0.8 * screen height down below
		self.rect.y = 650

		# Movement flag - when the right arrow key is pressed, we set the flag to True
		self.moving_right = False
		# Movement flag - when the left arrow key is pressed, we set the flag to True
		self.moving_left = False


	def update(self):
		""" Updates the flipper's position """
		if self.moving_right:
			self.rect.x += self.settings.flipper_speed
		if self.moving_left:
			self.rect.x -= self.settings.flipper_speed


	def blitme(self):
		self.screen.blit(self.flipper, self.rect)