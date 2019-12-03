import sys, pygame


def init():
	pygame.init()
	# Initialize screen
	size = width, height = (1200, 700)
	screen_color = (255, 255, 255)
	screen = pygame.display.set_mode((size))
	screen.fill(screen_color)
	pygame.display.set_caption('Pinball')

	# flipper
	flipper = pygame.image.load("imagem/flipper.bmp")
	base = pygame.Surface((170, 50))
	screen.blit(base, (0, 0))

	

def run_game():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		pygame.display.flip()


def main():
	init()
	run_game()



if __name__ == "__main__": main()

