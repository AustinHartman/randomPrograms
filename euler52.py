import time

def mult_same_digits(num, mult):
    num_mult = num * mult
    num = str(num)
    num_mult = str(num_mult)

    nums_ls = []
    nums_mult_ls = []

    for d in num:
        nums_ls.append(d)
    for d in num_mult:
        nums_mult_ls.append(d)

    if len(num_mult) != len(num):
        return False
    for l in nums_ls:
        if l not in nums_mult_ls:
            return False
        nums_mult_ls.remove(l)
    return True


# Runs in 0.534 seconds
lowest_found = False
place = 1
while not lowest_found:
    for i in range(6, 0, -1):
        if not mult_same_digits(place, i):
            place += 1
            break
        if i == 1:
            print(place)
            lowest_found = True