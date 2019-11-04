'''
Cola:
	-Encolar
	-Desencolar
	-Ver frente
	-Esta vacia?
'''
class Cola:
	def __init__(self):
		self.frente = None
		self.ultimo = None

	def encolar(self, valor):
		nuevo = _Nodo(valor, self.ultimo)
		if self.esta_vacia():
			self.frente = nuevo
		else: 
			self.ultimo.prox = nuevo
		self.ultimo = nuevo


	def desencolar(self):
		if self.esta_vacia():
			return 'Cola vacía'
		dato = self.frente.valor
		self.frente = self.frente.prox
		if self.frente == None:
			self.ultimo = None
		return dato

	def ver_frente(self):
		if not self.esta_vacia():
			return self.frente.valor	
		return 'Cola vacía'

	def esta_vacia(self):
		return self.ultimo == None

class _Nodo:
	def __init__(self, valor, prox=None):
		self.valor = valor
		self.prox = prox


