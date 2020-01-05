import turtle

def FractalTriangle(sideLength, levels):
    '''draws fractal triangles of x side length and x levels.'''
    if levels == 0:
        turtle.forward(sideLength)
        turtle.left(120)
        turtle.forward(sideLength)
        turtle.left(120)
        turtle.forward(sideLength)
        turtle.left(120)
    else:
        FractalTriangle(sideLength/2,levels-1)
        turtle.forward(sideLength)
        turtle.left(120)
        FractalTriangle(sideLength/2, levels-1)
        turtle.forward(sideLength)
        turtle.left(120)
        FractalTriangle(sideLength/2, levels-1)
        turtle.forward(sideLength)
        turtle.left(120)
        FractalTriangle(sideLength/2, levels-1)
        return

        
    
        