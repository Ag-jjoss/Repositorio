"""
Suma de pares
"""
def suma_numeros_pares_entre_n_m():
    n = int(input("Escribe un número entero: "))
    m = int(input("Escribe un número entero mayor a n: "))
    
    i = n
    suma = 0
    
    while i <= m:
        if i % 2 == 0:
            suma += i
        i += 1
        
    print("La suma de los números pares entre", n, "y", m, "es", suma)



