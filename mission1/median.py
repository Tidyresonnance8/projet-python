a = int(input("variable à évaluer :"))
b = int(input("variable à évaluer :"))
c = int(input("variable à évaluer :"))
if a<=b<=c or c<=b<=a:
    median = b
if a<=c<=b or b<=c<=a:
    median = c
else:
    median = a
print(f'la mediane est : {median}')