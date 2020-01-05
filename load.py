f = open("goodStuff.txt") # open the file
linesList = f.readlines() # read in the file as a list of its lines
f.close()
def list(linesList):
    newList = []
    for line in linesList:
        newList.append(line[:-1])
        return newList
        
def loadSeq(fileName):
    f = open(fileName)
    linesList = f.readlines()
    f.close()
    newStrings = ""
    DNA = linesList[1:]
    for string in DNA:
        newString +=(string[:-1])
    return newString