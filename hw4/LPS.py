# -*- coding: utf-8 -*-
def LCS(String1, String2):
    "returns the longest common subsequence within the two strings."""
    if String1 == "" or String2 == "":return 0
    elif String1[0] == String2[0]:
        return 1 + LCS(String1[1:], String2[1:])
    else:
        option1 = LCS(String1, String2[1:])
        option2 = LCS(String1[1:], String2)
        return max(option1, option2)
def LPS(myString):
    '''that takes a string as input and returns the length of the longest
    palindromic subsequence.'''
    if myString == "": 
        return 0
    reversemyString = myString[len(myString)::-1]
    return LCS(myString, reversemyString)
    
        
        
        
        
            
            
        
            
        
    
    