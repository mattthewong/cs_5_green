from load import *
from dna import *
import random

def restOfORF(DNA):
    newList = ''
    for i in range(0, len(DNA),3):
        if DNA[i:i+3] != 'TAG' and DNA[i:i+3] != 'TAA' and DNA[i:i+3] != 'TGA':
                newList = newList + DNA[i:i+3]
        else:
            return newList
def oneFrameV2(DNA):
    output = []
    for i in range(len(DNA)):
        if DNA[i:i+3] == 'ATG':
            output = output + [restOfORF(DNA[i:])]
        return output
    
def longestORFV2(DNA):
    output = []
    for i in range(len(DNA)):
        if DNA[i:i+3] == 'ATG':
            output = output + oneFrameV2(DNA[i:])
        return output
def longestORFBothStrands(DNA):
    list1 = []
    list2 = []
    for string in DNA:
        list1 = longestORFV2(DNA[i:])
        list2 = longestORFV2(reverseCompliment(DNA[i:]))
        combinedlist = list1 + list2
        output = reduce(longest, combinedlist)
        return output
def longest(x,y):
    if len(x) > len(y):
        return x
    return y
def longestORFNoncoding(DNA,numReps):
    counter = 0 
    myList1 = []
    lengthList = []
    while counter < numReps:
        for symbol in DNA:
            myList = list(DNA)
        random.shuffle(myList)
        
        myList1 = myList1 + [collapse(myList)]
        
        for i in range(len(myList1)):
            BestORF = longestORFBothStrands(myList1[i])
            lengthList = lengthList + [len(BestORF)]
            counter = counter + 1
        return reduce(longer, lengthList)
def longest(x,y):
    if len(x) > len(y):
        return x
    return y
def collapse(L):
    output = ""
    for s in L:
        output = output + s
    return output
def findORFs(DNA):
    output = []
    for i in range(len(DNA)):
        output = output + oneFrameV2(DNA[i:])
    return output
def findORFsBothStrands(DNA):
    list1 = ""
    list2 = ""
    for string in DNA:
        list1 == reverseComplement(DNA) + list1
        list2 == ForwardComplement(DNA) + list2
        combinedList = [list1]+[list2]
        return combinedList



        

        
    
    
    
    
    
