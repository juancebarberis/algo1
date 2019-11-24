#Ejercicios del cuarto parcialito

'''
2) Escribir una funci´on recursiva que reciba una lista y un par´ametro n, y devuelva otra
lista con los elementos de la lista replicados esa cantidad n de veces.
Por ejemplo, replicar ([1, 3, 3, 7], 2) debe devolver ([1, 1, 3, 3, 3, 3, 7, 7]) .
'''
def repetir_elementos_con_parametro(lista, n):
    '''
    Recibe: una lista y un parámetro n (int)
    
    Devuelve: una lista con los elementos de la lista replicados esa cantidad n de veces.
    '''
    resultado = []
    return _replicar(lista, n, resultado)

def _replicar(lista, n, resultado):
    '''
    Recibe: '...' y una lista del resultado

    Devuelve: una lista con el resultado.
    '''
    if len(lista) == 0:
        return resultado
    elemento = lista[0]
    for i in range(n):
        resultado.append(elemento)
    lista.pop(0)
    return _replicar(lista, n, resultado)

'''
3) a) Mostrar paso a paso como funcionar´ıan los algoritmos de inserci´on y quicksort sobre
la siguiente lista de n´umeros: [9, 12, 1, 4, 2, 8, 15, 21]
b) ¿Cual de los dos algoritmos es m´as eficiente para ordenar una gran cantidad de elementos?
¿Por qu´e?

RESPUESTA (a):
Lista: [9, 12, 1, 4, 2, 8, 15, 21]

Por Inserción, defino i como mi posición actual. En primer lugar [i] = 9, lo comparon con 12.
Como 9 < 12, la lista desde [0:i] está ordenada. Ahora [i] = 12, y lo comparo con el 
siguiente elemento. 12 > 1, entonces debo intercambiar la posición [i] por [i + 1] (el nuevo
valor de i = 4). El uno que intercambié por el 12, debo ubicarlo donde esté ordenado, entonces
recorro la lista desde [0:i] pero de derecha a izquierda, comparando el 1 con cada elemento hasta
encontrar uno donde el elemento no sea menor al siguiente. Entonces la lista quedará [1, 9, 12, ...]
siendo ahora i = 4 y repitiendo el mismo proceso hasta llegar al final de la lista, donde la lista
estará ordenada de menor a mayor.

Por quicksort. Eligo el último elemento como pivot. Divido la lista en tres sublistas.
Lista 1 (menores que el pivot): [9, 12, 1, 4, 2, 8, 15]
Lista 2 (pivote): [21]
Lista 3 (mayores que el pivot): []

Ahora recursivamente opero sobre la lista 1 y 2, realizando la misma operación.
Para la lista 1:
Sublista 1:[9, 12, 4, 2, 8]
Sublista 2:[15]
Sublista 3:[]
Para la lista 2:
Está vacía

Opero una vez más recursivamente:
Sublista 1:[4, 2]
Sublista 2:[8]
Sublista 3:[9, 12]

Ahora concatenamos las sublistas (ordenadas previamente) y la lista resulta:
[1, 2, 4, 8, 9, 12, 15, 21]

RESPUESTA (b):
Quicksort es más eficiente a la hora de ordenar grandes cantidades de datos, y en el peor
de los casos, su rapidez sería similar a la del algoritmo de incersion. Por lo que siempre 
nos conviene Quicksort frente a Inserción.

4) a) ¿Cómo deberı́a ser un arreglo con números del 1 al 10 para obtener la peor performance
en una implementación de quicksort que elige siempre como pivote al último elemento de la
lista en vez del primero? Justifique.
b) ¿Qué método de ordenamiento elegirı́a para ordenar ascendentemente un arreglo que ya
está ordenado pero en forma descendente? ¿Por qué?. Asumiendo que fueran muchos elementos,
¿elegirı́a este método de ordenamiento o utilizarı́a una función para invertirlos in- place (en el
mismo arreglo)?


RESPUESTA (a):
El arreglo debería estar ordenado de forma ascendente. De esta forma, el algoritmo de quicksort
realizará N cuadrado operaciones. Ya que el pivote siempre va a ser mayor que todos los elementos
de la lista. Terminaría siendo un algortimo de selección.

RESPUESTA (b):


'''
