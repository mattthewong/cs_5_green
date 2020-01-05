import random
def lengthToATG():
    counter = 0
    newcontainer = ""
    while counter <=3 or newcontainer[counter-4:counter-1] != "ATG":
        newcontainer += random.choice(['A','T','C','G'])
        counter = counter + 1
    return counter
def meanToATG(trials):
    newcounter = 0
    newcontainer = ""
    while newcounter <= 3 or newcontainer[newcounter-4:newcounter-1] !='AAA':
        newcontainer += random.choice(['A','T','C','G'])
        newcounter = newcounter +1
    return newcounter
def meanToAAA(trials):
    newcounter = 0
    for x in range(trials):
        newcounter = lengthToAAA() + newcounter