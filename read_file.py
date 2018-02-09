file = open('test.txt', 'r')
line = file.readline()
print(line)
line = int(line)
if line == 1:
    print("success")
