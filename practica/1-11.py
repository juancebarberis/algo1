class ColaConPrioridad:
    def __init__(self):
        self.prioridad = Cola()
        self.normal = Cola()
    
    def vacia(self):
        return self.prioridad.vacia() and self.normal.vacia()
    
    def encolar(self, valor):
        self.normal.encolar(valor)
    
    def encolarConPrioridad(self):
        self.prioridad.encolar(valor)
    
    def desencolar(self):
        if self.prioridad.vacia() and not self.normal.vacia():
            return self.normal.desencolar()
        else:
            return self.prioridad.desencolar()

