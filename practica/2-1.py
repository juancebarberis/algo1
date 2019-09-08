#Ejercicio 2.1. Escribir un programa que le pregunte al usuario una cantidad de pesos, una tasa
#de interés y un número de años y muestre como resultado el monto final a obtener.
#Donde C es el capital inicial, x es la tasa de interés y n es el número de años a calcular.

#Defino la funcion que calcula los datos ingresados

def plazoFijo(capitalInicial, tasa, tiempo):
    """Dados un (capitalInicial, tasa, tiempo) devuelve un montoFinal"""
    calculo = capitalInicial * ((1 + (tasa/100))**tiempo)
    return calculo

#Inputs para el usuario
print('Calculo de plazo fijo.')

capitalInicial = float(input('Ingrese un capital incial (en pesos): '))

tasa = float(input('Ingrese una tasa de interés: '))

tiempo = int(input('Ingrese la cantidad de años: '))

#Print del resultado

resultado = plazoFijo(capitalInicial, tasa, tiempo)

print('El monto final a obtener es:', resultado)