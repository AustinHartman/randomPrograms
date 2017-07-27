def pent_gen(n):
    return int(n * (3 * n -1) / 2)



def pe44():
    n = 4
    pent_ls = [1, 5, 12]
    l = 0
    peak_diff = 0
    while True:
        while pent_ls[-1] < pent_ls[l] * 2:
            pent_ls.append(pent_gen(n))
            n += 1
        for p in pent_ls[:l]:
            if pent_ls[l] - p < peak_diff:
                break
            else:
                peak_diff = pent_ls[l] - p
            if pent_ls[l] - p in pent_ls:
                if p + pent_ls[l] in pent_ls:
                    return pent_ls[l] - p
        l += 1


print(pe44())

