def to_bin(num):
    power = 0
    bin_str = ''
    while 2 ** power < num:
        power += 1
    while num != 0:
        if 2 ** power <= num:
            num -= 2 ** power
            bin_str += '1'
        else:
            bin_str += '0'
        power -= 1
    return bin_str

print(to_bin(1234))


def to_bin_2(num):
    bin_num = ''
    while num != 0:
        bin_num += str(num % 2)
        num = num // 2
    return bin_num[::-1]

print(to_bin_2(1234))
