import time

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def fib(n):
    a, b = 1, 1
    for i in range(n-2):
        print(i)
        tmp = b
        b = a + b
        a = tmp
    return b

a = 0
b = 1

def fibG():
    global a, b
    while True:
        tmp = b
        b = a + b
        a = tmp
        yield a



#num = 354224848179261915075
#index = 100
#while len(str(num)) <= 500:
 #   num = int(num * 1.6180339887498948482)
 #   index += 1
#print(num, index)