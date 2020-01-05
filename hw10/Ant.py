from Vector import *
import random
import turtle
class Ant:
    def __init__(self, position): 
        '''This is the "constructor" for the class. The user specifies a position of the ant
        which is a Vector. The ant keeps that vector as its position. In addition, the
        ant chooses a random color for its footstep. A color is a tuple with three numbers
        between 0 and 1, representing the amount of red, green, and blue in the color mixture.
        For example, the tuple (0.5, 0.8, 0.1) is a combination of some red, quite a bit of green,
        and just a touch of blue. You can get a random number between 0 and 1 using the random
        package using random.uniform(0, 1).'''
        self.position = position
        self.color = (random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))
        
        
    def __repr__(self): 
        '''This function returns a string which represents the ant. This string can
        simply display the ant's x- and y- coordinates.'''
        return str(self.position)
    
    def moveTowards(self, otherAnt):
        '''This function takes as input a reference to another ant. Then, our ant "moves" towards
        the other ant by a step of length 1. That is, we first compute a vector from
        ourself (self) to the other ant, normalize it to have length 1, and then update
        our ant's position by adding this vector to its current position. This method
        doesn't display anything, it simply updates the ant's own position vector!'''
        distancetomove = otherAnt.position - self.position
        distancetomove.normalize()
        self.position = self.position + distancetomove
        
    def footstep(self): 
        '''This function draws a dot in the ant's chosen color (remember, we established
        that color in the constructor when the ant was first "manufactured") at the
        ant's current location. To do this, you'll need to pickup the turtle
        (using turtle.penup()), move the turtle to the ant's current location
        (using turtle.setpos(x, y) where x and y are the desired x- and y- coordinates
        - which you'll need to extract from the vector that stores the ant's position),
        put the pen down so that the turtle can draw (using turtle.pendown()), set the
        turtle's drawing color (using turtle.color(c) where c represents the 3-tuple 
        that contain's this ant's chosen drawing color), and draw a dot for the footstep
        (using turtle.dot()).'''
        
        turtle.penup()
        turtle.setpos(self.position.x,self.position.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.dot()