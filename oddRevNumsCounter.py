def reversibleNumber(x):
    reversibleNumsList = []
    num = 1
    while num < x:
        rev = int("".join(reversed(list(str(num)))))
        sum = num + rev
        for b in str(sum):
            if int(b)%2 == 1:
                test = True
            else:
                test = False
                break
        if test == True and num%10 != 0:
            print(num,"Reversible")
            reversibleNumsList.append()
        num += 1
    print(len(reversibleNumsList))

num = int(input("What is your num?\n"))
reversibleNumber(num)
