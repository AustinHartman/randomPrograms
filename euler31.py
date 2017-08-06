import itertools

perm_list = []
perm_obj = itertools.permutations('01234567')
for perm in perm_obj:
    perm_list.append("".join(perm))
vals = [1, 2, 5, 10, 20, 50, 100, 200]
total = 200
print(perm_list)