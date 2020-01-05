def ORFadviser(DNA):
    if DNA[0:3] == 'ATG':
        if DNA[-3:] == 'TGA' or DNA[-3:] == 'TAG' or DNA[-3:] == 'TAA':
            if len(DNA) % 3 == 0:
                return 'This is an ORF'
    elif DNA[0:3] != 'ATG':
        return 'The first three bases arae not ATG'
    elif DNA[-3:] != 'TGA' or DNA[-3:] != 'TAG' or DNA[-3:] != 'TAA':
        return 'The last three bases are not a stop codon'
    else:
        return 'The string is not of the correct length'
        
def friendly(greeting):
    if greeting[0:5] == 'Hello' or greeting[0:2] == 'Hi':
        return 'What is up?'
    elif greeting[-1:] == '?':
        return 'Good question'
    else:
        return 'I am sorry, but I did not understand you.'
        