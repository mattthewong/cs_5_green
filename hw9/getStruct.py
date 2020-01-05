#Matt Wong 

from rna import *

def getStruct(RNA, memo):
    """Returns a tuple in which the first element is the maximum number of matches
    and the second element is a "list of tuples". Each element of that "list of
    tuples" is a tuple of two elements of the form (x, y) where x and y are the
    indices of two nucleotides that are matched in an optimal folding"""
    
    if len(RNA) < 5:
        return (0,[])
        
    elif (RNA) in memo:
        return memo[(RNA)]
    else:
        bestmatch = getStruct(RNA[1:],memo) # lose it case
        bestmatch =(bestmatch[0], adjust(bestmatch[1],1))
        
        for i in range(5,len(RNA)): # use it cases
            if isComplement(RNA[0],RNA[i]):
                score=1+getStruct(RNA[1:i], memo)[0]+getStruct(RNA[(i+1): ], memo)[0]
                if score>=bestmatch[0]:
                    bestmatch =(score, [(0,i)]+adjust((getStruct(RNA[1:i], memo)[1]),1)+adjust((getStruct(RNA[(i+1): ], memo)[1]),i+1))         
            memo[(RNA)] = bestmatch
        return bestmatch

def adjust(pairs, k):
    """takes as input a list of pairs of numbers and an integer k and returns
    a new tuple that increases every number in the pairs by k. 
    """
    outputL = []
    for x in pairs:
        outputL.append((x[0] + k, x[1]+ k))
    return outputL