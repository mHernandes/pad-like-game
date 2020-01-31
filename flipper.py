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

		# Settings instance
		self.settings = Settings()

		# Flipper's size, color and rect
		self.flipper = pygame.Surface((self.settings.flipper_size))
		self.flipper.fill(self.settings.flipper_color)
		self.rect = self.flipper.get_rect()
		# Matches the center of the flipper's rect to the center of screen's rect
		self.rect.center = self.screen_rect.center

		# Positions the flipper at flipper_pos
		self.rect.y = self.settings.flipper_pos

		# Movement flag - when the right arrow key is pressed, we set the flag to True
		self.moving_right = False
		# Movement flag - when the left arrow key is pressed, we set the flag to True
		self.moving_left = False


	def update(self):
		""" Updates the flipper's position """
		if self.moving_right and (self.rect.right < self.screen_rect.right):
			self.rect.x += self.settings.flipper_speed
		if self.moving_left and (self.rect.left > 0):
			self.rect.x -= self.settings.flipper_speed


	def blitme(self):
		""" Blits the flipper on the screen """
		self.screen.blit(self.flipper, self.rect)