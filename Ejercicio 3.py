"""
Calculadora
"""
a = int(input("ingresa un numero"))
b = int(input("ingresa otro numero"))

print("operaciones disponibles")
print("1.- Suma")
print("2.- Resta")
print("3.- Multpiplicacion ")
print("4.- Division")
operacion = int(input("Indica la operacion que quieres realizar :"))

if  operacion == 1:
    resultado = a + b
elif operacion == 2:
    resultado = a - b
elif operacion == 3:
    resultado = a * b
elif operacion == 4:
    if  b == 0:
        resultado = print("no es posible divir entre 0")
    else:
        resultado = a / b

print("El resultado es",resultado)
