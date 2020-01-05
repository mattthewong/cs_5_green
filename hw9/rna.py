import sys
sys.setrecursionlimit(100000)
from hivSeqs import *

def fold(RNA):
    """Use-it-or-lose-it RNA secondary structure prediction, returns
    score."""
    if len(RNA)<2:
        return 0
    else:
        bestSoFar=fold(RNA[1:])     # lose it case
        for i in range(1,len(RNA)): # use it cases
            if isComplement(RNA[0],RNA[i]):
                score=1+fold(RNA[1:i])+fold(RNA[(i+1):])
                if score>bestSoFar:
                    bestSoFar=score
        return bestSoFar
        
def isComplement(base1,base2):
    """Returns boolean indicating if 2 RNA bases are complementary."""
    if base1=="A" and base2=="U":
        return True
    elif base1=="U" and base2=="A":
        return True
    elif base1=="C" and base2=="G":
        return True
    elif base1=="G" and base2=="C":
        return True
    if base1=="G" and base2=="U":
        return True
    elif base1=="U" and base2=="G":
        return True
    else:
        return False
        
def mfold(RNA, memo):
    """Use-it-or-lose-it RNA secondary structure prediction, returns
    score."""
    if len(RNA) < 2:
        return 0
    elif (RNA) in memo:
        return memo[(RNA)]

    else:
        bestSoFar= mfold(RNA[1:],memo)     # lose it case
        for i in range(1,len(RNA)): # use it cases
            if isComplement(RNA[0],RNA[i]):
                score=1+mfold(RNA[1:i], memo)+mfold(RNA[(i+1):], memo)
                if score>bestSoFar:
                    bestSoFar=score
        memo[(RNA)] = bestSoFar
        return bestSoFar
def mfold5(RNA,memo):
    ''' is just like your mfold function but only permits pairs that are
    at least five positions apart. The solution scores we get now will be
    lower than what we got with mfold because we are inhibiting nearby
    matches.'''
    if len(RNA) < 2:
        return 0
    elif (RNA) in memo:
        return memo[(RNA)]

    else:
        bestSoFar= mfold(RNA[1:],memo)     # lose it case
        for i in range(1,len(RNA)): # use it cases
            if isComplement(RNA[0],RNA[i]):
                if range(RNA[0],(RNA[i])) > 5: 
                    score=1+mfold(RNA[1:i], memo)+mfold(RNA[(i+1):], memo)
                    if score > bestSoFar:
                        bestSoFar=score
        memo[(RNA)] = bestSoFar
        return bestSoFar
    
    
        
