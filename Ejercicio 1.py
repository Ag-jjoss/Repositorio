"""
Suma de pares
"""
n = int(input("Escribe un número entero: "))
m = int(input("Escribe un número entero mayor a n: "))

i = n

suma = 0
while i <= m:
  if i % 2 == 0:
    suma += i
  i += 1
print("La suma de los números pares entre ",n, "y", m, "es" ,suma)
