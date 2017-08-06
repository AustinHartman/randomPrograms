import time

#Solution number 1
#Time = 0.732 seconds

"""nums = []

for a in range(2, 101):
    for b in range(2, 101):
        if a ** b not in nums:
            nums.append(a ** b)

print(len(nums))"""

#Solution number 2
#Time = 0.0136 seconds

"""L = 101
r = range(2, L)
print(len({a**b for a in r for b in r}))"""

#Solution number 3
#Time = 0.01337 seconds

L = set()
for a in range(2, 101):
    for b in range(2, 101):
        L.add(a**b)
print(len(L))


