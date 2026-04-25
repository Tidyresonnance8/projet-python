def ajoute(l,v):
    if v not in l:
        l.append(v)

l = [3, 1, 5, 4]
ajoute(l, 4)
ajoute(l, 6)
ajoute(l, 7)
ajoute(l, 6)
print(l)