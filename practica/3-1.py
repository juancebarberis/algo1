#Ejercicio 3.1. Escribir dos funciones que permitan calcular:
#a) La duración en segundos de un intervalo dado en horas, minutos y segundos.
#b) La duración en horas, minutos y segundos de un intervalo dado en segundos.

#Función (a)

def convertirASegundos(h, m, s):
    """Esta función recibe tres parámetros h (horas), m (minutos) y s (segundos) y devuelve
    ese intervalo en segundos."""
    calculo = (h * 3600) + (m * 60) + s 
    return print(calculo, 'segundos.')

#Función (b)

def convertirDeSegundos(segundos):
    """Función que recibe segundos y devuelve un intervalo en formato horas:minutos:segundos"""
    horas       = int(segundos/3600)
    segundos   -= horas*3600
    minutos     = int(segundos/60)
    segundos   -= minutos*60
    return print(horas, minutos, segundos, sep=":")
#SANDBOX

inputSegundos = int(input('Ingrese cantidad de segundos: '))

test = convertirDeSegundos(inputSegundos)