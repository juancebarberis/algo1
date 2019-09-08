def fahrenheit_a_celsius(fahrenheit):
    """Esta función convierte datos recibidos en Fahrenheit,
     y devuelve celsius."""

    return ((fahrenheit - 32) * 5/9)

fahrenheitIn = int(input('Ingrese grados Fahrenheit: '))

fahrenheitFunction = fahrenheit_a_celsius(fahrenheitIn)

    

