import itertools

sum_of_pandigitals = 0


def checker(num):
    if len(num) < 10:
        return False
    if num[0] == '0':
        return False
    primes = [2, 3, 5, 7, 11, 13, 17]
    for i in range(7, 0, -1):
        if int(num[i: i + 3]) % primes[i - 1] != 0:
            return False
    return True

total = 0
for set in itertools.permutations('0123456789'):
    combo = ''
    total += 1
    for s in set:
        combo += s
    if checker(combo):
        sum_of_pandigitals += int(combo)
print(sum_of_pandigitals)
print(total)



