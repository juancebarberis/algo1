'''
Ejercicio 11.1.
a) Implementar la clase Intervalo(desde, hasta) que representa un intervalo entre dos
instantes de tiempo (números enteros expresados en segundos), con la condición desde
< hasta .
b) Implementar el método duracion que devuelve la duración en segundos del intervalo.
c) Implementar el método interseccion que recibe otro intervalo y devuelve un nuevo in-
tervalo resultante de la intersección entre ambos, o lanzar una excepción si la intersección
es nula.
d) Implementar el método union que recibe otro intervalo. Si los intervalos no son adya-
centes ni intersectan, debe lanzar una excepción. En caso contrario devuelve un nuevo
intervalo resultante de la unión entre ambos.
'''

class Intervalo:
	def __init__(self, desde, hasta):
		self.desde = desde
		self.hasta = hasta

