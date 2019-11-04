'''
Pila:
	-Apilar
	-Desapilar
	-Ver_Tope
	-Esta_Vacia
'''

class Pila:
	def __init__(self):
		self.tope = None

	def apilar(self, valor):
		nuevo = _Nodo(valor, self.tope)
		self.tope = nuevo

	def desapilar(self):
		if self.esta_vacia():
			raise PilaVacia()
		dato = self.tope.tope
		self.tope = self.tope.prox
		return dato

	def ver_tope(self):
		if self.esta_vacia():
			raise PilaVacia()
		return self.tope.tope

	def esta_vacia(self):
		return not self.tope

class PilaVacia(Exception):
	def __init__(self):
		super.__init__('Pila vacia')

class _Nodo:
	def __init__(self, dato, prox):
		self.tope = dato
		self.prox = prox