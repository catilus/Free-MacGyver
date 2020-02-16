class Maze:

	"""Gives the positions of walls, empty spaces and guardian."""

	def __init__(self, filename):
		self.filename = filename

	def wallPosition(self, position):

		i = position[0]
		j = position[1]
		
		# If position is that of a wall, return False 
		if self.filename[i][j] == 'w':
			return True

		# Else, return True
		else:
			return False

	def availablePosition(self, position):		

		i = position[0]
		j = position[1]
		
		# If position is empty, return True
		if self.filename[i][j] == '-':
			return True

		# Else, return False
		else:
			return False		
	
	def guardianPosition(self, position):

		i = position[0]
		j = position[1]				

		# If position is that of the guardian, return True
		if self.filename[i][j] == 'f':
			return True

		# Else, return False
		else:
			return False		