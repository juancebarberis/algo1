class Pila:
    def __init__(self):
        self.tope = None
    
    def apilar(self, valor):
        if not self.tope:
            self.tope = _Nodo(valor)
        else:
            nuevo = _Nodo(valor, prox=self.tope)
            self.tope = nuevo

class _Nodo:
    def __init__(self, valor, prox):
        self.valor = valor
        self.prox = prox
