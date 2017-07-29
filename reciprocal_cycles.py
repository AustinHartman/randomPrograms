unit_fracs = []
for i in range(1, 1000):
    unit_fracs.append(str(1/i)[2:])


def counter(s):
    for l in s:


print(unit_fracs)
print(len(unit_fracs[0]))

for frac in unit_fracs:
    if len(frac) == 1 or len(frac) == 2:
        print(frac)
        unit_fracs.remove(frac)
for frac in unit_fracs:
    if len(frac) == 1 or len(frac) == 2:
        print(frac)
        unit_fracs.remove(frac)


print(unit_fracs)



