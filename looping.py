def countLength(DNAlist, length):
    rightlengthstrings = 0
    for string in DNAlist:
        if len(string) == length:
            rightlengthstrings = rightlengthstrings +1
    return rightlengthstrings
    