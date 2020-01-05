def palindrome(input):
    if input == input[::-1]:
        return True
    else:
        return False
def fancyPal(string):
    lowerstring = string.lower()
    for value in lowerstring:
        if value == ',' or value == ' ' or value == '.':
            
            
            
            