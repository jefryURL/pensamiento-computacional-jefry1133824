print("ejercicio1")

n1 = int(input("ingresar el primer numero: "))
N2 = int(input("ingresar el primer numero: "))

divisionReal = n1/ N2
divEntera = n1//N2
divModular = n1 % N2

print(n1,"/",N2,"=",divisionReal)
print(n1,"/",N2,"=",divEntera)
print(n1,"/",N2,"=",divModular)

Suma = n1 + N2
Multiplicación = n1 * N2
resta = n1 - N2 

print(n1,"*",N2, "=",Multiplicación)
print(n1,"+",N2, "=",Suma)
print(n1,"-",N2, "=",resta)

print("ejercicio 2: operaciones booleanas")

igualdad = n1 == N2
diferencia = n1 != N2

print(n1, "==", N2, "=", igualdad)
print(n1, "!=", N2, "=", diferencia)

mayor = n1 > N2 
menor = n1 < N2

print(n1,">",N2, "=", mayor)
print(n1,"<",N2, "=", menor)

print("ejercicio 3: jerarquia de operaciones")
a=int(input("ingrese el primer numero: "))
b=int(input("ingrese el primer numero: "))
c=int(input("ingrese el primer numero: "))

print("i.", a*b+c)
print("ii.", a*(b+c))
print("iii.", a/(b+c))
print("iv: ", (3*a+2*b)/pow (c, 2))


print("actividad: ejercicio 1: ")

metros1 = int(input("ingrese metros: "))
km = metros1/ 1000 
print("km:", km)






print("actividad: ejercicio 2: ")

metros2 = int(input("ingrese metros: "))
yardas = metros2 // 0.9144
modyardas = metros2 % 0.9144
pies = modyardas // 0.3333333
pulgadas = metros2*39.37
print ("yardas: ",yardas, "pies: ", pies)

print("yardas: ", yardas, "pies: ", pies, "pulgadas: ", pulgadas)


