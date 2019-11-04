'''
1. Escribir una funci´on reemplazar que tome una Pila, un valor nuevo y un valor viejo y
reemplace en la Pila todas las ocurrencias de valor viejo por valor nuevo. Considerar que la
Pila tiene las primitivas apilar(dato), desapilar() y esta vacia().
'''

def reemplazar(pila, nuevo, viejo):
	pilaAuxiliar = Pila()
	#Recorro pila hasta vaciarla
	while not pila.esta_vacia():
		valor = pila.desapilar()
		if valor == viejo:
			valor = nuevo
		pilaAuxiliar.apilar(valor)
	#Muevo los valor de la pila auxiliar a la pila original
	while not pilaAuxiliar.esta_vacia():
		pila.apilar(pilaAuxiliar.desapilar())

'''
2. Escribir un m´etodo que invierta una ListaEnlazada utilizando una Pila como estructura
auxiliar y considerando que lista solo tiene una referencia al primer nodo.
'''
import enlazadas
import pilas
import colas

def invertir_lista_enlazada(self):
	''''''
	pila = Pila()
	#Apilo todos los elementos en pila
	actual = self.prim
	while actual:
		pila.apilar(actual)
		actual = self.prox
	#Vuelvo a enlistar los datos en la lista de manera invertida
	primero = self.prim
	proximo = self.prox
	while not pila.esta_vacia():
		primero = pila.desapilar()
	proximo = None


'''
3. Escribir una funci´on que reciba una pila de n´umeros y elimine de la misma los elementos
consecutivos que est´an repetidos. Se pueden usar estructuras auxiliares. La funci´on no devuelve
nada, simplemente modifica los elementos de la pila que recibe por par´ametro.
Por ejemplo: remover duplicados consecutivos(Pila([2, 8, 8, 8, 3, 3, 2, 3, 3, 3, 1, 7])) 
Genera: Pila([2, 8, 3, 2, 3, 1, 7]).
'''

def limpiar_repetidos_pila(pila):
	''''''
	pilaAuxiliar = Pila()

	while not pila.esta_vacia():
		valor = pila.desencolar()
		if not pila.esta_vacia():
			siguiente = pila.ver_tope()
		elif valor == siguiente:
			continue
		pilaAuxiliar.apilar(valor)

	while not pilaAuxiliar.esta_vacia():
		pila.apilar(pilaAuxiliar.desapilar())


'''
6. Escribir una funci´on que reciba una cola y la cantidad de elementos en la misma, 
y devuelva True si los elementos forman un pal´ındromo o False si no.
Por ejemplo:
es palindromo([n, e, u, q, u, e,n], 7) − > True
'''

