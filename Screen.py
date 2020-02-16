import pygame
from pygame.locals import *


class Screen:

	"""In charge with the display of objects"""

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.window = pygame.display.set_mode((width, height))

	def displays(self, position, item):		
		# Needs item [fed from script] & position = Position() 
		# [called in Maze.py] to know which item display and where
		tile_size = 20

		if item == 'w':
			tile = pygame.image.load("ressource/blue-floor.png") # Loads tile image
			self.window.blit(tile, (position[0]*tile_size, position[1]*tile_size))
			pygame.display.update()
			pygame.display.flip()

		elif item == 's': 
			tile = pygame.image.load("ressource/MacGyver_rs.png") 
			self.window.blit(tile, (position[0]*tile_size, position[1]*tile_size))
			pygame.display.update()
			pygame.display.flip()		

		elif item == 'f': 
			tile = pygame.image.load("ressource/Guardian_rs.png") 
			self.window.blit(tile, (position[0]*tile_size, position[1]*tile_size))
			pygame.display.update()
			pygame.display.flip()

		elif item == 'b': 
			tile = pygame.image.load("ressource/background_tile.jpg") 
			self.window.blit(tile, (position[0]*tile_size, position[1]*tile_size))
			pygame.display.update()
			pygame.display.flip()

		elif item == 'o':

			for character in position:
				if position[character] == "P1":
					object1 = pygame.image.load("ressource/Personnage1.png") # Loads object 1
					self.window.blit(object1, (character[0]*tile_size, character[1]*tile_size))
					pygame.display.update()
					pygame.display.flip()

				elif position[character] == "P2":
					object2 = pygame.image.load("ressource/Personnage2.png") # Loads object 1
					self.window.blit(object2, (character[0]*tile_size, character[1]*tile_size))
					pygame.display.update()
					pygame.display.flip()

				else:
					object3 = pygame.image.load("ressource/Personnage3.png") # Loads object 1
					self.window.blit(object3, (character[0]*tile_size, character[1]*tile_size))
					pygame.display.update()
					pygame.display.flip()	

		elif item == 'Game Over':
			game_over = pygame.image.load("ressource/defeat_screen.png") 
			self.window.blit(game_over, position)
			pygame.display.update()
			pygame.display.flip()


		elif item == 'Victory':	
			victory = pygame.image.load("ressource/victory_screen.png") 
			self.window.blit(victory, position)
			pygame.display.update()
			pygame.display.flip()
