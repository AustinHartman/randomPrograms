def is_prime(x):
    if x % 2 == 0:
        return False
    d = 3
    upper = int(abs(x) ** 0.5 + 1)
    while d <= upper:
        if x % d == 0:
            return False
        d += 2
    return True


def quad_consec_primes(a, b):
    n = 0
    length = 1
    n += 1
    while is_prime(n**2 + a*n + b):
        length += 1
        n += 1
    return length

print(quad_consec_primes(-79, 1601))


a = 1
b = 1
longest = 1
product = 0
for a in range(1000, -1000, -1):
    for b in range(1000, -1000, -1):
        current = quad_consec_primes(a, b)
        if current > longest:
            longest = current
            product = a*b
            print(a, b)


print(longest, product)
