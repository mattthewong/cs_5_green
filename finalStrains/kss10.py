#Jacob Fiksel and Matt Wong
#kss10.py
#12/12/14

from ecoli10 import *
from amplicons import *
from operator import itemgetter

def kss10(seqsL,minPrimerSiteSize,minAmpliconSize,maxAmpliconSize, numBest):
    '''takes a list of sequence blocks as input (e.g. seqs10L).
    It then determines the numBest best amplicons and prints them to
    the screen.'''
    ampliconList = amplicons(seqsL,minPrimerSiteSize,minAmpliconSize,maxAmpliconSize)
    bestList=[]
    for i in range(len(ampliconList)):
        minDist=minPairDistance(ampliconList[i])
        bestList.append([ampliconList[i], minDist])
    sortedBestList = sorted(bestList, key=itemgetter(1), reverse=True)
    #Print output to textfile
    f = open("kss10.txt", "w")
    for i in range(numBest):
        print >>f,"The " + "#"+str(i+1) + " best amplicon is:"
        print >>f,makeGuideString(sortedBestList[i][0])
        for seq in sortedBestList[i][0]:
            print >>f,seq 
            print >>f," "
        print >>f, " "
    f.close()

def pairDistance(seq1, seq2):
    '''Determines the number of sites that differ between
    sequence1 and sequence 2'''
    diff = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            diff +=1
    return diff

def minPairDistance(amplicon):
    '''Determines the minimimum pairwise distance between all
    pairs of sequences in an amplicon'''
    minDist = float('inf')
    for i in range(len(amplicon)):
        for j in range(len(amplicon)):
            if i < j:
                dist = pairDistance(amplicon[i], amplicon[j])
                if dist <=minDist:
                    minDist = dist
    return minDist
    
def makeGuideString(amplicon):
    '''takes an amplicon as input (a list of aligned sequences).It returns
    a string which indicates which alignment columns are all the same, and
    which are not all the same.'''
    SeqNum = len(amplicon)
    Seqlen = len(amplicon[0])
    output = ''
    for base in range(Seqlen):
        for n in range(SeqNum):
            nextletter = '-'
            if amplicon[0][base] != amplicon[n][base]:
                nextletter = '*'
                break
        output += nextletter
    return output     

        
                
        
        
    
        
    