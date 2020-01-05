from Vector import *
from Ant import *
import turtle
import random

    
def AntBox():
    '''This function initializes four ants, one at each corner of a square
    with side length 100. Then, these ants are placed in a list. Finally, we
    enter an infinite loop that, at each iteration, has each ant move one step
    towards its "friend". Each ant likes the ant clockwise to it. '''
    Ant1 = Ant(Vector(0,0))
    Ant2 = Ant(Vector(100,0))
    Ant3 = Ant(Vector(100,100))
    Ant4 = Ant(Vector(0,100))
    
    AntList = [Ant1,Ant2,Ant3,Ant4]
    
    while True:
        for x in range(len(AntList)):
            if x < (len(AntList)-1):
                AntList[x].moveTowards(AntList[x+1])
                AntList[x].footstep()
            else:
                AntList[x].moveTowards(AntList[0])
                L[x].footstep()
def FickleAnts(n,side):
    '''This function takes as input a positive integer n indicating the number of
    ants to be used and a positive integer side indicating the side length
    (height and width) of the antbox. '''
    L = []
    while len(L) < n:
        L.append(Ant(Vector(random.randrange(0,side),random.randrange(0,side))))
    while Stop is True:
        for x in range(len(L)):
            otherAnt = random.choice(L)
            if L[x].position != otherAnt.position:
                L[x].moveTowards(otherAnt)
                L[x].footstep()
    return L[0].position
    
def Stop(L):
    '''function returns True is distance between two ant vectors < 
    stop distance and returns False otherwise'''
    for x in range(len(L)):
        for y in range(len(L)):
            if L[x].position != L[y].position:
                dist = L[x].position - L[y].position
                mag = dist.magnitude()
                if abs(mag) > StopDistance:
                    return True
    return False
    
                
    