x = int(input("entrer l'entier :"))
if x == 0:
    result = 1
    print(result)
else:
    result = 1
    for i in range(1,x+1):
        result *= i
    print(result)