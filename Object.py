import random


class Object:

		"""Generates a random list of positions for objects to be collected."""

		def __init__(self):   
			self.objectsPositions = []		#empty list of objects' positions


		# Random generation of objects positions amid available positions ("-") 
		# in maze structure
		def objectsPosition(self, maze):

			# Do that until len(objectsPositions is == 3)
			while len(self.objectsPositions) != 3:

				# Picks two random numbers between 0 and 14 included
				i = random.randint(0, 14)
				j = random.randint(0, 14)
				position = (i, j)


				# Check with Maze if the position corresponds to an empty space (i.e. "-")	
				# if yes, append position to list objectsPositions
				if maze.availablePosition(position) is True and position not in self.objectsPositions:
					self.objectsPositions.append(position)

			# Return objectsPositions
			return self.objectsPositions