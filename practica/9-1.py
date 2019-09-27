#Ejercicio 9.1. Escribir una función que reciba una lista de tuplas, y que devuelva un diccionario
#en donde las claves sean los primeros elementos de las tuplas, y los valores una lista con los
#segundos.

def tuple2dic(lista):
    """"""
    resultado = {}

    for prim, seg in lista:
        if prim in resultado:
            resultado[prim].append(seg)
        else:
            resultado[prim] = [seg]
    return resultado

print(tuple2dic([(1, 1), (2, 1), (0, 1), (1,4)]))