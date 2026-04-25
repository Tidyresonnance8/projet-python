def primes(max):
    liste = []

    if max <= 0:
        return []
    
    for i in range(2,max+1):
        prime = True
        for j in range(2,i):
            if i%j == 0 :
                prime = False
                break
        if prime:
            liste.append(i)
        
    return liste

print(primes(13))