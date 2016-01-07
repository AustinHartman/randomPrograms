def coinFlip():
    import random
    heads = 0
    tails = 0
    n = input("How many times do you want to flip the coin?\n")

    for x in range(int(n)):
        number = random.choice([0,1])
        if number == 0:
            heads+=1
        else:
            tails+=1

    print("Heads: ", heads)
    print("Tails: ", tails)

coinFlip()


