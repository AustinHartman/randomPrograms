import math

nums = []

for n in range(3, 2540160):
    str_n = str(n)
    fact_sum = 0
    for i in str_n:
        fact_sum += math.factorial(int(i))
    if fact_sum == n:
        nums.append(n)
print(sum(nums))