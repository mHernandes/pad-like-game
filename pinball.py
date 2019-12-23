"""
What to do next:
"""


import sys, pygame
from flipper import Flipper
from settings import Settings
from ball import Ball


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
		# Creates a Ball instance. (we pass 'self' so we can create the screen in Flipper __init__())
		self.ball = Ball(self)


	def check_events(self):
		""" Checks for key presses """
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					self.flipper.moving_right = True
				elif event.key == pygame.K_LEFT:
					self.flipper.moving_left = True
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					self.flipper.moving_right = False
				elif event.key == pygame.K_LEFT:
					self.flipper.moving_left = False


	def check_collision(self):
		""" Check for ball and flipper collisions """
		if self.ball.rect.colliderect(self.flipper.rect):
			self.ball.change_y *= -1


	def update_screen(self):
		""" Updates screen """
		# Fill screen with color
		self.screen.fill(self.settings.screen_color)
		# Blits the flipper on screen
		self.flipper.blitme()
		# Blits the ball on the screen
		self.ball.blitme()
		# Update the full display Surface to the screen
		pygame.display.flip()


	def game_over(self):
		""" Runs the game while number of lives >= 0 """
		if self.ball.settings.lives_left > 0:
			return True


	def run_game(self):
		""" Main loop of the game """
		while True:
			self.check_events()
			if self.settings.game_active:
				self.flipper.update()
				self.ball.update()
				self.check_collision()
			self.update_screen()


def main():
	pinball = Game()
	pinball.run_game()


if __name__ == "__main__": main()