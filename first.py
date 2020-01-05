def power(x):
    """takes any value x and returns x^x"""
    return x**x
    
def stringMultiply(myString, number):
    """that takes as input a string called myString and a positive integer called number 
    and returns a new string that is the concatenation of number copies of myString"""
    return myString * number
     
def listMaker(myString, number):
    """takes as input a string called myString and a positive integer called number
    and returns a list that contains number copies of that myString"""
    list1 = [myString]
    return list1 * number
    
def palindromeMaker(input):
    """takes a string named input and returns a new string
    that is the input string followed by its reversal"""
    return str(input) + str(input[1000000000::-1])
   

    
    
    