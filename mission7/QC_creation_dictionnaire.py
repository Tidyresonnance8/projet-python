def create_dict(l):
    dict = {}

    for x, y in l:
        if x in dict:
            dict[x].append(y)
        else:
            dict[x] = [y]
    
    return dict