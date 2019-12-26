import pygame


class Scoreboard:
	""" Class to manage the score """

	def __init__(self, game):
		""" Initializes the scoreboard """
		# Assign the screen from pinball.py to Scoreboard in order to blit onto the screen
		self.screen = game.screen
		self.screen_rect = self.screen.get_rect()

		# Initializes the score
		self.score = 0

		# Score and display
		self.display_current_score()


	def display_current_score(self):
		""" Display the current score on the screen """
		# Score font
		font = pygame.font.SysFont(None, 48)
		# Current score font color
		self.current_score_font_color = (255,255,255)
		# Renders the score
		self.current_score_image = font.render(str(self.score), True, self.current_score_font_color)
		# Get the current score image's rect
		self.current_score_rect = self.current_score_image.get_rect()
		# Set the current score on top of the screen
		self.current_score_rect.midtop = self.screen_rect.midtop


	def blitme(self):
		""" Blit the score onto the screen """
		self.screen.blit(self.current_score_image, self.self.current_score_rect)