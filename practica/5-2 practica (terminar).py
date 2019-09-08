#Ejercicio 5.2. Escribir una función que reciba un número entero k e imprima su descomposición
#en factores primos.

def todosLosPrimos(n):
    """Dado un número n, devuelve todos los números primos desde 2 hasta n."""
    

def descomponerFactoresAPrimos(k):
    """Recibe un número y devuelve su descomposición en factores primos."""
    for n in range(2, k + 1):
        while k % n == 0:
            print(n)
            


entrada = int(input('Ingrese un número a descomponer: '))
descomponerFactoresAPrimos(entrada)