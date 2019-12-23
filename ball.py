import pygame
from pygame.sprite import Sprite
from settings import Settings
from random import randint
from time import sleep


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
		# Get the screen rect to check for screen edges
		self.screen_rect = self.screen.get_rect()

		# Creates the surface - ball size defined in settings.py
		self.ball = pygame.Surface((self.settings.ball_size))
		# Get the ball's rect
		self.rect = self.ball.get_rect()
		# Starts the ball
		self._start_ball()
		# Add color to the ball - ball color defined in settings.py
		self.ball.fill(self.settings.ball_color)

		# Ball moving speed
		self.speed = 1.5

		# Variables to change the ball direction
		self.change_x = 1
		self.change_y = 1


	def _start_ball(self):
		""" Set the ball to its starting position """
		# Set the ball's center to a random position on the screen. x goes from 0 to the screen width, y goes from 0 to 1/3 screen height
		self.x, self.y = (randint(0, self.settings.screen_width), randint(0, self.settings.screen_width / 3))
		self.rect.center = (self.x, self.y)


	def _check_screen_edges(self):
		""" Checks for screen edges (right, left, top) in order to invert the ball movement """
		if self.x > self.screen_rect.right or self.x < self.screen_rect.left:
			self.change_x *= -1
		elif self.y < self.screen_rect.top:
			self.change_y *= -1


	def _bottom_hit(self):
		""" Respond to the ball reaching the bottom  """
		if self.rect.bottom >= self.screen_rect.bottom:
			self._start_ball()
			# Decreases number of lives left
			self.settings.lives_left -= 1
			# Debuging
			print(self.settings.lives_left)
			# Add delay after the ball reaches the bottom of the screen
			sleep(0.5)


	def update(self):
		""" Updates the ball position """
		self._check_screen_edges()
		self._bottom_hit()
		# Moves the ball
		self.x += self.speed * self.change_x
		self.y += self.speed * self.change_y
		self.rect.center = (self.x, self.y)


	def blitme(self):
		""" Blits the ball on screen """
		self.screen.blit(self.ball, self.rect)