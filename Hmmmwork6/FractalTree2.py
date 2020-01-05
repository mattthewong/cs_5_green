import turtle

def fractalTree2(angle,scale,trunkLength,levels):
    """takes the angle as an argument. It also takes scale, which specifies an
    amount by which we multiply trunk length as we go from one level to the next
    (i.e. if we set scale to 0.5, it will cut trunkLength in half at each level)
    . And it uses the variable levels to determine how many levels to go before
    stopping."""
    if levels == 0: return
    else:
        turtle.forward(trunkLength)
        turtle.left(angle)
        fractalTree2(angle,scale,trunkLength*scale,levels-1)
        turtle.right(angle)
        turtle.right(angle)
        fractalTree2(angle,scale,trunkLength*scale,levels-1)
        turtle.left(angle)
        turtle.backward(trunkLength)
        
def fractalTree(trunkLength):
    """draws fractal trees"""
    if trunkLength < 10:
        return
    else:
        turtle.forward(trunkLength)
        turtle.left(45)
        fractalTree(trunkLength/2.0)
        turtle.right(90)
        fractalTree(trunkLength/2.0)
        turtle.left(45)
        turtle.backward(trunkLength)