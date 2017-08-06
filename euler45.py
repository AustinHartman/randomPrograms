def t(n):
    return n * (n + 1) / 2


def p(n):
    return n * (3 * n - 1) / 2


def h(n):
    return n * (2 * n - 1)

for t in range(286, 1000000):
    for p in range(166, 1000000):
        for h in range(144, 1000000):
            if t(t) == h(h) and t(t) == p(p):
                print(t(t))

