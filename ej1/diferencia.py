# NOMBRE_Y_APELLIDO = JUAN CELESTINO BARBERIS
# PADRÓN = 105147
# MATERIA = 7540 Algoritmos y Programación 1, curso Essaya
# Ejercicio 1 de entrega obligatoria

def diferencia(x1, y1, z1, x2, y2, z2):
    """Recibe las coordenadas de dos vectores en R3 y devuelve su diferencia"""
    dif_x = x1 - x2
    dif_y = y1 - y2
    dif_z = z1 - z2
    return dif_x, dif_y, dif_z

# Agregar pruebas

assert diferencia(1, 2, 3, 1, 2, 3) == (0, 0, 0)

assert diferencia(16, -72, -52, 55, 90, -31) == (-39, -162, -21)

assert diferencia(55, -88, -75, 38, 62, -12) == (17, -150, -63)

assert diferencia(-55, -87, -32, -10, 3, -34) == (-45, -90, 2)

assert diferencia(-29, 90, 77, 32, -81, -48) == (-61, 171, 125)

assert diferencia(73, 33, 6, 98, -79, -73) == (-25, 112, 79)
