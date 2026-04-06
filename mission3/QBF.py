def chiffres_pairs(n):
    if n == 0:
        return False
    count = 0
    while n > 0:
        n//=10
        count += 1
    return count%2 == 0
n = 0
while True:
    n = int(input("Entrez un nombre (-1 pour arrêter) : "))
    if n < 0:
        break
    if chiffres_pairs(n):
        print(n, " a un nombre pair de chiffres dans sa représentation décimale")
    else:
        print(n, " a un nombre impair de chiffres dans sa représentation décimale")


