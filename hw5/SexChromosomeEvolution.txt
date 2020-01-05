import sys
sys.setrecursionlimit(100000)
from humanChickenProteins import *
from blosum62 import *

def memoAlignScore(S1, S2, gap, subMat,memo):
    '''does the exact same thing as AlignScores, but uses memoization
    to make the process function more efficiently.'''
    if S1 == '': 
        return gap * len(S2)
    elif S2 == '': 
        return gap * len(S1)
    elif (S1, S2, gap) in memo:
        return memo[(S1, S2, gap)]
    else: 
        option1 = subMat[(S1[0], S2[0])] + memoAlignScore(S1[1:], S2[1:], gap, subMat,memo)
        option2 = gap + memoAlignScore(S1[1:], S2, gap, subMat,memo)
        option3 = gap + memoAlignScore(S1, S2[1:], gap, subMat,memo)
        best= max(option1, option2, option3)
        
        memo[(S1, S2, gap)] = best
        return best
        
def allScores(geneList1,geneList2):
    '''takes as input two lists of genes. It then takes every protein in the
    first list and calls memoAlignScore on it with every protein in the second
    list. returns a dictionary as output. The keys in this dictionary are pairs
    of protein names in the form of a tuple.'''
    
    allScoresD = {}
    for geneA in geneList1:
        for geneB in geneList2:
            
            protein1 = geneD[geneA][3]
            
            protein2 = geneD[geneB][3]
            
            allScoresD[(geneA,geneB)] = memoAlignScore(protein1,protein2,-9,blosum62,{})
           
    return  allScoresD  
    
def closestMatch(geneName,allScoresD):
    '''returns the protein from the other species which is most similar
    (has the highest alignment score).''' 
    
    keys = allScoresD.keys()
    
    bestScore = 0
    matchGene = ''
    for x in keys:
        if geneName in x:
            
            score = allScoresD[x]
            
            if score > bestScore:
                
                bestScore = score
                
                matchGene = x
                
    if geneName == matchGene[0]:
        
        return matchGene[1]
                
    return matchGene[0]          

def printBRH(geneName,allScoresD):
    """takes a gene name, and a dictionary of memoAlignScore scores as input.
    It finds and prints the best reciprocal hit for geneName.If there is no best
    reciprocal hit it returns without printing anything."""
    
    match1 = closestMatch(geneName,allScoresD)
    match2 = closestMatch(match1,allScoresD)
    
    if match2==geneName:
        
        
        chromosome1=geneD[match1][0]
        startposition1=geneD[match1][1]
        
        chromosome2=geneD[match2][0]
        startposition2=geneD[match2][1]
        
        print chromosome1, startposition1, match1, '---', chromosome2, startposition2, match2
        
    else: return
        
def runBRHSample():
    '''Prints the best reciprocal hits for sample data. First in human
    chromosome order, then in chicken chromosome order.'''
    allScoresD = allScores(sampleHumanGeneList,sampleChickenGeneList)
    print 'human --- chicken'
    for geneName in sampleHumanGeneList:
        
        printBRH(geneName,allScoresD)
    print
    print 'chicken --- human'
    for geneName in sampleChickenGeneList:
        printBRH(geneName,allScoresD)
           
def runBRH():
    '''Print best reciprocal hits for full data. First in human
    chromosome order, then in chicken chromosome order.'''
    allScoresD=allScores(humanGeneList,chickenGeneList)
    print 'human --- chicken'
    for geneName in humanGeneList:
        printBRH(geneName,allScoresD)
    print
    print 'chicken --- human'
    for geneName in chickenGeneList:
        printBRH(geneName,allScoresD)