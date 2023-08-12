"""
Arreglo invertido
"""
n = int(input("Escribe el número de elementos que tendrá tu arreglo: "))
Arreglo = []

for i in range(n):
    posicion = input(f"Ingresa el número de la posición {i + 1}: ")
    Arreglo.append(posicion)

print("Arreglo original:")
for posicion in Arreglo:
    print(posicion)

x = n - 1
mitad = n // 2  # Usar la división entera //

for i in range(mitad):
    intercambio = Arreglo[i]
    Arreglo[i] = Arreglo[x]
    Arreglo[x] = intercambio
    x = x - 1

print("Arreglo invertido:")

for posicion in Arreglo:
print(posicion)
