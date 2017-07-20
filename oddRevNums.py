def reversibleNumber(x):
    counter = 0
    strNum = str(x)
    numList = list(strNum)
    numListRev = reversed(numList)
    revStr = "".join(numListRev)
    revInt = int(revStr)
    test = True
    sum = x + revInt
    print(sum)
    for b in str(sum):
        if int(b)%2 != 0:
            test = True
        else:
            counter += 1
            print(x,"This number IS NOT reversible")
            test = False
            break
    if test == True:
        print("Reversible")


num = int(input("What is your num?\n"))
reversibleNumber(num)