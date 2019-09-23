#Ejercicio 7.7. Escribir una función que reciba una lista de tuplas (Apellido, Nombre, Ini-
#cial_segundo_nombre) y devuelva una lista de cadenas donde cada una contenga primero el
#nombre, luego la inicial con un punto, y luego el apellido.

data = [
    ('Viviana', 'Tupac', 'R'),
    ('Francisco', 'Tupac', 'M'),
    ('Raquel', 'Barquez', 'H'),
    ('Mocca', 'Tupac Barquez', 'D'),
    ('Lara', 'Tupac Barquez', 'P')
]

def tuplaACadena(lista):
    """
    Esta función recibe una lista de tuplas con (Nombre, Apellido, Inicial segundo nombre)
    y devuelve una lista con cadenas, donde cada una representa "Nombre Inicial. Apellido).
    """
    resultante = []

    for persona in lista:
        cadenaIndividual = ""
        cadenaIndividual += f"{persona[1]} {persona[2]}. {persona[0]}"
        resultante.append(cadenaIndividual)
    return resultante  

print(tuplaACadena(data))