#Ejercicio 10.6. Persistencia de un diccionario
#a) Escribir una función cargar_datos que reciba un nombre de archivo, cuyo contenido
#tiene el formato clave, valor y devuelva un diccionario con el primer campo como clave
#y el segundo como valor.
#b) Escribir una función guardar_datos que reciba un diccionario y un nombre de archivo,
#y guarde el contenido del diccionario en el archivo, con el formato clave, valor .

def cargar_datos(ruta):
    '''.'''
    resultado = {}
    with open(ruta) as archivo:
        for linea in archivo:
            clave, valor = linea.rstrip('/n').split(',')
            resultado[clave] = resultado.get(clave, 0) + int(valor)
    return resultado

print(cargar_datos('archivos/106.txt'))    
