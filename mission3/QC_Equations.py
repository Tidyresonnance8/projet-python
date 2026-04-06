import math as m

def rho(a,b,c):
    return b**2 -4*a*c

def n_solutions(a,b,c):
    delta = rho(a,b,c)
    if delta < 0:
        return 0
    elif delta == 0:
        return 1
    elif delta >= 0:
        return 2

def solution(a,b,c):
    discriminant = m.sqrt(rho(a,b,c))
    if discriminant == 0:
        return -b/(2*a)
    elif discriminant > 0:
        x1 = (-b - discriminant)/(2*a)  
        x2 = (-b + discriminant)/(2*a)
        return min(x1,x2)

print(rho(1,2,1))
print(n_solutions(1,2,1))
print(solution(1,2,1))  