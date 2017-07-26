running = True
dec = ''
counter = 1
while running == True:
    dec += str(counter)
    counter += 1
    if len(dec) > 1000000:
        running = False

answer = 1
for i in range(7):
    answer *= int(dec[(10 ** i) - 1])
print(10**7)
print(answer)