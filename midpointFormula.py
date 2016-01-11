def midpointFormula():
    print("This program will calculate the midpoint of the given points\n")
    pt1 = [int(input("What is the 1st x coordinate?\n")), int(input("What is the 1st y coordinate?\n"))]
    pt2 = [int(input("What is the 2nd x coordinate?\n")), int(input("What is the 2nd y coordinate?\n"))]
    midpoint = [(pt1[0] + pt2[0]) / 2, (pt1[1] + pt2[1]) / 2]
    print(midpoint)
    rerun = input("Would you like to run it again? y or n\n")
    if rerun == "y":
        midpointFormula()
    else:
        exit(0)
midpointFormula()
