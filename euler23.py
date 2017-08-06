import time


def divisor_list(num):
    divs = set()
    upper_bound = int(num ** 0.5) + 1
    for i in range(2, upper_bound):
        if num % i == 0:
            divs.add(i)
            divs.add(num // i)
    return divs



def abundant(num):
    if sum(divisor_list(num)) > num:
        return True
    return False


abundant_nums = []
sum_of_two = False
non_abundants_sum = 0
new = []
for i in range(24, 28124):
    if abundant(i):
        abundant_nums.append(i)
        continue
    sum_of_two = False
print(abundant_nums)
for num in abundant_nums:
    if num % 2 != 0:
        new.append(num)
print(new)
