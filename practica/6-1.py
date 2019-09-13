#Ejercicio 6.1. Escribir funciones que dada una cadena de caracteres:
#a) Imprima los dos primeros caracteres.
#b) Imprima los tres últimos caracteres.
#c) Imprima dicha cadena cada dos caracteres. Ej.: 'recta' debería imprimir 'rca'
#d) Dicha cadena en sentido inverso. Ej.: 'hola mundo!' debe imprimir '!odnum aloh'
#e) Imprima la cadena en un sentido y en sentido inverso. Ej: 'reflejo' imprime
#'reflejoojelfer' .

def imprimirDosPrimerosCaracteres(s):
    print('Primeros dos: ' + s[:2])

def imprimirTresUltimosCaracteres(s):
    print('Tres ultimos caracteres: ' + s[-3:])

def imprimirCadaDosCaracteres(s):
    print('Cada dos caracteres: ' + s[::2])

def imprimirCadenaInversa(s):
    print('Inversa: ' + s[::-1])

def imprimirCadenaEInversa(s):
    print('Cadena e Inversa: ' + s + s[::-1])

entrada = input('Ingrese una secuencia: ')
aReturn = imprimirDosPrimerosCaracteres(entrada)
bReturn = imprimirTresUltimosCaracteres(entrada)
cReturn = imprimirCadaDosCaracteres(entrada)
dReturn = imprimirCadenaInversa(entrada)
eReturn = imprimirCadenaEInversa(entrada)