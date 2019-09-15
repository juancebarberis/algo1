#Ejercicio 7.5. Dada una lista de números enteros, escribir una función que:
#a) Devuelva una lista con todos los que sean primos.
#b) Devuelva la sumatoria y el promedio de los valores.
#c) Devuelva una lista con el factorial de cada uno de esos números.

def factorial(n):
    """Recibe un número <n> y devuelve su factorial."""
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def filtrarPrimos(lista):
    """"""
    primos = []
    for n in lista:
        for i in range(2,n):
            if n % i != 0:
                primos.append(n)
    return primos

def mapear(nums, funcionMapeo):
    """"""
    resultado = []

    for e in nums:
        resultado.append(funcionMapeo(e))
    return resultado



#print(filtrarPrimos([1, 2, 3, 4, 5, 6]))
print(mapear([1, 2, 3, 4, 5, 6]))
