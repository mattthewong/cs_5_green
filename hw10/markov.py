import random

def readFile(filename):
    """ reads the given file and returns a list of strings in that file. """
    filehandle = open(filename, "r")
    contents = filehandle.read()
    stringList = contents.split()
    filehandle.close()
    return stringList

def starters(words, k):
    """ Takes a list of words and a parameter k and returns a list of
        tuples, each with the first k words of a sentence in the words
        list. """
    endsymlist = [".", "!","?"]
    LargeList = []
    temp = []
    for i in endsymlist:
        for x in range(len(words)):
            if i not in words[x]:
                temp.append(words[x])
            else:
                temp.append(words[x])
                LargeList.append(temp)
                temp = []
        completeList = []
        for lists in LargeList:
            completeList.append(tuple(lists[0:k]))
            
    return completeList
        

def learn(words, k):
    """ Takes the list of strings and a parameter k>=1 as input and
        returns a dictionary in which the keys are all the k-tuples
        of consecutive words in the dictionary and the value associated
        with a key is the list of all words - with repetitions - that 
        appear immediately after that k-tuple. """
        
    D = {}
    for i in range(0,len(words)-k):
        kword = tuple(words[i:i-k])
        if kword in D:
            D[(kword)] = [words[i+k]]
            

def generate(markovD, length, starterList):
    """ Takes a Markov dictionary, the desired length of the output
        text, and list of the starter tuples  and generates random 
        text of the specified length or more. """
    
    Starter = random.choice(starterList)
    for word in Starter:
        print word,
   
        
    count = 0
    while count < length:
                
            value = markovD[Starter]
            word = random.choice(value)
            print word,
                
            if word[-1] in ['.', '!', '?']:
                Starter = random.choice(starterList)
                    
                startList = list(Starter)
                startList.remove(startList[0])
                startList.append((word,))
                Starter = tuple(startList)
                count += 1
    return Starter
        
    

def main():
    fileName = raw_input("Enter the name of a training file: ")
    k = input("Enter k: ")
    n = input("Enter approximate output length: ")
    text = readFile(fileName)
    starts = starters(text, k)
    D = learn(text, k)
    generate(D, n, starts)



