#Ejercicio 7.8. Inversión de listas
#a) Realizar una función que, dada una lista, devuelva una nueva lista cuyo contenido sea
#igual a la original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'] ,
#deberá devolver ['papa', 'a', 'día', 'buen', 'Di'] .
#b) Realizar otra función que invierta la lista, pero en lugar de devolver una nueva, modi-
#fique la lista dada para invertirla, sin usar listas auxiliares.

lista = [1, 2, 3, 4, 5, 6]

def invertirLista(lista):
    """"""
    for i in range(len(lista)//2):
        primero = lista[i]
        segundo = lista[-1-i]
        lista[i] = segundo
        lista[-1-i] = primero
    return 

print(invertirLista(lista))
print(lista)