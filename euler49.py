import itertools

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


for i in range(1001, 5000, 2):
    if not is_prime(i):
        continue
    s = str(i)
    perm_obj = itertools.permutations(s)
    perms = []
    for perm in perm_obj:
        if len(str(int("".join(perm)))) == 4 and int("".join(perm)) not in perms:
            perms.append(int("".join(perm)))
    diff = 0
    for perm in perms[1:]:
        if not is_prime(perm):
            continue
        diff = perm - perms[0]
        if diff + perm in perms and is_prime(diff+perm):
            print(str(perms[0]) + str(perm) + str(diff + perm))







