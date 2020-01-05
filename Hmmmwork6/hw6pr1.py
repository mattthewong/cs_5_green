
# hw6pr1.py - Hmmm!
#
# problem number: Lab!
#
# name: Matt Wong
# date: 10/24
#


# you'll write unique later in the lab...
def unique(L):
    '''Your function unique(L) will take a list as its only input and should
    return True if that list has only unique elements (no elements repeated)
    and False otherwise.'''
    if L == []:
        return True 
    else:
        i = L[0]
        if i in L[1:]:
            return False
        else:
            L = L[1:]
            return unique(L)
NUMBERS = '''18
81
4
87
30
33
96
19
2
45
48
11
34
17
60
63
26
49
32
75
78
41
64
47
90
93
56
79
62
5
8
71
94
77
20
23
86
9
92
35
38
1
24
7
50
53
16
39
22
65
68
31
54
37
80
83
46
69
52
95
98
61
84
67
10
13
76
99
82
25
28
91
14
97
40
43
6
29
12
55
58
21
44
27
70
73
36
59
42
85
88
51
74
57
0
3
66
89
72
15
'''
def test(S):
    """ test accepts a (triple-quoted) string, S,
        containing one number per line. Then, test
        returns True if those numbers are all unique
        (or if S is empty); otherwise it returns False
    """
    ListOfStrings = S.strip().split()
    # print "ListOfStrings is", ListOfStrings
    ListOfIntegers = [int(s) for s in ListOfStrings]
    # print "ListOfIntegers is", ListOfIntegers
    return unique(ListOfIntegers)            
            
# Example1 is an example program that
#   1) asks the user for two inputs
#   2) computes the product of the inputs
#   3) prints out the result (with write)
#   4) stops

Example1 = """
00 read r1          # get # from user to r1
01 read r2          # ditto, for r2
02 mul r3 r1 r2     # r3 = r1 * r2
03 write r3         # print what's in r3
04 halt             # stop.
"""


# Problem1 is an example program that
#   1) asks the user for an input
#   2) counts up from that input
#   3) keeps going and going...

# Lab task #1: Change Problem1 to "the cubic countdown"

Problem1 = """
00 read r1        # get number from user for input
01 mul r2 r1 r1   # gets the square of r1 and stores that value in r2
02 mul r3 r2 r1   # multiplies r2 by r1 and stores that value in r3
03 write r3       # prints the value of r3
04 addn r3 -1     # counts down from r3 value until the value in r3 < 0
05 write r3       # otherwise, the program stops.
06 jgtzn r3 04
07 halt
"""


# Lab task #2: Write a random-number generator, named Random, here:
#   (Note: this is starter code for the inputs...)

Random = """
00 read r1      # input a
01 read r2      # input c
02 read r3      # input m
03 read r4      # input X_0
04 read r5      # input N
05 mul r6 r4 r1 # multiplies a by Xn and stores that in r6
06 add r7 r6 r2 # adds r6 and r2, storing the value in r7
07 mod r8 r7 r3 # divides r7 by r3 and stores value in r8.
08 write r8     # prints contents of register r8
09 copy r4 r8   # copies the value of r8 into r4
10 addn r5 -1   # decriments r5 by -1
11 jgtzn r5 05  # if r5 > 0, then jump to line 5 and go through program.
12 halt         # otherwise, halt. 
"""



# This function runs the Hmmm program specified
#
def run():
    """ runs a Hmmm program... """
    import hmmmAssembler ; reload(hmmmAssembler)  # import helpers
    hmmmAssembler.main(Random)     # this runs the code!
#   change this name   ^^^^^^^^  to run a different function!

#Xn+1 = (a Xn + c) % m
#m = 100
#a = 21
#c = 3






