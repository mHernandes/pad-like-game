import pygame
from settings import Settings


class Scoreboard:
	""" Class to manage the score """

	def __init__(self, game):
		""" Initializes the scoreboard """
		# Assign the screen from pinball.py to Scoreboard in order to blit onto the screen
		self.screen = game.screen
		self.screen_rect = self.screen.get_rect()

		# Initializes the current game's score
		self.current_score = 0

		# Settings instance
		self.settings = Settings()

		# Reads the highest score file as scoreboard's initialized
		self._read_highest_score_file()

		# Score and display
		self.display_current_score()
		self.display_highest_score()


	def check_highest_score(self):
		""" In each collision, check if the current score is bigger than the highest score """
		self._read_highest_score_file()
		if self.current_score > self.highest_score:
			self.highest_score = self.current_score
			self._write_to_file()


	def _read_highest_score_file(self):
		""" Read higest score file """
		for n in open("highest_score.txt"):
			self.highest_score = int(n)


	def _write_to_file(self):
		""" Write to highest score file """
		f = open("highest_score.txt", "w")
		f.write(str(self.highest_score))
		f.close()


	def display_current_score(self):
		""" Display the current score on screen """
		# Score font
		self.font = pygame.font.SysFont(None, 48)
		# Renders the score
		self.current_score_image = self.font.render("Current score: " + str(self.current_score), True, self.settings.score_font_color)
		# Get the current score image's rect
		self.current_score_rect = self.current_score_image.get_rect()
		# Set the current score on top of the screen
		self.current_score_rect.midtop = self.screen_rect.midtop


	def display_highest_score(self):
		""" Display the highest score on screen """
		# Renders the score - we'll use the same font as in display_current_score()
		self.highest_score_image = self.font.render("Highest score: " + str(self.highest_score), True, self.settings.score_font_color)
		# Get the highest_score_image rect
		self.highest_score_rect = self.highest_score_image.get_rect()
		# Set the current score on top right of the screen
		self.highest_score_rect.topright = self.screen_rect.topright


	def blitme(self):
		""" Blit the score onto the screen """
		self.screen.blit(self.current_score_image, self.current_score_rect)
		self.screen.blit(self.highest_score_image, self.highest_score_rect)