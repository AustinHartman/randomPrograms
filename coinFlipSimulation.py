def coinFlip():
    import random
    heads = 0
    tails = 0
    flipCount = input("How many times do you want to flip the coin?\n")

    for i in range(int(flipCount)):
        number = random.choice([0, 1])
        if number == 0:
            heads += 1
        else:
            tails += 1

    print("Heads: ", heads)
    print("Tails: ", tails)

coinFlip()


