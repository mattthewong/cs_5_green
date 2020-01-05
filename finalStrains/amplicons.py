#Jacob Fiksel and Matt Wong
#amplicons.py
#12/12/14

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

def containsCandidateRegion(blockL, start, end):
    '''Takes an alignment block as input. It evaluates whether
    the given region, which is inputed by the start and end
    of the region, that is to be evaluated is identical
    in all strains'''
    
    for i in range(len(blockL)):
        for j in range(len(blockL)):
            if blockL[i][start:end]!=blockL[j][start:end]:
                return False
    return True
    
def extendCandidateRegion(blockL, start, end):
    '''Takes an alignment block as input. Uses containsCandidateRegion
    to evaluate whether the given start and end region is identical
    in all strains. If so, it extends the end of the region
    to find the longest possible identical region with the given
    start point, and returns the new endpoint'''
    newEnd=end
    test=containsCandidateRegion(blockL, start, end)
    while test==True:
        if newEnd+1==len(blockL[0])+1:
            test=False
        elif containsCandidateRegion(blockL, start, newEnd+1)==True:
            newEnd+=1
            test=containsCandidateRegion(blockL, start, newEnd+1)
        else:
            test=False
    return newEnd
        
def blockPrimers(blockL, minPrimerSiteSize):
    '''Takes an alignment block as input. Within this block it
    finds candidate regions, which consist of minPrimerSiteSize bases
    in a row that are identical in all strains, where a primer could bind.
    Each putative primer site is recorded in a tuple like this: (start,end).
    The function returns a list of such tuples.''' 
    
    tupleList=[]
    i=0
    while i <=len(blockL[0])-minPrimerSiteSize:
        if containsCandidateRegion(blockL, i, i+minPrimerSiteSize)==True:
            newEnd=extendCandidateRegion(blockL, i, i+minPrimerSiteSize)
            tupleList.append((i,newEnd))
            i+=newEnd-i
        else:
            i+=1
    return tupleList
    
def chopAmplicon(blockL, start, end):
    '''Creates a list containing the strings of each element
    in blockL that are contained within the start and end
    region'''
    output=[]
    for block in blockL:
        output.append(block[start:end])
    return output

           
def findBlockAmplicons(blockL, minPrimerSiteSize,minAmpliconSize,maxAmpliconSize):
    '''Finds potential primer sites for blockL. It then finds if pairs of primer sites
    will produce an amplicon between maxAmpliconSize and minAmpliconSize large.
    If so, it returns a list of lists, with each list containing the alignment
    block from the first primer to the end of the second'''
    primerL=blockPrimers(blockL, minPrimerSiteSize)
    blockAmpliconList=[]
    if len(primerL)<=1:
        return []
    else:
        for i in range(len(primerL)-1):
            for j in range(i+1, len(primerL)):
                ampliconSize=primerL[j][1]-primerL[i][0]
                if ampliconSize >= minAmpliconSize and ampliconSize <= maxAmpliconSize:
                    start=primerL[i][0]
                    end=primerL[j][1]
                    blockAmpliconList.append(chopAmplicon(blockL, start, end))
    return blockAmpliconList
     

def amplicons(seqsL,minPrimerSiteSize,minAmpliconSize,maxAmpliconSize):
    '''The function amplicons takes a list of blocks as input. 
    It loops over blocks, and in each block it calls blockPrimers 
    to get a list of putative primer sites. It then considers pairs
    of these sites, identifying those pairs which would produce an
    amplicon between maxAmpliconSize and minAmpliconSize large.When 
    it finds a qualifying amplicon, it chops out an alignment block from 
    the beginning of the first primer to the end of the second'''
    ampliconList=[]
    for blockL in seqsL:
        blockAmpliconList=findBlockAmplicons(blockL, minPrimerSiteSize,minAmpliconSize,maxAmpliconSize)
        if blockAmpliconList!=[]:
            ampliconList.extend(blockAmpliconList)
    return ampliconList
    
    