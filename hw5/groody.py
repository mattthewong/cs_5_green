def superLCS(S1,S2):
    """returns a list of three items: the lenth 
    of the LCS and two input strings. These two
    strings wil  be identical to the original
    two input strings except that they will both have
    the same length and will contain a symbol '-' at any location
    where they mismatch. """

    if S1=='':
        return[0,'-'*len(S2),S2]
    elif S2=='': 
        return [0, S1, '-'*len(S1)]
    elif S1[0] == S2[0]:
        match = superLCS(S1[1:],S2[1:])
        match=[1+match[0],S1[0]+match[1],S2[0]+match[2]]
        return match
    else:
        option1 = superLCS(S1,S2[1:])
        option1 = [option1[0],'-'+option1[1],S2[0]+option1[2]]
        
        option2 = superLCS(S1[1:],S2)
        option2 = [option2[0],S1[0]+option2[1],'-'+option2[2]]
        
        if option1[0] > option2[0]:
            return option1
        else: return option2
        

#the longest common subsequence in Eastern and Western Groody Schlitz genes
# is: [12, 'GT-A-CGTCGATAACTG-', '-TGATCGTC-ATAAC-GT']