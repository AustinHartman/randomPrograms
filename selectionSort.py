import timeit

ls = [3, 4, 8, 2, 9, 6, 5, 3, 2]


"""def minimum(l):
    low = l[0]
    for n in l:
        if n < low:
            low = n
    return low

while len(ls) > 0:
    print(minimum(ls))
    list_min_pos = minimum(ls)
    ls.remove(list_min_pos)
    ls_sorted.append(list_min_pos)
print(ls_sorted)"""

def selection_sort(ls):
    for l in range(len(ls)-1, 0, -1):
        max_pos = 0
        for loc in range(1, l+1):
            if ls[loc] > ls[max_pos]:
                max_pos = loc

        temp = ls[l]
        ls[l] = ls[max_pos]
        ls[max_pos] = temp
    return ls



























def sel_sort(ls):
    for l in range(len(ls)-1, 0, -1):
        max_pos = 0
        for loc in range(1, l+1):
            if ls[loc] > ls[max_pos]:
                max_pos = loc

        temp = ls[l]
        ls[l] = ls[max_pos]
        ls[max_pos] = temp
        print(ls)
    return ls

print(sel_sort([9,8,7,6,5,4,5,4,5]))
