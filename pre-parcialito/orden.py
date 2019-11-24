 #Ordenamiento por selección
lista = [0, -1, 4, 56, 7, 11, 6, -3, 2, 1, 5, 21, 67, 89, 0]
print('Lista a ordenar:')
print(lista)

def seleccion(lista):
	'''
	'''
	longitud = len(lista) - 1

	while longitud > 0:
		p = maximo(lista, 0, longitud)

		lista[p], lista[longitud] = lista[longitud], lista[p]
		print("DEBUG: ", p, longitud, lista)

		longitud = longitud - 1 

def maximo(lista, a, b):
	'''
	Recibe una lista no vacía con elementos comparables, y a y b son las posiciones iniciales 
	y finales de la lista.
	'''
	pos_max = a
	for i in range(a + 1, b + 1):
		if lista[i] > lista[pos_max]:
			pos_max = i
	return pos_max

#Ordenamiento por inserción

def insercion(lista):
	'''
	Ordena una lista de elementos comparables siguiendo el algoritmo de inserción.
	'''
	for i in range(len(lista) - 1):
		if lista[i + 1] < lista[i]:
			reubicar(lista, i + 1) 
	print(lista)

def reubicar(lista, p):
		v = lista[p]
		# Recorrer el segmento [0:p-1] de derecha a izquierda hasta
		# encontrar la posición j tal que lista[j-1] <= v < lista[j].
		j = p
		while j > 0 and v < lista[j - 1]:
			# Desplazar los elementos hacia la derecha, dejando lugar
			# para insertar el elemento v donde corresponda.
			lista[j] = lista[j - 1]
			j -= 1
		lista[j] = v

#Ordenamiento por Merge

def merge_sort(lista):
	if len(lista) <= 1:
		return lista
	med = len(lista) // 2
	izq = lista[:med]
	der = lista[med:]
	return merge(izq, der)

def merge(lista1, lista2):
	resultado = []
	i, j = 0, 0
	while (i < len(lista1) and j < len(lista2)):
		if lista1[i] < lista2[j]:
			resultado.append(lista1[i])
			i += 1
		else:
			resultado.append(lista2[j])
			j += 1
	resultado += lista1[i:]
	resultado += lista2[j:]
	return resultado


'''
El ordenamiento por selección obtiene el elemento mayor de un arreglo y lo posiciona
al final de la lista. Luego, realiza lo mismo, omitiendo el último valor (porque ya está
ordenado). Así hasta llegar a la posición 0.

El ordenamiento por inserción se desplaza hacia la derecha comparando uno a uno. 
Si el valor del elemento actual es mayor al siguiente elemento, lo intercambia y 
posiciona el más chico en la lista que va desde 0 hasta el elemento actual.
Para más info, este gif: https://es.wikipedia.org/wiki/Ordenamiento_por_inserci%C3%B3n

'''