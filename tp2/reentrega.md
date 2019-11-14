## Changelog de la reentrega

Recordar de volver a activar los obstaculos.

Módulo: cargar.

- (Línea 21 - cargarVariablesNivel) Documentación de la función mejorada.
- (Línea 39 - cargarVariablesNivel) Except ahora espera un ValueError.
- (Línea 41 - cargarVariablesNivel) Ahora la variables OBSTACLE del diccionario de cada nivel, realiza un .split() inicial y guarda nuevamente los obstaculos del nivel en una lista de tuplas. También se revisó la documentación.
- (Línea 47 - cargarVariablesNivel) Except ahora espera un KeyError, ya que el nivel puede no tener especiales.
- (Línea 103 - cargarEspeciales) Se quitó el contador 'cantidadDeFilas'. Ahora se accede a la cantidad de elementos en el diccionario a través de la función len().

Módulo: generar.

- (Línea 4) La función generarTablero() fue movida al módulo 'imprimir' ya que sólo este hacia uso de ella.
- (Línea 12 - generarFruta) Se removió el bloque Try/Except que comprobaba que la fruta no se genere encima de un obstaculo ya que esta comprobación se realiza en la función generarEspecial() del mismo módulo, además, de que la función generarFruta se ejecuta siempre antes que generarEspecial(). Esto era código repetido.
- (Línea 28 - generarEspecial) Bloque Try/Except optimizado. Except ahora realiza la operación pass.
- (Línea 36 - generarEspecial) Condicional if reemplazado por un ciclo while. Esto asegura que nunca se generen en la misma coordenada. 

Módulo: imprimir.

- (Línea 32 - imprimirTablero) Se removio el innecesario Try/Except al generar la fruta.
- (Línea 36 - imprimirTablero) Se removio el innecesario Try/Except al posicionar los obstaculos. Estos ahora son más simples gracias al cambio realizado anteriormente en el módulo de carga. 