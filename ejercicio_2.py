print("lista de numeros\n")
pares =0
impares=0
n=int(input("digite los numeros : "))
for i in range(8):
    n=int(input("digite los numeros : "))
    if n%2==0:
        pares=pares+1
    else:
        impares=impares+1
    
print(pares)
print(impares)                 