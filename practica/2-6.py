#Ejercicio 2.6. Escribir un programa que tome una cantidad m de valores ingresados por el usua-
#rio, a cada uno le calcule el factorial e imprima el resultado junto con el número de orden co-
#rrespondiente.

#Defino la funcion que calcula el factorial de un numero.

def factorial(n):
    """Recibe un número <n> y devuelve su factorial."""
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

#Defino el input del valor de m

print('Dado un valor, devuelve el factorial desde 0 -> valor.')
entrada = int(input('Ingrese un valor:'))

#Ciclo que calcula factorial e imprime cada orden

for j in range(0, entrada + 1):
    print('Orden:', j ,'Factorial!:' ,factorial(j))