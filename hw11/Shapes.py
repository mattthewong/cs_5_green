# Shapes
# January 26, 2010
# RLH

import math
import turtle
scalefact = 0.866
from Matrix import *
from Vector import *

class Shape:
    def __init__(self):
        self.points = []
        
    def render(self):
        """Use turtle graphics to render shape"""
        turtle.penup()
        turtle.setposition(self.points[0].x, self.points[0].y)
        turtle.pendown()
        turtle.fillcolor(self.color)
        turtle.pencolor(self.color)
        turtle.begin_fill()
        for vector in self.points[1:]:
            turtle.setposition(vector.x, vector.y)
        turtle.setposition(self.points[0].x, self.points[0].y)
        turtle.end_fill()

    def erase(self):
        """Draw shape in white to effectively erase it from screen"""
        temp = self.color
        self.color = "white"
        self.render()
        self.color = temp
    
    def rotate(self, theta, rotateAbout):
        """Rotate shape by theta degrees """
        theta = math.degrees(theta)  # THIS IS CORRECT!
        # Python's trig functions expect input in radians
        # so this function converts from degrees into radians.
        RotationMatrix = Matrix(math.cos(theta), -1*math.sin(theta), math.sin(theta), math.cos(theta))
        NewPoints = []
        for vector in self.points:
            vector1 = Vector(vector.x +rotateAbout.x, vector.y + rotateAbout.y)
            newvector = RotationMatrix * vector1
            vector2 =Vector(newvector.x - rotateAbout.x, newvector.y - rotateAbout.y)
            NewPoints.append(vector2)
        self.points = NewPoints
        
    def translate(self,transVector):
        '''that takes a Vector as input and translates any of your current shapes
        by this Vector.'''
        self.transVector = transVector
        NewPoints = []
        for vector in self.points:
            newvector = Vector(self.transVector.x + vector.x, self.transVector.y + vector.y)
            NewPoints.append(newvector)
            self.points = NewPoints
    def scale(self,s):
        '''takes a single floating point number s as input and scales any of your current
        shapes by a factor of s about its center. That is, the center of the new scaled
        shape should be the same as the center of the original shape.'''
        self.s = s
        ScaledMatrix = Matrix(self.s,0,0,self.s)
        Newlocation = []
        for vectors in self.points:
            vector1 = Vector(vectors.x - self.center.x, vectors.y - self.center.y)
            Newvector = ScaledMatrix.__mul__(vector1)
            Vector2 = ScaledMatrix * Newvector
            Vector3 = Vector(Vector2.x + self.center.x, Vector2.y + self.center.y)
        Newlocation.append(Vector3)
        
class Rectangle(Shape):
    def __init__(self, width, height, center = Vector(0, 0), color = "black"):
        SW = Vector(center.x - width/2.0, center.y - height/2.0)
        NW = Vector(center.x - width/2.0, center.y + height/2.0)
        NE = Vector(center.x + width/2.0, center.y + height/2.0)
        SE = Vector(center.x + width/2.0, center.y - height/2.0)
        self.points = [SW, NW, NE, SE]
        self.color = color

class Square(Rectangle):
    def __init__(self, width, center=Vector(0, 0), color = "black"):
        Rectangle.__init__(self, width, width, center, color)
        
class Circle(Shape):
    def __init__(self, center = Vector(0, 0), radius = 10, color = "black"):
        self.center = center
        self.radius = radius
        self.color = color
    def rotate(self, theta):
        """ theta is in degrees."""
        theta = math.radians(theta)
        RotationMatrix = Matrix(math.cos(theta), -1*math.sin(theta), math.sin(theta), math.cos(theta))        
        self.center = RotationMatrix * self.center
        

    def render(self):
        turtle.penup()
        turtle.right(90)
        turtle.forward(self.radius)
        turtle.setposition(self.center.x, self.center.y)
        turtle.pendown()
        turtle.fillcolor(self.color)
        turtle.pencolor(self.color)
        turtle.begin_fill()
        turtle.circle(self.radius)
        turtle.end_fill()
        turtle.left(90)
        
class triangle(Shape):
    '''draws am equilateral triangle with starting at center 0 with a given width,
    sidelength, and color)'''
    def __init__(self, center=Vector(0, 0), sidelength = 10, color = "black"):
        self.sidelength = sidelength
        self.center = center
        self.color = color
        Vector1 = Vector(center.x, center.y +(0.5*scalefact*self.sidelength))
        Vector2 = Vector(center.x -(0.5*self.sidelength*scalefact), center.y - (0.5*self.sidelength*scalefact))
        Vector3 = Vector(center.x +(0.5*self.sidelength*scalefact), center.y - (0.5*self.sidelength*scalefact))
        self.points = [Vector1,Vector2,Vector3]
     
    
        
        




        
        
