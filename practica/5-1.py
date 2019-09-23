#Ejercicio 5.1. Escribir un programa que permita al usuario ingresar un conjunto de notas, pre-
#guntando a cada paso si desea ingresar más notas, e imprimiendo el promedio correspondiente.

def promedioNotas():
    """Recibe notas del usuario y calcula el promedio de las mismas."""
    promedio = 0
    cantidad = 0
    entrada = int(input('Ingrese una nota: '))

    while entrada != 0:
        cantidad += 1

        print('El promedio es: ', entrada / cantidad)

        pregunta = input('Desea ingresar otro nota? [s/n]: ')
        if (pregunta == 'n' or pregunta == ''):
            print('Gracias por utilizar el programa!')
            break
        
        entrada = int(input('Ingrese otra nota: '))

promedioNotas()