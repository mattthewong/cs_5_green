#Matt Wong

import turtle
from getStruct import *
from hivSeqs import *

#The four structures similarly illustratae multiple folds, signifying that their
#diversive biological functionality for their respective organisms.
def render(RNA, matches):
    """Draws the RNA sequence graphically, showing every nucleotide in the RNA
    string and showing the matches in the positions given in the list matches.
    """
    if len(RNA)<5:
        return 
    else:
        count=0
        for i in RNA:
            turtle.pendown()
            turtle.dot(5, "blue")
            turtle.write(i, font = ("arial", 8, "normal"))
            count+=1
            if count!=len(RNA):
                turtle.pencolor("black")
                turtle.forward(20)
                turtle.penup()
                   
            else: 
                turtle.penup()
        count+=1
        turtle.backward(20*(len(RNA)-1))       
        
        x=300
        for each in matches:
            turtle.setx(20*each[0])  
            turtle.right(90)
            turtle.pendown()
            turtle.pencolor("red")
            turtle.forward(x)
            turtle.left(90)
            turtle.forward(20*(each[1]-each[0]))
            turtle.left(90)
            turtle.forward(x)
            turtle.penup()
            turtle.right(90)
            turtle.backward(20*(each[1]-each[0]-1))
            x-=20
   
    return 
                  
def showStruct(RNA):
    optiFold=getStruct(RNA,{})
    return render(RNA, optiFold[1])
    