a = int(input("entrer la variable: "))
b = int(input("entrer la variable: "))
if b == 0:
    rest = -1
    print(rest)
else:
    rest = a
    while rest >= b:
        rest -= b
    print(rest)