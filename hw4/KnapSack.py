def knapsack(capacity,items):
    '''that takes a positive integer capacity and a list of items
    (such as stuff in the example above) where each item in the list
    is itself a list of the form [weight, value]. Then knapsack returns
    the best solution, which is maximum total value of items you can 
    pack.'''
    if capacity == 0: return 0
    elif items == []: return 0
    else:
        It = items[0][0]
    if It > capacity:
        return knapsack(capacity, items[1:])
    else:
        useIt = items[0][1] + knapsack(capacity-It, items[1:])
        
        loseIt = knapsack(capacity, items[1:])
    return max(useIt, loseIt)

            
        
        
            