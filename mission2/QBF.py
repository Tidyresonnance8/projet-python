n = int(input("entre la valeur :"))
for i in range(1, n+1):
    count = 0
    for j in range(1,i):
        if i%j == 0:
            count += 1
    print(i,":",count)
