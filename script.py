""" Free MacGyver - To escape the maze, our hero MacGyver needs 
to beat the Guardian of the exit.To do so, he will have to collect 
three objects on its way out. """

## Import modules
import json
import pygame
import pygame.locals
from Maze import *
from Screen import *
from MacGyver import *
from Object import *


pygame.init()


## Load maze initial structure file
levelfile = json.load(open("level.json"))
(width, height) = (300, 300)


## Instanciate objects
maze = Maze(levelfile)
objects = Object()  
screen = Screen(width, height)


## Display the first structure of the maze
# Objects to be collected.
list_of_objects = objects.objectsPosition(maze)
dict_of_objects = {list_of_objects[0]: "P1", list_of_objects[1]: "P2", 
				   list_of_objects[2]: "P3"}
screen.displays(dict_of_objects, 'o')


# Maze: walls, start and finish
for i in range(0, len(levelfile)):
    for j in range(0, len(levelfile)):

        item_position = [i, j]

		# display walls
        if levelfile[i][j] == 'w':
            screen.displays(item_position, 'w')

		# display MacGyver
        elif levelfile[i][j] == 's':
            macGyver = MacGyver((i, j), dict_of_objects)
            screen.displays(macGyver.position, 's')

		# display Guardian
        elif levelfile[i][j] == 'f':
            screen.displays(item_position, 'f')


## Events loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

        if event.type == KEYDOWN:

        	# display black tile on MacGyver's current position
        	# if he cannot move, he'll be re-printed on top of the background tile
            screen.displays(macGyver.position, 'b')

            macGyver.moves(event, macGyver.position, maze)

            # display MacGyver
            screen.displays(macGyver.position, 's')

            # display Victory or Game over screens
            if maze.guardianPosition(macGyver.position) is True:
                if macGyver.beatsGuardian(macGyver.position, macGyver.bag) == False:
                    screen.displays((0, 0), 'Game Over')
                    print("Game over")
                else:
                    screen.displays((0, 0), 'Victory')
