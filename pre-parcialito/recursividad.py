'''
11) Escribir una funcion recursiva en Python que ordene una Pila (la cual contiene unica-
mente numeros) de menor a mayor (quedando el elemento mas grande en el tope).
'''
from pilas import *

def ordenar(pila):
    '''
    Recibe: una pila con números.

    Devuelve: la misma pila, con los números ordenados de menor a mayor.
    '''
    if pila.esta_vacia():
        return pila
    lista_aux = []
    while not pila.esta_vacia():
        lista_aux.append(pila.desapilar())
    lista_aux = sorted(lista_aux)
    return _ordenar_pila(pila, lista_aux)

def _ordenar_pila(pila, lista):
    if len(lista) == 0:
        return
    pila.apilar(lista.pop(0))
    return _ordenar_pila(pila, lista)

'''
12) Escribir una funcion recursiva en Python que cuente la cantidad de apariciones de un
elemento en una lista recibidos por parametro.
'''

def contar(lista):
    '''
    Recibe: una lista.

    Devuelve: un diccionario con elemento::cantidad de apariciones.
    '''
    resultado = {}
    indice = 0
    return _contar(lista, resultado, indice)

def _contar(lista, resultado, indice):
    if len(lista) - 1 == indice:
        return resultado
    if lista[indice] not in resultado:
        resultado[lista[indice]] = 1
    else:
        resultado[lista[indice]] += 1
    return _contar(lista, resultado, indice + 1)

    