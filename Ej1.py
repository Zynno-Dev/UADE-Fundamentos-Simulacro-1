a=int(input("Ingrese el legajo del alumno: "))
b=int(input("Ingrese la nota del alumno: "))
while b<0 or b>10:
    b=int(input("Nota erronea, vuelva a intentar: "))
c,d,e,f,g,h=0,0,0,0,0,0

while a!=-1:
    if b>=7:
        c+=1
    elif b>=4:
        d+=1
    else:
        e+=1
    f+=1
    if b>g:
        g=b
        h=a
    a=int(input("Ingrese el legajo del alumno: "))
    if (a!=-1):
        b=int(input("Ingrese la nota del alumno: "))
        while b<0 or b>10:
            b=int(input("Nota erronea, vuelva a intentar: "))
e=(e*100)/f

print("")
print(" PROGRAMA FINALIZADO")
print("")
print("------Resultados------")
print("Alumnos con nota igual o mayor a 7:",c)
print("Alumnos con nota entre 4 y 6:",d)
print("Alumnos aplazados:",e ,"%")
print("Alumnos totales:",f)
print("")
print("El alumno con mayor nota es:",h,"con una nota de:",g)