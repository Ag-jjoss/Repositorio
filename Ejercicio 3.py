"""
Calculadora
"""

def realizar_operacion():
    a = int(input("Ingresa un número: "))
    b = int(input("Ingresa otro número: "))
    
    print("Operaciones disponibles:")
    print("1.- Suma")
    print("2.- Resta")
    print("3.- Multiplicación")
    print("4.- División")
    
    operacion = int(input("Indica la operación que quieres realizar: "))
    
    if operacion == 1:
        resultado = a + b
    elif operacion == 2:
        resultado = a - b
    elif operacion == 3:
        resultado = a * b
    elif operacion == 4:
        if b == 0:
            resultado = "No es posible dividir entre 0"
        else:
            resultado = a / b
    else:
        resultado = "Operación no válida"
    
    print("El resultado es", resultado)


