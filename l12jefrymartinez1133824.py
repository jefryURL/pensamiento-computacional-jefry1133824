print("semana No.12: ejercicio 1")

print("a. sumatoria", "b. factorial", "c. tablas de multiplicar", "d. numero perfecto", sep = "\n")

opcion = input("ingrese la letra de su opcion")

match opcion: 
    case "a":
        n = int(input("ingrese un numero entero positivo"))

        if(n>0):
            sumatoria = 0
            i = 1
            while (i<= n):
                sumatoria = sumatoria + i
                i = i + 1
            print("sumatoria es:", sumatoria)
        else: 
            print("error: el numero debe ser mayor a 0")
    case "b": 
        print("tarea")
    case "c":
        titulocolumnas = "\t"

        for i in range (1, 11): 
            titulocolumnas = titulocolumnas + str(i) + "\t"
        print(titulocolumnas)
        for filas in range (1, 11): 
            print(filas)

    case "d":
        ent=int(input("Ingrese un número entero: "))
for i in range(2, ent+1):
    b=0
    for j in range(1, (i//2)+1):
        if((i%j)==0):
            b= b+j
    if(b==i):
        print("%s es perfecto" %i)
    else:
        print("%s no es perfecto"%i)