#USE LOGS

#count may need to start at ten for 1^1 2^1 etc. bc power range doesnt include 1
count = 10
base = 2
for p in range(2, 333):
    if p == 2 and len(str(base ** p)) > p:
        break
    while True:
        if len(str(base ** p)) == p:
            count += 1
        if len(str(base ** p)) > p:
            base = 2
            break
        base += 1
print(count)

