# hw6 problem 2
#
# name(s): Matt Wong
# date: 10/26/14
#
#
#

# For cs5gold, you'll write a power program
# For cs5black, it's a fibonacci program

# Either way, be sure to call it Problem2 !

# program should first ask for two nonnegative numbers from the user. 
#Then, the program should compute the result obtained when you raise the
#first input to the power of the second input. Finally, it should print
#that result and then halt. 
Problem2 = """
00 read r1          # get # from user to r1
01 read r2          # ditto, for r2
02 setn r3 1        # sets r3 to 1
03 jeqzn r2 07      # if r2 == 0, jump to return statement.
04 mul r3 r1 r3     # multiplies r1 by r3 and stores value in r3
05 addn r2 -1       # decriments r2 by 1
06 jumpn 03         # jumps back to test if r2 == 0
07 write r3         # print what's in r3
08 halt             # stop.
"""

# This function runs the Hmmm program specified
#
def run():
    """ runs a Hmmm program... """
    import hmmmAssembler ; reload(hmmmAssembler)  # import helpers
    hmmmAssembler.main(Problem2)     # this runs the code!
#   change this name   ^^^^^^^^  to run a different function!


