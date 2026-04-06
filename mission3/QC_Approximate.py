def factorial(n):
    """
    @pre:    n est un entier tel que n >= 0
    @post:   retourne n!
    """
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1,n+1):
            fact *= i
        return fact

def approx_sin(n):
    """
    @pre:   n est un entier tel que n >= 0
    @post:  retourne une estimation de sin 1 en sommant
            les n + 1 premiers termes de la série
    """
    sin1 = 0
    for i in range(n+1):
        term = ((-1)**i)/factorial(2*i + 1)
        sin1 += term
    return sin1

print(approx_sin(0))
print(approx_sin(1))
print(approx_sin(2))
print(approx_sin(3))
print(approx_sin(1000))