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
def find(node, Tree):
    ''' Returns True if node is in the Tree and False otherwise. '''
    if Tree == (): return False
    elif Tree[0] == node: return True # found it at the Root!
    else:
        return find(node, Tree[1]) or find(node, Tree[2])

def nodeList(Tree):
    """Returns the list of all nodes in Tree."""
    if Tree[1] == ():
        return [Tree[0]]
    else:
        return [Tree[0]]+nodeList(Tree[1])+nodeList(Tree[2])
def subtree(node,Tree):
    """Returns the subtree of the given Tree rooted at the given node. This
    function returns the tree beginning at node."""
    if Tree[0] == node:
         return Tree
    elif Tree == ():
        return Tree
    if not find(node, Tree):
        return ()
    else:
        return subtree(node,Tree[1]) + subtree(node,Tree[2])
def descendantNodes(node,Tree):
    """Returns the list of all descendant nodes of the given node in the Tree.
    This function will not be recursive itself, but it will call the nodeList
    and subtree functions for help."""
    if Tree == ():
        return []
    if Tree[0] == node:
        return nodeList(Tree)[1:]
    elif not find(node, Tree):
        return []
    else:
        return nodeList(subtree(node,Tree))[1:]
def parent(node, Tree):
    """ returns the parent of the given node in the Tree. If the node has no
    parent in the tree, the function should return the special value None."""
    if Tree[0] == node:
         return None
    elif not find(node,Tree):
        return None
    elif Tree[1][0] == node: return Tree[0]
    elif Tree[2][0] == node: return Tree[0]
    
    else:
        Root = Tree[0]
        Left = Tree[1]
        Right = Tree[2]
        
        if find(node,Left):
            return parent(node,Left)
        elif find(node,Right):
            return parent(node,Right)
def scale(Tree,scaleFactor):
    """takes a Tree as input, and multiplies the numbers at its internal nodes
    by scaleFactor and returns a new tree with those values."""
    if Tree == (): return Tree
    if Tree[1] == ():
        if isinstance(Tree[0], float): 
            return (scaleFactor * Tree[0], (), ())
        else:
            return(Tree[0], (), ())
    else:
        return ((scaleFactor * Tree[0]), (scale(Tree[1], scaleFactor)), (scale(Tree[2], scaleFactor)))
        
        
    
        
    
    
    

         
    
        
        
        