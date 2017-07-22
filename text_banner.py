import sys
import os

ls=[" #  # #### #    #    ####", "#  # #    #    #    #  #",
    "#### #### #    #    #  #", "#  # #    #    #    #  #",
    "#  # #### #### #### ####"]
space = " "

for i in range(5):
    d = space*i
    sys.stdout.write(d + ls[0])
    sys.stdout.write("\n")
    sys.stdout.write(d + ls[1])
    sys.stdout.write("\n")
    sys.stdout.write(d + ls[2])
    sys.stdout.write("\n")
    sys.stdout.write(d + ls[3])
    sys.stdout.write("\n")
    sys.stdout.write(d + ls[4])
    sys.stdout.flush()
    