# hw6 problem 4
#
# date: 10/28/14
#
# Hmmm...
#
#

# For cs5gold, you'll write a recursive power program
# For cs5black, it's the Ex. Cr. "Ackermann" program

# Either way, be sure to call it Problem4 !

# This is a placeholder by that name whose code you'll replace:

Problem4 = """
00 read r2          # read input and put into r2. 
01 read r1          # read input and put into r1.       
02 setn r15 42      # 42 is the beginning of the stack, put that address in r15.
03 call r14 5       # begin function at line 5, but first put next address (03) into r14.
04 jumpn 21         # Let's defer final output to line 21...
05 jnez r1 8        # BEGINNING OF FACTORIAL FUNCTION!  Check if r1 is non-zero.  If it is go to line 8 and do the real recursion!
06 setn r13 1       # otherwise, we are at the base case:  load 1 into r13 and...
07 jumpr r14        # ... return to where we were called from (address is in r14)
08 storer r1 r15    # place r1 onto the stack
09 addn r15 1       # increment stack pointer
10 storer r14 r15   # place r14 onto the stack
11 addn r15 1       # increment stack pointer
12 addn r1 -1       # change r1 to r1-1 in preparation for recursive call
13 call r14 5       # recursive call to factorial, which begins at line 5 - but first store next memory address in r14
14 addn r15 -1      # we're back from the recursive call!  Restore goods off the stack.
15 loadr r14 r15    # restoring r14 (return address) from stack
16 addn r15 -1      # decrement stack pointer
17 loadr r1 r15     # restoring r1 from stack
18 mul r13 r13 r2   # now for the multiplication 
19 jumpr r14        # and return!
20 nop              # nothing
21 write r13        # write the final output
22 halt
"""

# This function runs the Hmmm program specified
#
def run():
    """ runs a Hmmm program... """
    import hmmmAssembler ; reload(hmmmAssembler)  # import helpers
    hmmmAssembler.main(Problem4)     # this runs the code!
#   change this name   ^^^^^^^^  to run a different function!


