def memoizedSubset(target,numberTuple, memo):
    """works exaclty like the subset function, but uses memoization
    to process in a more efficicent way."""
    if target == 0: 
        return True
    elif numberTuple == (): 
        return False
    elif (target, numberTuple) in memo:
        return memo[(target,numberTuple)]
    else:
    
        if numberTuple[0] > target: 
            best = memoizedSubset(target,numberTuple[1:], memo)
        else:
            useIt = memoizedSubset(target-numberTuple[0],numberTuple[1:], memo)
            
            loseIt = memoizedSubset(target, numberTuple[1:],memo)
        
            best = useIt or loseIt
        
    memo[(target,numberTuple)] = best
    return best
    
    