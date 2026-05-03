def equal(l, d):
    n = len(l)
    for i in range(n):
        for j in range(n):
            if l[i][j] != d.get((i,j),0):
                return False
    return True