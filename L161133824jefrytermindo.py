print("actividad 1: ")

import random

print("Semana No. 16: Ejercicio 1")

def programa1():
    arreglo = [random.randint(0, 100) for _ in range(10)]
    print(f"Números ingresados: {arreglo}")

    promedio = sum(arreglo) / len(arreglo)
    print(f"Promedio del arreglo: {promedio}")
    print(f"Longitud del arreglo: {len(arreglo)}")

    suma_pares = sum(arreglo[i] for i in range(len(arreglo)) if i % 2 == 0)
    print(f"Suma de posiciones pares: {suma_pares}")
    suma_impares = sum(arreglo[i] for i in range(len(arreglo)) if i % 2 != 0)
    print(f"Suma de posiciones impares: {suma_impares}")
    
    pass









print("actividad 2: ")
import random

# 1. Mostrar el título del ejercicio
print("Semana No. 12: Ejercicio 2")

# 2. Pedir al usuario que ingrese las dimensiones de la matriz (número de filas y número de columnas)
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

# 3. Crear una matriz con números generados aleatoriamente, los números deben estar en el rango entre 0 y 1000
matriz = [[random.randint(0, 1000) for _ in range(columnas)] for _ in range(filas)]

# 4. Calcular estadísticas
pares = 0
impares = 0
max_num = float('-inf')
min_num = float('inf')

for fila in matriz:
    for num in fila:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

# 4. Imprimir estadísticas
print("Matriz:")
for fila in matriz:
    print(fila)

print("Estadísticas:")
print(f"  a. Números pares: {pares}")
print(f"  b. Números impares: {impares}")
print(f"  c. Número máximo: {max_num}")
print(f"  d. Número mínimo: {min_num}")