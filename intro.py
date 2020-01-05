# intro.py
# Your name here: Matt Wong
# Date:  4 September 2014

import random   # This imports a package that allows us to get random numbers

def fourfours():
    """ Give an expression using exactly four 4's that evaluates
        to the given number.  We've given an example for 0.  Note the comma
        between the closed quotation mark and the expression! """
    print "0 is: ", 4 + 4 - 4 - 4 # Here's an example for 0
    print "1 is: ", (4 + 4 - 4)/4
    print "2 is: ", (4/4)+(4/4)
    print "3 is: ", (4+4+4)/4
    print "4 is: ", (4 - 4)*4 + 4
    print "5 is: ", (4*4 + 4)/4
    # Feel free to come back and add more lines later.  But for now,
    # move on to the next part of this problem. :^)

def slicing():
    """ Give an expression using the defined myString and string
        slicing notation to construct the desired string.  Note the comma
        between the closed quotation mark and the expression!"""
    myString = 'Pseudopseudohypoparathyroidism' 
    print "Pseudohypo is: ", myString[0:6] + myString[12:16] # Here's an example
    print "myString but with the first three and last three symbols removed is:", 
    print myString[3:27]
    print "the reversal of mystring but skipping every second letter is: " 
    print myString[29:0:-2]

def lists1():
    """ Give an expression using the defined myList and list slicing to
        construct the desired lists.  Note the comma between the closed quotation
        mark and the expression! """
    myList = [1, 2, 3, ['hello', 'there'], 42, 47]
    print "the number 2 is: ", myList[1]   # Here's an example
    print "the list [2] is: ", myList[1:2] # Another example
    print "the list [1, 2, 3, 42, 47] is: ", myList[0:3] + myList[4:]
    print "the list ['hello', 'there'] is: ", myList[3]

def lists2():
    """ Give an expression using the two defined lists, list1 and list2, and list
        operations to construct the desired lists. """
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    print "[1, 2, 3, 4, 5, 6] is: ", list1 + list2 # An example
    print "[1, 2, 3, [4, 5, 6]] is: ", list1+[list2]
    print "[1, 2, [4, 5, 6], 3, 4] is: ", [list1[0],list1[1],list2,list1[2],list2[0]]

def usingRange():
    """ Give an expression using the built-in range function and other list operations
        to construct the desired lists. """
    print "the list of numbers from 10 to 20 is:", range(10, 21) # an example
    print "the list of numbers from 10 to 40, excluding 30 through 35 is: ", range(10, 30), range(36, 41)
    print "the list of numbers from 1 to 100 that do not contain the digit 9 is: ", 
    list = range(1,9) + range(10,19) + range(20,29) + range(30,39) + range(40,49) + range(50,59) + range(60,69) + range(70,79) + range(80,89),100
    print list
    

        
        

def guess():
    """ Play this game!  Then, make some change to it of your choosing.  Explain
        the change that you made in this docstring. I changed the high low messages to either 5 digits away from the answer or not five digits away from the answer.  """
    secret = random.randint(0, 100)  # Python chooses a random number between 0 and 100
    while True:
        guess = input("Guess the number:")
        if guess == secret:
            print "You got it!"
            return # return causes function to stop!
        elif guess == secret + 5:
            print "Your guess is 5 digits away from the answer"
        else:
            print "Your guess is not five digits away from the answer"
            
    


    


    
