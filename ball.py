import pygame
from pygame.sprite import Sprite
from settings import Settings


class Ball(Sprite):
	""" Class that manages the ball """
	def __init__(self, game):
		""" initializes the ball """
		# Call the parent class (Sprite) constructor
		super().__init__()
		# Creates a Settings instance
		self.settings = Settings()
		# Assign the screen from pinball.py to Flipper in order to access it
		self.screen = game.screen
		# Get the screen
		self.screen_rect = self.screen.get_rect()

		# Creates the surface - ball size defined in settings.py
		self.ball = pygame.Surface((self.settings.ball_size))
		# Get the ball's rect
		self.rect = self.ball.get_rect()
		# Set the ball's center to the screen's center. We will initialize the ball on a random spot later
		self.rect.center = self.screen_rect.center
		# Add color to the ball - ball color defined in settings.py
		self.ball.fill(self.settings.ball_color)

		"""# Ball's velocity vector
		self.position = (self.change.x, self.change.y) = (100, 100)"""


	def update(self):
		pass


	def blitme(self):
		""" Blits the ball on screen """
		self.screen.blit(self.ball, self.rect)