def count(letter, string):
    counter = 0
    for symbol in string:
        if letter == symbol:
            counter = counter+1
    return counter
    
        
        