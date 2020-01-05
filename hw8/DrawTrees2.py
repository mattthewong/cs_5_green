import turtle
ANGLE = 30
CORRECTION = 1.155

myTree = (5,
              (3,
                   ("A", (), ()),
                   ("B", (), ())
              ),
              ("C", (), ())
         )
         
def drawPhyloTree2(Tree,scale):
    '''takes as input a tree and makes sure that the internal nodes are drawn
    according to this "height" (that is the proper horizontal distance away from
    the leaves).This procedure gives you the right distance to travel assuming
    you're going at a specific angle.'''
    if Tree == ():
        return
    elif Tree[1] == ():
        return turtle.write(str(Tree[0]), font = ('Arial', 14, 'normal'))
    else:
        if isinstance(Tree[1][0], int):
            distance = Tree[0] - Tree[1][0]
        else:
            distance = Tree[0]
            
    turtle.write(str(Tree[0]), font = ('Arial', 14, 'normal'))
    turtle.left(ANGLE)
    turtle.forward(distance*CORRECTION*scale)
    turtle.right(ANGLE)
    turtle.write(str(Tree[1][0]), font = ('Arial', 14, 'normal'))
    drawPhyloTree2(Tree[1],scale)
    turtle.left(ANGLE)
    turtle.backward(distance*CORRECTION*scale)
    
    if isinstance(Tree[2][0], int):
        distance = Tree[0] - Tree[2][0]
    else:
        distance = Tree[0]
    
    turtle.right(2*ANGLE)
    turtle.forward(distance*CORRECTION*scale)
    turtle.left(ANGLE)
    turtle.write(str(Tree[2][0]), font = ('Arial', 14, 'normal'))
    drawPhyloTree2(Tree[2],scale)
    turtle.right(ANGLE)
    turtle.backward(distance*CORRECTION*scale)
    turtle.left(ANGLE)
    
    