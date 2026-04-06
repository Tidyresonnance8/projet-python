n = int(input("entrer la valeur du nombre : "))
ln = 0
for i in range(1,n+1):
    term = ((-1)**(i+1))/i
    ln += term
print(ln)
