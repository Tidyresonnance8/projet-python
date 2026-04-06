s0 = int(input("Entrer l'entier de départ :"))
s = s0
while s > 1:
    print(s)
    if s % 2 == 0:
        s//=2
    else:
        s = 3*s + 1
print(1)