class Impresora:
	def __init__(self, nombre, tinta):
		self.nombre = nombre
		self.tinta_max = tinta
		self.tinta = tinta
		self.cola = []

	def cargar_tinta(self):
		self.tinta = self.tinta_max

	def encolar(self, documento):
		self.cola.append(documento)

	def imprimir(self):
		if self.esta_vacia():
			return 'No hay nada para imprimir'
		doc = self.cola.pop(0)
		return doc + ' impreso.'

	def esta_vacia(self):
		return self.cola[0] == None

class Oficina: