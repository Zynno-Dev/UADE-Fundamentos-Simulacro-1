a=int(input("Ingrese un numero: "))
b=0
c=a

if a<0:
    a=a*-1

while (a>0):
    a=a//10
    b+=1

print("El numero",c,"tiene",b,"digitos")