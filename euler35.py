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


def is_prime(x):
    if x % 2 == 0:
        return False
    d = 3
    upper = int(x ** 0.5 + 1)
    while d <= upper:
        if x % d == 0:
            return False
        d += 2
    return True


thr_dig = prime_list(101, 1001)
fou_dig = prime_list(1001, 10001)
fiv_dig = prime_list(10001, 100001)
six_dig = prime_list(100001, 1000001)


def str_rotate(s):
    rotations = []
    for rotation in range(len(s)):
        s = s[1:] + s[0]
        rotations.append(s)

    return rotations


def find_circular_primes(p_ls):
    circular = True
    circ_nums = []
    for prime in p_ls:
        for check in str_rotate(str(prime)):
            if not is_prime(int(check)):
                circular = False
                break
        if circular:
            circ_nums.append(prime)
        circular = True
    return circ_nums


len3_5 = len(find_circular_primes(thr_dig)) + len(find_circular_primes(fou_dig)) + len(find_circular_primes(fiv_dig)) \
         + len(find_circular_primes(six_dig))
print(len3_5 + 13)
