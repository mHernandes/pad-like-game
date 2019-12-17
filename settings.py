class Settings:
	""" Class to store all settings for the pinball game """
	def __init__(self):
		""" Initializes the settings """
		self.screen_size = (self.screen_width, self.screen_height) = (1200, 700)
		self.screen_color = (255, 255, 255)
		self.screen_caption = "Pinball"