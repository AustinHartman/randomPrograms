def isPrime(x):
    var = 2
    while(var <= x/2):
        if(x%var == 0):
            print('no')
            var = x+1
        else:
            var += 1
    if(var != x+1):
        print('yes')

number = int(input("What is your number?\n"))
isPrime(number)