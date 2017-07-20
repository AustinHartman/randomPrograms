def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i > 0:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    print (factors)

number = int(input("What is your number?\n"))
prime_factors(number)
