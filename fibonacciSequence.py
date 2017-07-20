def fibonacciSequence():
    limit = int(input("How far to go?\n"))
    sequenceList = [0]
    while len(sequenceList) < limit:
        if len(sequenceList) == 1:
            sequenceList.append(1)
        else:
            sequenceList.append(sequenceList[-1] + sequenceList[-2])
    print("\nHere are", limit, "digits of Fibonacci:", sequenceList)

fibonacciSequence()
