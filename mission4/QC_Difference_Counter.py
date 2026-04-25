def diff_count(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return 1
    else:
        unique = []
        for element in lst:
            if element not in unique:
                unique.append(element)
        return len(unique)

print(diff_count([3,2,3]))
print(diff_count([1]))
print(diff_count([]))
