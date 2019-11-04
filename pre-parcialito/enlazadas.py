class ListaEnlazada:
    def __init__(self):
        self.prim = None
        self.cant = 0

    def append(self, dato):
        nuevo = _Nodo(dato, None)
        if self.prim is None:
            self.prim = nuevo
        else:
            act = self.prim
            while act.prox is not None:
                act = act.prox
            act.prox = nuevo
        self.cant += 1

    def __str__(self):
        s = "LE("
        act = self.prim
        while act is not None:
            s += str(act.dato) + ", "
            act = act.prox
        s += ")"
        return s

    def __len__(self):
        return self.cant

class _Nodo:
    """Representa un nodo con un dato y una referencia
    al sig. nodo"""

    def __init__(self, dato, prox):
        self.dato = dato
        self.prox = prox

    def __repr__(self):
        return f"Nodo({self.dato}, {self.prox})"