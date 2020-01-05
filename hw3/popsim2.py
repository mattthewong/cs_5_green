#Matt Wong
#CS5Green/30 September 2014
import random
import matplotlib.pyplot as pyplot
def createInitialPop(popSize, pA):
    """Create starting pop given popSize and proportion of 1s."""
    num0=int(round(pA*popSize))
    num1=popSize-num0
    popL=["A"]*num0+["a"]*num1
    return popL
def nextGen(popL):
    """Given population of current generation, obtains next gen by
    sampling with replacement."""
    newPopL=[]
    for n in range(len(popL)):
        newPopL.append(random.choice(popL))
    return(newPopL)  
def uniquify(myList):
    """returns new list that is just myList but with duplicates removed"""
    if myList==[]: return[]
    
    elif myList[0] in myList[1:]:
        return uniquify(myList[1:])
        
    else: 
        return [myList[0]]+uniquify(myList[1:])
def evePlot(popSize,generations):
    '''that takes two inputs, the population size and the number of generations
    to simulate and tracks
    how many unique mitochondrial DNA alleles there are as we go forward
    from generation to generation.'''
    xaxis = []
    yaxis = []
    popL = range(popSize)
    for i in range(generations):
        uniqueAlleleList = uniquify(popL)
        popL = nextGen(popL)
        xaxis= xaxis +[i]
        yaxis= yaxis +[len(uniqueAlleleList)]
    print "Number of distinct mitochondrial DNA in last generation:", uniqueAlleleList[-1]
    pyplot.plot(xaxis,yaxis)
    pyplot.show()
def naturalSelection(popsSize, pA, gen, s):
    """Gives the fraction of A that survived in each generation in 
    terms of natural selection, varied from the simplePopSimProportion function."""
    popL = createInitialPop(popsSize,pA)
    SelectedList = []
    for i in range(gen):
        fraction = (popL.count("A"))*1.0/(popsSize*1.0)
        SelectedList.append(fraction)
        popL = newGen(popL,s) 
    return SelectedList
def newGen(popL,s):
    """selects organisms to copy for the new generation not randomly, 
    but biased by fitness values and the fraction of 'A' alleles."""
    newPopL=[]
    survivalList=[]
    for i in range(len(popL)):
        if popL[i] == "A":
            if random.random() < s: 
                survivalList = survivalList + ["A"]
            else: 
                survivalList   
        elif popL[i] == "a":
            if random.random() < (1-s):
                survivalList = survivalList + ["a"]
            else:
                survivalList      
    for i in range(len(popL)):
        newPopL.append(random.choice(survivalList))
    return(newPopL)
def plotSelectPopSim(popsSize, pA, gen, s, numTrials):
    """calls naturalSelection numTrials times and plots the results of each trial.
    plotSelectPopSim should not contain a call to pyplot.show(). Used recursion for"""
    if numTrials == 0:
        return
    else:
        pyplot.plot(naturalSelection(popsSize, pA, gen, s))
        return plotSelectPopSim(popsSize, pA, gen, s , numTrials-1)
        
#plotSelectPopSim visually represented the changes in allele frequency based on natural selective factors. 
#This was visually represented in this problem where high natural selective factors helped to increase the
#proportion of specific alleles, while a reduction in these factors did the reverse. 



        
    