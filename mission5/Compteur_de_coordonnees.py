def count(coordonnees, i, j):
    compteur = 0
    for element in coordonnees:
        if element == (i,j):
            compteur += 1
    return compteur

coordonnees = [(0, 1), (2, 3), (0, 1), (4, 5), (1, 2), (0, 1), (1, 1), (0, 2), (1, 1)]
print(count(coordonnees, 1, 1))