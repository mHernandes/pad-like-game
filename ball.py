import pygame


class Ball:
	""" Class that manages the ball """
	def __init__(self, game):
		""" initializes the ball """
		# Assign the screen from pinball.py to Flipper in order to access it
		self.screen = game.screen
		# Get the screen
		self.screen_rect = self.screen.get_rect()

		# Ball height and width
		self.size = (self.width, self.height) = (10, 10)
		# Creates the surface
		self.ball = pygame.Surface((self.size))
		# Get the ball's rect
		self.rect = self.ball.get_rect()
		# Set the ball's center to the screen's center. We will initialize the ball on a random spot later
		self.rect.center = self.screen_rect.center
		# Add color
		ball_color = (255,0,255)
		self.ball.fill(ball_color)

	def blitme(self):
		self.screen.blit(self.ball, self.rect)