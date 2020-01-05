from DrawTrees2 import *
from PhylogeneticTrees import *
from mitoData import *

def leafCount(Tree):
    '''Computes total number of nodes in a given tree'''
    if Tree[1] == ():
        return
    else:
        return leafCount(Tree[1]) + leafCount(Tree[2])
def findClosestPair(speciesList, Distances):
    '''This function takes as input a species list (a list of trees represented
    as tuples) and a distance dictionary and returns the pair of distinct trees
    in the speciesList that have the least distance between them.'''
    distancesList = []
    pair = ()
    minDistance = float('inf')
    for i in speciesList:
        for j in speciesList:
            if i != j and Distances[(i, j)] != 0:
                distancesList.append(Distances[(i,j)])
                if Distances[(i,j)] < minDistance:
                    minDistance = Distances[(i, j)]
                    pair = (i,j)
    return pair
def updateDist(speciesList,Distances,newTree):
    '''This function takes the current list of trees called speciesList,
    the Distances dictionary, and the new tree that we have just built by
    merging the closest pair of species (as found by findClosestPair).
    This function does not return anything, but it does modify the Distances
    dictionary.'''
    
    node = newTree[0]
    treeI = newTree[1]
    treeJ = newTree[2]
    newTree = (node,treeI, treeJ)
    
    for TreeK in speciesList:
        newDistance = (1.0*leafCount(treeI))/(1.0*leafCount(treeI) + leafCOunt(treeK)) * (Distances[t(reeI,TreeK)]) + (1.0*leafCount(treeJ))/(1.0*leafCount(treeJ)) * (Distances[(treeI, TreeK)]) + (1.0*leafCount(treeJ))/(1.0 * leafCount(treeI)) + leafCount(treeJ)) * Distances[(treeJ,TreeK)])
        Distances[(treeK,(node,treeII,treeJ))] = newDistance
        Distances[(node,treeI, treeJ),treeK] = newDistance
def upgma(speciesList,Distances):
    '''This function takes as input the the speciesList and the distance dictionary
    and runs the algorithm that we described in the text. It repeatedly 
    does the following until there is only one tree in the speciesList, 
    at which point that phylogenetic tree is returned.'''
    while len(speciesList) > 1:
        closestPair = findClosesPair(speciesList, Distances)
        treeI = closestPair[0]
        treeJ = closestPair[1]
        newTree = (0.5*(Distances[(treeI,treeJ)]), treeI, treeJ)
        speciesList.remove(treeI)
        speciesList.remove(treeJ)
        updateDist(speciesList, Distances, newTree)
        speciesList.append(newTree)
        
    return speciesList[0]
    

#Are Neanderthals more closely related to modern Europeans than to other modern humans?
Yes
#Does this data support a the out of Africa model for modern human origins (or the alternative multiregional model)?
Out of Africa
#Compare the divergence time of Neanderthals from modern humans with that among modern human groups. What is the ratio between these two? 
    0.12 %
        
    
        
        
        
    
        
        