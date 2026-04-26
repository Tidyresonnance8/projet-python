def merge(first_list, second_list):
    i, j = 0, 0
    merget = []

    while i < len(first_list) and j < len(second_list):
        name1, time1 = first_list[i]
        name2, time2 = second_list[j]

        if time1 < time2:
            merget.append(first_list[i])
            i += 1
        else:
            merget.append(second_list[j])
            j += 1
    
    while i < len(first_list):
        merget.append(first_list[i])
        i += 1
    
    while j < len(second_list):
        merget.append(second_list[j])
        j += 1
    
    return merget
