def subsetRepeat(target,numberList):
    '''returns True if there exists a way to choose numbers from the numberList,
    with repeated use of an item permitted. If there is no such solution, the
    function should return False.'''
    if target == 0: 
        return True
    elif numberList == []: 
        return False
    elif numberList[0] > target: 
        return subsetRepeat(target, numberList[1:])
    else:
        It = numberList[0]
        useIt = subsetRepeat(target-It,numberList)
        loseIt = subsetRepeat(target,numberList[1:])
        return useIt or loseIt
        
        