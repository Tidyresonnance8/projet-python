def carre(n):
    matrix = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(i*n+j)
        matrix.append(row)
    return matrix

print(carre(4))
print(carre(8))
print(carre(12))