# NOMBRE_Y_APELLIDO = JUAN CELESTINO BARBERIS
# PADRÓN = 105147
# MATERIA = 7540 Algoritmos y Programación 1, curso Essaya
# Ejercicio 1 de entrega obligatoria

from vectores import productoVectorial, norma, diferencia

def areaTriangulo(Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz):
    """Esta función recibe tres vectores A, B y C en R3, y devuelve el área del triángulo que forman dichos vectores."""

    ABx, ABy, ABz = diferencia(Ax, Ay, Az, Bx, By, Bz)
    ACx, ACy, ACz = diferencia(Ax, Ay, Az, Cx, Cy, Cz)

    prodVectX, prodVectY, prodVectZ = (productoVectorial(ABx, ABy, ABz, ACx, ACy, ACz))
    resultadoNorma = norma(prodVectX, prodVectY, prodVectZ)
    
    areaTriangulo = resultadoNorma / 2
     
    return int(areaTriangulo)

assert areaTriangulo(5, 8, -1, -2, 3, 4, -3, 3, 0) == 19
assert areaTriangulo(1, 0, 1, 2, 2, 2, 0, 0, 0) == 1
assert areaTriangulo(5, 6, 7, 5, 4, 3, 1, 1, 1) == 9
assert areaTriangulo(1, 7, 4, 23, 54, 66, 89, 54, 1) == 3515
assert areaTriangulo(67, 1, 2, 0, 0, 0, 1, 1, 0) == 33




