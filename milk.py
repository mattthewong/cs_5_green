from reads import *
from dna import *
def mapRead(read, genomeSequence):
    '''searches for the desired DNA read in the genome sequence and returns the
    location of that read in a list of lists.'''
    readlocation = []
    for i in range(len(genomeSequence)):
        if read in genomeSequence[i:len(read)+ i]:
            readlocation = readlocation + [[i,i+ len(read)]]
    return readlocation
def reverseComplement(DNA):
    '''returns the complements of the provided DNA strand.'''
    storecomplement = ""
    for n in DNA:
        n = compBase(n)
        storecomplement = n + storecomplement
    return storecomplement
def mapReadBothStrands(read,genomeSequence):
    '''Works exactly as the previous map function but will reverse the read
    and check the genome sequence for that reversed read'''
    readlocation = []
    reversereadlocation = []
    for i in range(len(genomeSequence)):
        readlocation = readlocation + mapRead(read,genomeSequence)
        reversedread = mapRead(reverseComplement(read))
        reversereadlocation = mapRead(reversedread,genomeSequence)
        return readlocation + reversereadlocation
    
    
        
    
    

    
    
            
            
        