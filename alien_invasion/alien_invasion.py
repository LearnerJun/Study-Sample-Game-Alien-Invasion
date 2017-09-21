import sys

import pygame

from settings import Settings
from ship import Ship

def run_game():
	#initialize game and create a screen
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
	(ai_settings.screen_width, ai_settings.screen_height)) #size of screen
												  #screen is a surface,
	pygame.display.set_caption("Alien Invasion")  #refresh surface while game start looping

	#create a ship
	ship = Ship(screen)

	#set the background color
	bg_color = (230, 230, 230)

	#loop for starting game
	while True:

		#monitor events - keyboard and mouse
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		#update background color when events monitored
		screen.fill(bg_color)
		ship.blitme()
		#display recent screen which is kept updating
		pygame.display.flip()

run_game() #start the game
