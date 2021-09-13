a=int(input("Ingrese un numero: "))
b=0

while (a>0):
    a=a//10
    b+=1

print("El numero tiene",b,"digitos")