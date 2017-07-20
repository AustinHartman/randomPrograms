def bubble_sort(list):
    list = [int(i) for i in list]
    length = len(list)
    for i in range(0, length):
        for j in range(0, length-1):
            if list[j] > list[j+1]:
                store = list[j]
                list[j] = list[j+1]
                list[j+1] = store
    print(list)

def bs(list):
    for key in range(len(list)):
        print(key)
        for i in range(len(list)-key-1):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
    return list



print(bs([1,6,3,8,5,9,0,1,5,8]))

#BS function works
#Doesnt work... two for statments though
