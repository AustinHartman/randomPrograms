import math
import time

def prime_list(lower, upper):
    p_ls = [2, 3, 5, 7]
    for n in range(lower, upper, 2):
        p = True
        for d in range(3, int(math.sqrt(n)) + 1):
            if n % d == 0:
                p = False
                break
        if p:
            p_ls.append(n)
    return p_ls


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


def prime_generator():
    num = 5
    while True:
        prime = True
        for d in range(3, int(num ** 0.5 + 1)):
            if num % d == 0:
                prime = False
                break
        if prime:
            yield num
        num += 2

start = time.time()

gen = prime_generator()
primes = [2, 3]
n = 5
longest = 0
total = 0
length = 0
prime = 0
keep_checking_num = True
l = 0

while n < 1000001:
    if not is_prime(n):
        n += 2
        continue
    while primes[-1] < n:
        primes.append(gen.__next__())
    keep_checking_num = True
    l = 0

    while keep_checking_num:
        l += 1
        length = 0
        total = 0
        for i in range(l, len(primes)):
            total += primes[i]
            length += 1
            if total > n:
                break
            if total == n:
                if length > longest:
                    longest = length
                    prime = n
                    print(prime)
                keep_checking_num = False
    n += 2
print(longest, prime)

print(time.time()-start)

for i in range(primes):
    for n in range(primes):
        if sum(primes)





