"""
Pendências: criar uma tela de fim; fazer com que, mesmo se o arquivo txt estiver vazio, o jogo não pare; depois que as três vidas acabam, é possível 
movimentar o pad; refactor the code

"""


"""
What to do next: 
2 - Criar uma tela de End Game. Depois das três vidas, printar Game Over na tela e um "deseja jogar de novo?" Teremos que criar uma função
que reinicia os parâmetros. Remover a vida restante da  tela
Ou só end game. if number of lives = 0, game_active = False print("game over")
3 - Refactor the code
"""


import sys, pygame
from flipper import Flipper
from settings import Settings
from ball import Ball
from button import Button
from scoreboard import Scoreboard
from time import sleep


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
		# Creates a Button instance
		self.play_button = Button(self)
		# Creates a Scoreboard instance
		self.scoreboard = Scoreboard(self)


	def check_events(self):
		""" Checks for key presses """
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)
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
		""" Check for ball and flipper collisions. Each time there's a collision, change ball movement and increase the current score """
		if self.ball.rect.colliderect(self.flipper.rect):
			self.scoreboard.current_score += 1
			# calls display_current_score() to update the current score to the screen 
			self.scoreboard.display_current_score()
			# Inverts the ball direction
			self.ball.change_y *= -1
			# Check for high score
			self.scoreboard.check_highest_score()
			# Calls display_highest_score() to update the high score to the screen
			self.scoreboard.display_highest_score()


	def _check_play_button(self, mouse_pos):
		""" Start a new game when the player presses Play """
		if self.play_button.rect.collidepoint(mouse_pos):
			self.settings.game_active = True


	def update_screen(self):
		""" Updates screen """
		# Fill screen with color
		self.screen.fill(self.settings.screen_color)
		# Blits the flipper on screen
		self.flipper.blitme()
		# Blits the ball on the screen
		self.ball.blitme()
		# Blits the scoreboard on the screen only if settings.game_active is True
		if self.settings.game_active:
			self.scoreboard.blitme()
			self.scoreboard.display_lives_left(self.ball.lives)
		# Blits the button on the screen if the game status is inactive (game_active is False)
		if not self.settings.game_active:
			self.play_button.blitme()
		# Update the full display Surface to the screen
		pygame.display.flip()


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