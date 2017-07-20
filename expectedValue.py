def colorTrial():
    import random
    #70, 10 each color, expected value of colors if 20 balls are chosen
    trials = 20
    colors = [10,10,10,10,10,10,10]
    while trials > 0:
        number = random.randint(0, 70)
        if int(number/10) == 0:
            colors[0] -= 1
            trials -= 1
        elif int(number/10) == 1:
            colors[1] -= 1
            trials -= 1
        elif int(number/10) == 2:
            colors[2] -= 1
            trials -= 1
        elif int(number/10) == 3:
            colors[3] -= 1
            trials -= 1
        elif int(number/10) == 4:
            colors[4] -= 1
            trials -= 1
        elif int(number/10) == 5:
            colors[5] -= 1
            trials -= 1
        elif int(number/10) == 6:
            colors[6] -= 1
            trials -= 1
    print(colors)

def combination(n,r):
    import math
    comb = math.factorial(n) / (math.factorial(r)*math.factorial(n-r))
    return comb

def expectedValue():
    seventyCtwenty = combination(70,20)
    sixtyCtwenty = combination(60, 20)
    probability = 7 * (1-sixtyCtwenty/seventyCtwenty)
    print(probability)

expectedValue()

