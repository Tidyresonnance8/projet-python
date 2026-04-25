def maximum_index(lst):
    if len(lst) == 0:
        return None

    e = 0
    for i in range(1,len(lst)):
        if lst[i] > lst[e]:
            e = i
    return e
print(maximum_index([1,3,4,4,5,3]))
print(maximum_index([12,5,14,5,5,12]))
