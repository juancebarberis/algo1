'''
Ejercicio 15.3. Ordenar la lista 6 0 3 2 5 7 4 1 usando el método quicksort. Mostrar el árbol
de recursividad explicando las llamadas que se hacen en cada paso, y el orden en el que se
realizan.
'''

lista = [6, 0, 3, 2, 5, 7, 4, 1]

def quicksort(lista):
    '''
    Ordena una lista utilizando el algoritmo quicksort.
    Los elementos deben ser comparables.
    '''
    pivot = lista[-1]
    if len(lista) <= 2:
        return lista
    menores, mayores = ordenar(lista, pivot)
    
    return lista

def ordenar(lista, pivot):
    '''
    Devuelve dos listas, una con todos los valores menores al pivot, y otra con 
    todos los mayores.
    '''

