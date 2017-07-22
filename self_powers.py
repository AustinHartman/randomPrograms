total = 0
for i in range(1001):
    print(i)
    total += i**i
    if len(str(total)) > 10:
        total = int(str(total)[-10:])

print(total)