def create_dict_max(l):
    dict = {}
    for x, y in l:
        if x in dict:
            dict[x] = max(dict[x],y)
        else:
            dict[x] = y
    return dict
