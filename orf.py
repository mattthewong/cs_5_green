#worked with Koffi
from dna import *
from load import *
def restOfORF(DNA):
    newList = ''
    for i in range(0, len(DNA),3):
        if DNA[i:i+3] != 'TAG' and DNA[i:i+3] != 'TAA' and DNA[i:i+3] != 'TGA':
                newList = newList + DNA[i:i+3]
        else:
            return newList
                               
def oneFrame(DNA):
    ORFlist = []
    for codon in range(0,len(DNA),3):
        if DNA[codon:codon+3] == 'ATG':
            ORFlist = ORFlist + [restOfORF(DNA[codon:])]
    return ORFlist
def longestORF(DNA):
    list1 = oneFrame(DNA)
    list2 = oneFrame(DNA[1:])
    list3 = oneFrame(DNA[2:])
    combinedList = list1 + list2 + list3
    for i in range(0,len(combinedList)):
        if combinedList == []:
            return
        elif len(combinedList) == 1:
            return combinedList
        elif combinedList[1] > combinedList[0]:
            combinedList = combinedList[1:]  
        else:
            combinedList = combinedList[0] + combinedList[2:]    
def longest(x,y):
    if len(x) > len(y):
        return x
    return y
motBDNASeq = longestORF(salSeq)
motBProtSeq = codingStrandToAA(motBDNASeq)
salSeq = loadSeq("U81861.fa")
            
           
            

    
            
        
       
    
            
             
