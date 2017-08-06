import time

def rev(n): return int(str(n)[::-1])


def is_lychrel(num):
    for i in range(1, 51):
        num += rev(num)
        if num == rev(num):
            return False
    return True

"""start = time.time()
print(sum(is_lychrel(n) for n in range(10000)))
print(time.time() - start)"""

# Reverse an int
def is_palindromic(n): return int(str(n)[::-1]) == n


def lychrel(num):
    for i in range(1, 51):
        num += int(str(num)[::-1])
        if is_palindromic(num):
            return False
    return True

start = time.time()
print(sum(lychrel(n) for n in range(10000)))
print(time.time()-start)