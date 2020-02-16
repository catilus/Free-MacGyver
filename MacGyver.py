from pygame.locals import *


class MacGyver:

    """Attributes and methods associated with the movement of MacGyver,
    and collect of objects in the maze."""

    def __init__(self, position, dict_of_objects):
        self.position = position  #(tuple)
        self.bag = 0
        self.dict_of_objects = dict_of_objects

    def collects(self, position, dict_of_objects, bag):

        # If Macgyver's position corresponds to that of an object
        if self.position in dict_of_objects:
            # MacGyver collects objects
            self.bag += 1
            # Collected objects disappear from the dictionaire of objects 
            del(self.dict_of_objects[self.position])
            return self.dict_of_objects, self.bag
        else:
            pass 

    def beatsGuardian(self, position, bag):
        if self.bag == 3:
            return True
        else:
            return False

    def moves(self, event, position, maze):    
        
        # Calculates new position
        if event.key == K_DOWN: 
            self.position = (position[0], position[1]+1)

        elif event.key == K_UP:
            self.position = (position[0], position[1]-1)         

        elif event.key == K_LEFT: 
            self.position = (position[0]-1, position[1])

        elif event.key == K_RIGHT:
            self.position = (position[0]+1, position[1])

        # Checks that new position is not outside of the screen or on a wall
        if 0 <= self.position[0] <=14 and 0 <= self.position[1] <=14:
            
            # check with maze if there is a wall at this position or not
            if maze.wallPosition(self.position) == False:
                # if it's an object: collect it
                self.collects(self.position, self.dict_of_objects, self.bag)          
            else:
                self.position = position    # Keeps original position
        else:
            self.position = position    

   


                    






        	