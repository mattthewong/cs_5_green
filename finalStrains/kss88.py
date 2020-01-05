#Jacob Fiksel and Matt Wong
#kss88.py
#12/12/14

from ecoli88 import *
from amplicons import *
from operator import itemgetter



def kss88(alignmentBlockL,minPrimerSiteSize,minAmpliconSize,maxAmpliconSize, numBest):
    '''Creates sets of amplicons based off the amplicon function,
    and judges them using the numDistinguishableStrains function.
    It returns the numBest pairs of primers'''
    
    ampliconL = amplicons(alignmentBlockL, minPrimerSiteSize,minAmpliconSize,maxAmpliconSize)
    primerSets=[]
    
    for i in range(len(ampliconL)):
        for j in range(len(ampliconL)):
            if i <=j:
                joined = joinAmplicons(ampliconL[i], ampliconL[j])
                score = numDistinguishableStrains(joined)
                setList = [ampliconL[i], ampliconL[j], score]
                primerSets.append(setList)
    sortedPrimerSets = sorted(primerSets, key=itemgetter(2), reverse=True)
    return sortedPrimerSets[:numBest]
    
def printKss88():
    '''Prints the output from kss88 to a text file'''
    kss88output = kss88(seqs88L, 50, 200, 500, 5)
    f = open("kss88.txt", "w")
    for i in range(len(kss88output)):
        print >>f,"The " + "#"+str(i+1) + " best amplicon pair is:"
        print >>f,"First amplicon:"
        print >>f,makeGuideString(kss88output[i][0])
        for seq in kss88output[i][0]:
            print >>f,seq
            print >>f, " "
        print >>f," "
        print >>f,"Second amplicon:"
        print >>f,makeGuideString(kss88output[i][1])
        for seq in kss88output[i][1]:
            print >>f,seq
            print >>f, " "
        print >>f," "
    f.close()
    

def joinAmplicons(amplicon1, amplicon2):
    '''Takes two amplicons, each of which is a list of sequences, 
    and returns a new list, which combines the elements of amplicon1
    and amplicon2'''
    newAmpliconL=[]
    for i in range(len(amplicon1)):
        newAmpliconL.append(amplicon1[i]+amplicon2[i])
    return newAmpliconL
        
def numDistinguishableStrains(amplicon):
    '''Takes a list of aligned sequences as input and 
    returns the number that are distinguishable'''
    numDistinct=0
    for i in range(len(amplicon)):
        if amplicon[i] not in amplicon[i+1:] and amplicon[i] not in amplicon[:i]:
            numDistinct+=1
    return numDistinct
    
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
        
