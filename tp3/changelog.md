## Changelog - Reentrega N° 1

- (mapa.py >> Mapa@es_coord_valida) Ahora ya no se recorren dos arreglos completos, sólo se tiene en cuenta si la coordenada a evaluar está entre 0 y filas/columnas que tenga el laberinto en total.
- (mapa.py >> Mapa@_init_) Al instanciar el objeto Mapa se realiza la generación de celdas en el constructor, en relación a las filas y columnas recibidas por parámetro. 
- (ia.py >> IA@_init_) Para self.visitadas ahora se utiliza un diccionario, que mejora la eficiencia.
- (mapa.py >> Coord@_iter_) Se implementó el método __iter__() para la clase Coord.
- (mapa.py >> Mapa@trasladar_coord) Ahora verifica también que la coordenada a trasladar esté dentro de los bordes llamando al método es_coord_valida.
- (ia.py >> IA@avanzar) Ya no se usa un diccionario para manejar las posibles celdas vecinas. Ahora simplemente usamos un arreglo.
- (laberinto.py >> generar) En la línea 45, en el condicional, ahora se llama a los métodos de la clase mapa para validar las coordenadas. Se utiliza mapa.celda_bloqueda() y mapa.es_coord_valida().
- (laberinto.py >> generar_laberinto) El for de la línea 17 fue mejorado notoriamente. Ahora hacemos menos comprobaciones (debido a que ya fueron realizadas en otro momento) y se movió una parte del código a el init de la clase Mapa, en mapa.py.
- (mapa.py >> Mapa@_init_) self.bloqueadas ahora es un diccionario al cual accedemos en tiempo constante. Esto mostró grandes mejoras en la IA y en la generación. ¡Nuestros algoritmos ahora son más rápidos!
- (mapa.py >> Mapa@_iter_) Ahora se pintan todas las celdas del mapa. Antes no se activaba la celda (0, 0).