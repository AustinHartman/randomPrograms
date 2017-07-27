import math
import itertools


def prime_list(lower, upper):
    primes = []
    for n in range(lower, upper, 2):
        p = True
        for d in range(3, int(math.sqrt(n)) + 1):
            if n % d == 0:
                p = False
                break
        if p:
            primes.append(n)
    return primes

two_dig = prime_list(10, 100)
thr_dig = prime_list(101, 1000)
fou_dig = prime_list(1001, 10000)
fiv_dig = prime_list(10001, 100000)
six_dig = prime_list(100001, 1000000)



print(primes)
check = 0
p_len = 0
max = 0
for prime in primes:
    for i in primes:
        if check > prime:
            break
        if check == prime:
            if p_len > max:
                max = p_len