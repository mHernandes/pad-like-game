import pygame


class Flipper:
	""" A Class to manage the flipper """

	def __init__(self, game):
		""" Initialize the flipper and set it to its starting position """
		# Assign the screen from pinball.py to Flipper in order to access it
		self.screen = game.screen
		# Gets the screen's rect to match the flipper's rect
		self.screen_rect = self.screen.get_rect()

		# Flipper's size
		self.flipper_size = (self.flipper_width, self.flipper_height) = (100, 20)
		self.flipper = pygame.Surface(self.flipper_size)
		self.rect = self.flipper.get_rect()
		# Matches the flipper's rect to the screen's rect
		self.rect.midbottom = self.screen_rect.midbottom


	def blitme(self):
		self.screen.blit(self.flipper, self.rect)