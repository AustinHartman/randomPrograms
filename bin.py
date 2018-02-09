def to_binary(x):
    x = str(x)
    power = 0
    total = 0
    for digit in x[::-1]:
        if digit == '1':
            total += 2**power
        power = power + 1

    return total






bin_num = 110001
result=to_binary(bin_num)
print(result)
