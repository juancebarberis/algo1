#Ejercicio 2.4. Escribir un programa que imprima todos los números pares entre dos números
#que se le pidan al usuario.

#Defino la función

def paresEntreAB(a, b):
    """Devuelve todos los numeros pares entre A y B"""
    for i in range(a + a % 2, b+1, 2):
        print(i)
    return i

#Inputs de números que se le piden al usuario

print('Números pares entre un valor A y B.')

a = int(input('Ingrese un valor A: '))
b = int(input('Ingrese un valor B: '))

#Llamo la función e imprimo los resultados

salida = paresEntreAB(a, b)

print(salida)


