#Ejercicio 5.4. Utilizando la función randrange del módulo random , escribir un programa que
#obtenga un número aleatorio secreto, y luego permita al usuario ingresar números y le indique
#si son menores o mayores que el número a adivinar, hasta que el usuario ingrese el número
#correcto.

from random import randrange

def adivinarNumeroAleatorio():
    """"""
    numeroSecreto = randrange(start= 0, stop=100)

    print('Adivine el número entre 0 y 100.')

    while True:
        entrada = input('Ingrese el candidato:')

        if not entrada.isnumeric():
            print('Por favor, ingrese un número válido.')
            continue
        else:
            entrada = int(entrada)
        
        if entrada == numeroSecreto:
            break

        if entrada > numeroSecreto:
            print(f'El número {entrada} es mayor que el número a adivinar.')
            continue
        if entrada < numeroSecreto:
            print(f'El número {entrada} es menor que el número a adivinar.')
            continue
    print('¡Genial, adivinaste! El número era ' + str(numeroSecreto))

adivinarNumeroAleatorio()