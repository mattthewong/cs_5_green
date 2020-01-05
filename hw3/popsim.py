import matplotlib.pyplot as pyplot
import math
import random
def hplot(low,high):
    '''that has integer values of k from low to high (which are also integers) 
    on the x-axis and plots the sin of k for each k from low to high 
    on the y-axis. '''
    list1 = []
    list2 = []
    for k in range(low,high+1):
        list1.append(k)
        list2.append(math.sin(k))
        pyplot.plot(list1,list2)
        pyplot.show()
def createInitialPop(popSize,p1):
    '''create starting pop given popSize and proportion of A's.'''
    num1 = int(round(p1*popSize))
    num0 = popSize - num1
    popL =['A']*num0+['a']*num1
    return popL
def nextGen(popL):
    '''given population of current generation,obtain 
    next gen by sampling with replacement'''
    newPopL = []
    for n in range(len(popL)):
        newPopL.append(random.choice(popL))
    return(newPopL)
def simplePopSimProportion(popSize,pA,generations):
    '''that does not print out the populations each time. Instead it should
    return a list consisting of the fraction of alleles of type "A" 
    (remember, in this model there are alleles of type "A" and "a") 
    in each generation. Recall that the argument pA is the proportion of the
    initial population with the allele "A". The population should be popSize large,
    and the simulation should be carried out for generations iterations.'''
    fractionlist = []
    popL = createInitialPop(popSize,pA)
    for i in range(generations):
        fraction = (popL.count('A'))*1.0/(popSize)*1.0
        fractionlist.append(fraction)
        popL = nextGen(popL)
    return fractionlist
def plotSimplePopSim(popSize,pA,generations,numTrials):
    '''which calls simplePopSimProportion numTrials times and plots
    the results of each trial.''' 
    
    if numTrials == 0:
        return 
    else:
        pyplot.plot(simplePopSimProportion(popSize,pA,generations))
        return plotSimplePopSim(popSize,pA,generations,numTrials-1)
#1.What changes as you go to larger population sizes?

#with larger population sizes, allele fixation takes longer for the A allele.
#This is because the average for for trial allele fraction is more mediated.

#2.In the small population, one allele or the other always becomes fixed. 
#This is not the case in larger population for the number of iterations
#we are using. If you used a very large (arbitrarily large) number of iterations,
#do you think that you could get all the larger populations to fix too? 

#Eventually, even with the larger populations, one allele or the other will 
#become fixed. However, it will just take many more iterations to get to that point.


    
        
    
     

 
        
    
        
        
        
        
        
        
    
         