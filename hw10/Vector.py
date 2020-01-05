import math

class Vector:
    def __init__(self, x, y):
        '''This is the "constructor" for the class. The user specifies floating point
        values x and y and these are the values for the vector.
        Note that there are two underscores before and two underscores after the word "init".
        This is the format for every "overloaded" method (as is "add" and "sub" below).'''
        self.x = x  # Notice that x is the name of the input, but self.x is our own self's copy of that!
        self.y = y  # ... and same for y

    def __repr__(self): 
        '''Returns a string representing the vector. Recall that this method will
        automatically be invoked when you ask to print the vector. You can choose
        how the string representation should look, but one common representation
        is something like this: (3, 42) where 3 is the x-coordinate and 42 is the y-coordinate.'''
        return "(" + str(self.x) + "," + str(self.y) + ")"
    def magnitude(self): 
        '''Returns the floating point magnitude of the vector. 
        (Recall that if you import math in your file, you can use math.sqrt(blah)
        to compute the square root of blah). The math package has all kinds of other
        snazzy functions, including trigonometric ones and others. You can Google
        "python math" to learn more about it.'''
        magnitude1 = (self.x * self.x) + (self.y * self.y)
        return math.sqrt(magnitude1)
        
    
    def normalize(self): 
        '''Changes the x- and y-coordinates of the vector so that the vector
        has magnitude 1 but the same direction as before.'''
        magnitude1 = self.magnitude()
        self.x = self.x/magnitude1
        self.y = self.y/magnitude1
        
        

    def __add__(self, other): 
        '''Returns a new vector that is the sum of the current vector and the given
        other vector. Recall that when the function is named in this funny way,
        using the "+" sign will automatically invoke this function (see examples below).'''
        xsummation = self.x + other.x
        ysummation = self.y + other.y
        return "(" + str(xsummation) + "," + str(ysummation) + ")"
    
    def __sub__(self, other): 
        '''Returns a new vector that is the difference self - other. Recall that when
        the function is named in this funny way, using the "-" sign will automatically
        invoke this function (see examples below). '''
        xdifference = self.x - other.x
        ydifference = self.y - other.y
        return "(" + str(xdifference) + "," + str(ydifference) + ")"
        
        