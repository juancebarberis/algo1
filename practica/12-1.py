'''
Ejercicio 12.1. Escribir una clase TorreDeControl que modele el trabajo de una torre de control de
un aeropuerto con una pista de aterrizaje. Los aviones que están esperando para aterrizar tienen
prioridad sobre los que están esperando para despegar. La clase debe funcionar conforme al
siguiente ejemplo:
>>> torre = TorreDeControl()
>>> torre.nuevo_arribo('AR156')
>>> torre.nueva_partida('KLM1267')
>>> torre.nuevo_arribo('AR32')
>>> torre.ver_estado()
Vuelos esperando para aterrizar: AR156, AR32
Vuelos esperando para despegar: KLM1267
>>> torre.asignar_pista()
El vuelo AR156 aterrizó con éxito.
>>> torre.asignar_pista()
El vuelo AR32 aterrizó con éxito.
>>> torre.asignar_pista()
El vuelo KLM1267 despegó con éxito.
>>> torre.asignar_pista()
'''

class TorreDeControl:
    def __init__(self):
        self.para_aterrizar = []
        self.para_despegar = []
    
    def nuevo_arribo(self, vuelo):
        self.para_aterrizar.append(vuelo)

    def nueva_partida(self, vuelo):
        self.para_despegar.append(vuelo)
    
    def ver_estado(self):
        aterrizar = ", ".join(self.para_aterrizar)
        despegar = ", ".join(self.para_despegar)
        print(f"Vuelos esperando para aterrizar:{aterrizar}")
        print(f"Vuelos esperando para despegar:{despegar}")
    
    def asignar_pista(self):
        if len(self.para_aterrizar) > 0:
            vuelo = self.para_aterrizar.pop(0)
            return f"El vuelo {vuelo} aterrizó con éxito."
        elif len(self.para_despegar) > 0:
            vuelo = self.para_despegar.pop(0)
            return f"El vuelo {vuelo} despegó correctamente."
        return "No hay vuelos programados."