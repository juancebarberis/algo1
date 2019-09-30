#Ejercicio 10.1. Escribir una función, llamada head que reciba un archivo y un número N e im-
#prima las primeras N líneas del archivo.

def head(rutaArchivo, n):
    """"""
    with open(rutaArchivo, 'r') as archivo:
        for linea in range(n):
            print(archivo.readline())

    
head('archivos/101.txt', 3)