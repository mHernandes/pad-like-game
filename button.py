import pygame
from settings import Settings


class Button:
	""" A Class to manage the button """

	def __init__(self, game):
		""" Initializes the Class """
		# Settings instance
		self.settings = Settings()

		#
		self.screen = game

		self.button = pygame.Surface() 
		self.button_font = pygame.font.Font(self.settings.button_font)

