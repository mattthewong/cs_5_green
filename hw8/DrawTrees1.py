import turtle

Groodies =  ( "X",
             
                ("Y",
                    ("W", (), ()),
                    ("Z",
                        ("E", (), ()),
                        ("L", (), ())
                    )
                ),
                ( "C", (), () )
            )

def drawPhyloTree(Tree):
    '''that takes a tree as input and uses the turtle to draw a pictorial
    representation of that tree.'''
    if Tree == ():
        return 
    elif Tree[1] == ():
        return turtle.write(Tree[0], font = ('Arial', 14, 'normal'))
    else:
        turtle.write(Tree[0], font = ('Arial', 14, 'normal'))
        turtle.left(45)
        turtle.forward(50)
        turtle.right(45)
        turtle.write(Tree[1][0], font = ('Arial', 14, 'normal'))
        drawPhyloTree(Tree[1])
        turtle.left(45)
        turtle.backward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.left(45)
        turtle.write(Tree[2][0], font = ('Arial', 14, 'normal'))
        drawPhyloTree(Tree[2])
        turtle.right(45)
        turtle.backward(50)
        turtle.left(45)

