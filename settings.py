class Settings:
	""" Class to store all settings for the pinball game """
	def __init__(self):
		""" Initializes the settings """
		# Screen settings
		self.screen_size = (self.screen_width, self.screen_height) = (1200, 700)
		self.screen_color = (255, 255, 255)
		self.screen_caption = "Pinball"

		# Ball settings
		self.ball_size = (self.ball_width, self.ball_height) = (10, 10)
		self.ball_color = (255,0,255)
		self.ball_speed = 1.5

		# Flipper settings
		self.flipper_size = (self.flipper_width, self.flipper_height) = (100, 20)
		self.flipper_pos = 650
		self.flipper_speed = 2.5

		# Button settings
		self.button_x, self.button_y = ()
		self.button_size = self.button_width, self.button_height = ()
		self.button_color = ()
		self.button_font = ('freesansbold.ttf',48)

		# Game settings
		self.game_active = True
		self.lives_left = 3