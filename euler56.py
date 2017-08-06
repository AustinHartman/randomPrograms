highest = 0
digit_sum = 0

for a in range(1, 100):
    print(a)
    for b in range(1, 100):
        product_str = str(a ** b)
        digit_sum = 0
        for l in product_str:
            digit_sum += int(l)
        if digit_sum > highest:
            highest = digit_sum
print(highest)
