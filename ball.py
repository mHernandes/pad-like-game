import pygame
from pygame.sprite import Sprite
from settings import Settings
from random import randint


class Ball(Sprite):
	""" Class that manages the ball """
	def __init__(self, game):
		""" initializes the ball """
		# Call the parent class (Sprite) constructor
		super().__init__()
		# Creates a Settings instance
		self.settings = Settings()
		# Assign the screen from pinball.py to Ball in order to blit the ball on it. See blitme()
		self.screen = game.screen

		# Creates the surface - ball size defined in settings.py
		self.ball = pygame.Surface((self.settings.ball_size))
		# Get the ball's rect
		self.rect = self.ball.get_rect()
		# Set the ball's center to a random position on the screen. x goes from 0 to the screen width, y goes from 0 to 1/3 screen height
		self.x, self.y = (randint(0, self.settings.screen_width), randint(0, self.settings.screen_width / 3))
		self.rect.center = (self.x, self.y)
		# Add color to the ball - ball color defined in settings.py
		self.ball.fill(self.settings.ball_color)

		# Ball moving speed
		self.speed = 0.5


	def _check_edges(self):
		pass


	def update(self):
		""" Updates the ball position """
		self.x += self.speed
		self.y += self.speed
		self.rect.center = (self.x, self.y)


	def blitme(self):
		""" Blits the ball on screen """
		self.screen.blit(self.ball, self.rect)