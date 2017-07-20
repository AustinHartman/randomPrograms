def findFactors(x):
    div = 1
    facs = []
    while(div<=x):
        if(x%div==0):
            facs.insert(0, div)
            facs.insert(0, int(x/div))
            div = div + 1
        else:
            div = div + 1
    factors = len(facs)
    print("There are",int(factors/2),"factors")
    print("This is every factor shown twice:",facs)

number = int(input("What number do you want the factors of?\n"))
findFactors(number)




