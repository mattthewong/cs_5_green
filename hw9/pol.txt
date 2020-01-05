#Matt Wong 11/10/2014

import sys, random
sys.setrecursionlimit(100000)
from rna import *
from hivSeqs import *

def rnaWin(RNA,wsize,step):
    """ runs a sliding window over RNA and uses mfold5 to calculate the optimal
    number of matches in each window. RnaWin should return a tuple comprising
    the score of the optimal window, its start position, and its sequence.
    """
    windowcount = ((len(RNA)-wsize)/step)+1
    newbestscore = 0
    
    for i in range(0,windowcount*step,step):
        Score = mfold5(RNA[i:i+wsize],{})
        if Score > newbestscore:
            newbestscore = Score
                  
            
    return (newbestscore,i, RNA[i:i+wsize])
            
def randSeq(RNA):
    '''Takes an RNA string as input and returns a new string formed by
    randomly shuffling the symbols in the given string.'''
    L = list(RNA)
    random.shuffle(L)
    return "".join(L)            
            
def randomWins(RNA, wsize, step, trials):
    """that takes an RNA input, shuffles it, and calculates the best scoring
    window using rnaWin(wsize, step). It should repeat this process trials times
    and store the maximum score from each trial in a list. At the end it should
    return that list."""
    counter = 0
    rnatrialscores = []
    while counter < trials:
        newRNA = randSeq(RNA)
        rnatrialscores.append(rnaWin(newRNA, wsize, step)[0])
        counter += 1 
        
    return rnatrialscores
        
def findSecStrucWrapper():
    '''Wrapper function to search HIV Pol gene for secondary
    structure.'''
    bestScoreHIV, bestPosHIV, bestSeqHIV = rnaWin(hivPol, 60, 30)
    randomWinsList = randomWins(hivPol,60,30,100)
    p = pval(bestScoreHIV,randomWinsList)
    print "Best window score:", bestScoreHIV
    print "Best window position:", bestPosHIV
    print "Best window seq:", bestSeqHIV
    print "Best window pvalue:", p 
    print "List of Scores:", randomWinsList
                        
def pval(trueVal,randomWinsList):
    """Calculates an empirical p-value based on the list of scores from randomly
    shuffled sequences that we can compare with our real score."""
    pvaluelist=[]
    denom=len(randomWinsList)
    for num in randomWinsList:
        if num >= trueVal:
            pvaluelist.append(num) 
            pvaluelistLen = len(plist)
                  
    return pvaluelistLen*1.0/denom*1.0