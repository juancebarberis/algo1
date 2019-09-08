# NOMBRE_Y_APELLIDO = JUAN CELESTINO BARBERIS
# PADRÓN = 105147
# MATERIA = 7540 Algoritmos y Programación 1, curso Essaya
# Ejercicio 1 de entrega obligatoria


#def productoVectorial(x1, y1, z1, x2, y2, z2):
#    """Recibe las coordenadas de dos vectores en R3 y devuelve el producto vectorial"""
#    resultadoX = y1*z2 - z1*y2
#    resultadoY = z1*x2 - x1*z2
#    resultadoZ = x1*y2 - y1*x2
#    return resultadoX, resultadoY, resultadoZ

def productoVectorial(x1, y1, z1, x2, y2, z2):
    """Recibe las coordenadas de dos vectores en R3 y devuelve el producto vectorial"""
    return y1*z2 - z1*y2, z1*x2 - x1*z2, x1*y2 - y1*x2

assert productoVectorial(54, 12, 29, 1, 11, 12) == (-175, -619, 582)
assert productoVectorial(71, 52, 24, 1, 11, 6) == (48, -402, 729)
assert productoVectorial(726, 434, 110, 488, 962, 820) == (250060, -541640, 486620)
assert productoVectorial(62, 12, 198, 380, 334, 490) == (-60252, 44860, 16148)
assert productoVectorial(-85, 807, 964, 462, 101, 474) == (285154, 485658, -381419)
assert productoVectorial(746, 466, 396, 910, 138, 289) == (80026, 144766, -321112)
assert productoVectorial(-15, 53, 105, 413, 149, 270) == (-1335, 47415, -24124)
assert productoVectorial(291, 413, 227, 166, 638, 284) == (-27534, -44962, 117100)
assert productoVectorial(192, 362, 397, 249, 598, 50) == (-219306, 89253, 24678)
assert productoVectorial(781, 520, 996, 348, 68, 215) == (44072, 178693, -127852)
assert productoVectorial(459, 971, 201, 582, 569, 703) == (568244, -205695, -303951)
assert productoVectorial(754, 968, 956, 231, 901, -31) == (-891364, 244210, 455746)



