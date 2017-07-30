#COMINATORIC SELECTIONS

import math


def combinations(n, r):
    return int(math.factorial(n) / (math.factorial(r)*math.factorial(n-r)))

for r in range(23):
    print(combinations(23, r))
count = 0
for n in range(101):
    for r in range(n):
        if combinations(n, r) > 1000000:
            count += n - 2 * r + 1
            break
print(count)

