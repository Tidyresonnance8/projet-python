n = int(input("entrer la valeur: "))
pi = 0
for i in range(n+1):
    term = ((-1)**i)/(2*i + 1)
    pi += 4*term
print(pi)