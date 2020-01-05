def alignScore( S1, S2, gap, subMat ):
    ''' Returns the sequence alignment score for S1 and S2. '''
    if S1 == '': 
        return gap * len(S2)
    elif S2 == '': 
        return gap * len(S1)
    else: 
        option1 = subMat[(S1[0], S2[0])] + alignScore(S1[1:], S2[1:], gap, subMat)
        option2 = gap + alignScore(S1[1:], S2, gap, subMat)
        option3 = gap + alignScore(S1, S2[1:], gap, subMat)
        return max(option1, option2, option3)
        
dnamat = {('A', 'A'): 5, ('A', 'T'): -4, ('A', 'G'): -1, ('A', 'C'): -4,
          ('T', 'A'): -4, ('T', 'T'): 5, ('T', 'G'): -4, ('T', 'C'): -1,
          ('G', 'A'): -1, ('G', 'T'): -4, ('G', 'G'): 5, ('G', 'C'): -4,
          ('C', 'A'): -4, ('C', 'T'): -1, ('C', 'G'): -4, ('C', 'C'): 5}     
        
def align( S1, S2, gap, subMat ):
    ''' Returns a list that contains the S1 and S2 distance
    along with two strings that show the alignment. '''
    if S1 == '': 
        return [gap * len(S2),"-"*len(S2),S2.lower()]
    elif S2 == '': 
        return [gap * len(S1),S1.lower(), "-"*len(S1)]
    
    else:
            if S1[0] == S2[0]:
                option1 = align(S1[1:], S2[1:], gap, subMat)
                
                option1 = [subMat[(S1[0], S2[0])] + option1[0],S1[0] + option1[1],S2[0] + option1[2]]
            else:   
                option1 = align(S1[1:], S2[1:], gap, subMat)
                
                option1 = [subMat[(S1[0], S2[0])] + option1[0],S1[0].lower() + option1[1],S2[0].lower() + option1[2]]
        
            option2 = align(S1[1:], S2, gap, subMat)
            option2 = [gap + option2[0],S1[0].lower() + option2[1], '-' + option2[2]]
        
            option3 = align(S1, S2[1:], gap, subMat)
            option3 = [gap + option3[0],'-' + option3[1],S2[0].lower() + option3[2]]
        
            return max(option1, option2, option3)
        
def prettyAlign(S1,S2,gap,subMat):
    """takes two strings and a cost matrix as input. It then simply calls your align function to compute an optimal alignment. 
    Finally, it takes the alignment found by align and prints the score and then the two aligned strings, one above the other"""
    
    list = align( S1, S2, gap, subMat )
    
    print "Score", list[0]
    print list[1]
    print list[2]