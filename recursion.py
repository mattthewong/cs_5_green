def dot(L,K):
#outputs the dot product of the lists L and K
    if L == []:
        if K == []: 
            return 0.0
    else:
        return L[0]*K[0] + dot(L[1:],K[1:])
def GCcount(DNA):
#takes DNA string as input and returns the number of G's and C's that appear
#in that string.
    if DNA == "":
        return 0.0
    elif DNA[0] == 'G' or DNA[0] == 'C':
        return 1 + GCcount(DNA[1:])  
    else:
        return GCcount(DNA[1:])   
def countStarts(DNA):
# takes a DNA string as input and returns the number of times the string 'ATG'
#appears in that string. 
    if DNA == "":
        return 0.0    
    elif DNA[0:3] == 'ATG':
        return 1 + countStarts(DNA[1:])    
    else:
        return countStarts(DNA[1:])
def explode(S):
#takes a string S as input and should return a list of the characters 
#(each of which is a string of length 1) in that string
    if S == "":
        return []
    else:
        return [S[0]] + explode(S[1:])
    
def ind(e,L):
#takes an element e and a sequence L where ind should return the index
#where e is first found in L. Counting starts at 0 and if e isn't an element
#of L, then ind(e,L) should return an integer that is at least the length of 
#L(meaning the element I'm looking for isnt in the list or string)
    if L == [] or L == "":
        return 0.0
    elif e == L[0]:
        return 0
    if e not in L:
        return len(L)
    else:
        return 1 + ind(e,L[1:])
    

    

        
    
