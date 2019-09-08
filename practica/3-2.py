#Ejercicio 3.2. Usando las funciones del ejercicio anterior, escribir un programa que pida al usua-
#rio dos intervalos expresados en horas, minutos y segundos, sume sus duraciones, y muestre
#por pantalla la duración total en horas, minutos y segundos.

def convertirASegundos(h, m, s):
    """Esta función recibe tres parámetros h (horas), m (minutos) y s (segundos) y devuelve
    ese intervalo en segundos."""
    calculo = (h * 3600) + (m * 60) + s 
    return calculo

def convertirDeSegundos(segundos):
    """Función que recibe segundos y devuelve un intervalo en formato horas:minutos:segundos"""
    horas       = int(segundos/3600)
    segundos   -= horas*3600
    minutos     = int(segundos/60)
    segundos   -= minutos*60
    return horas, minutos, segundos

#Inputs

print('Ingrese hh:mm:ss para el intervalo A.')
horasA      = int(input('Horas de A: '))
minutosA    = int(input('Minutos de A: '))
segundosA   = int(input('Segundos de A: '))

print('Ingrese hh:mm:ss para el intervalo B.')
horasB      = int(input('Horas de B: '))
minutosB    = int(input('Minutos de B: '))
segundosB   = int(input('Segundos de B: '))

A = convertirASegundos(horasA, minutosA, segundosA) 
B = convertirASegundos(horasB, minutosB, segundosB)

hora, minutos, segundos = convertirDeSegundos(A + B)

print('La suma de los dos intervalos es: ', hora, ':', minutos, ':', segundos, ' hh:mm:ss')