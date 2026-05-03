def greatest_divisor(a):
    if a <= 1:
        return -1
    else:
        for i in range(a-1,0,-1):   # Je commence à compter le plus grand nombre par exemple de 10000 à 1
            if a%i == 0:
                return i

print(greatest_divisor(1))        # -1
print(greatest_divisor(15))       #  5
print(greatest_divisor(1000))     #  500
print(greatest_divisor(30000))    #  15000
