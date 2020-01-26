import pygame
from settings import Settings


class Button:
	""" A Class to manage the button """

	def __init__(self, game):
		""" Initializes the Class """
		# Settings instances
		self.settings = Settings()

		# Assign the screen from pinball.py to Button in order to access it and get rect
		self.screen = game.screen
		self.screen_rect = self.screen.get_rect()

		# Button rect
		self.font = pygame.font.SysFont(None, 48)
		self.rect = pygame.Rect(0, 0, self.settings.button_width, self.settings.button_height)
		self.rect.center = self.screen_rect.center

		# Text and prepping
		text = "Play"
		self._prepare_text(text)


	def _prepare_text(self, text):
		""" Renders text as an image and centers it on the button """
		self.text_image = self.font.render(text, True, self.settings.text_color, self.settings.button_color)
		self.text_image_rect = self.text_image.get_rect()
		self.text_image_rect.center = self.rect.center


	def blitme(self):
		""" Draw button and blits it """
		self.screen.fill(self.settings.button_color, self.rect)
		self.screen.blit(self.text_image, self.text_image_rect)