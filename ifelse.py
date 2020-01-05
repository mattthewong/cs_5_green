def absolute(n):
    if n < 0:
        return n*-1
    return n
    
def palindrome4(input):
    if len(input) == 4:
        if input[0] == input[3]:
            if input [1] == input [2]:
                    return True
    return False
    
def ORF(DNA):
    if DNA[0:3] == 'ATG':
        if DNA[-3:] == 'TGA' or DNA[-3:] == 'TAG' or DNA[-3:] == 'TAA':
            if len(DNA) % 3 == 0:
                return True
    else:
        return False
        

    
                