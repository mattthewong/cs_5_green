from visual import *
import math

class robot:
    def __init__(self, position=vector(0,0,0), heading=vector(0,0,1)):
        self.base = vector(position)
        self.heading = vector(norm(heading))
        self.parts = []

    def forward(self, amount):
        self.base += self.heading * amount
        for part in self.parts:
            part.pos += self.heading * amount

    def turn(self, angle):
        theta = math.radians(angle)
        self.heading = rotate(self.heading, angle=theta, axis=(0, 1, 0))
        for part in self.parts:
            part.rotate(angle=theta, axis=(0,1,0), origin=self.base)


class ranbot(robot):
    def __init__(self, position=vector(0,0,0), heading=vector(0,0,1), speed=1.0):
        robot.__init__(self, position, heading)
        self.body = cylinder(pos = self.base+vector(0, 0.5, 0), axis=(0, 6, 0), radius=1, color=color.red)
        self.head = box(pos= vector(0,7,0)+self.base, length = 2, width = 2, height = 2, color=color.green)
        self.nose = cone(pos = vector(0,7,1)+self.base, radius = 0.5, axis=(0,0,1), color=color.yellow)
        self.wheel1 = cylinder(pos = self.base + vector(1, 1, 0), axis=(0.5, 0, 0), radius = 1, color=color.blue)
        self.wheel2 = cylinder(pos = self.base + vector(-1, 1, 0), axis=(-0.5, 0, 0), radius = 1, color=color.blue)
        self.parts = [self.body, self.head, self.nose, self.wheel1, self.wheel2]
        self.speed = speed



class myrobot(robot):
    def __init__(self, position=vector(-10,0,10), heading=vector(0,0,1), speed=0.5):
        robot.__init__(self, position, heading)
        self.body = cylinder(pos = self.base+vector(0, 0.5, 0), axis=(0, 6, 0), radius=1, color=color.yellow)
        self.head = box(pos= vector(0,7,0)+self.base, length = 2, width = 2, height = 2, color=color.black)
        self.nose = cone(pos = vector(0,7,1)+self.base, radius = 0.5, axis=(0,0,1), color=color.green)
        self.wheel1 = cylinder(pos = self.base + vector(1, 1, 0), axis=(0.5, 0, 0), radius = 1, color=color.black)
        self.wheel2 = cylinder(pos = self.base + vector(-1, 1, 0), axis=(-0.5, 0, 0), radius = 1, color=color.black)
        self.parts = [self.body, self.head, self.nose, self.wheel1, self.wheel2]
        self.speed = speed






  

        
        
            
        




        
        
