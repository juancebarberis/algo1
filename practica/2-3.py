#Ejercicio 2.3. Utilice el programa anterior para generar una tabla de conversión de temperatu-
#ras, desde 0 °F hasta 120 °F, de 10 en 10.

def fahrenheit_a_celsius(fahrenheit):
    """Esta función convierte datos recibidos en Fahrenheit,
     y devuelve celsius."""

    return ((fahrenheit - 32) * 5/9)

print('Fahrenheit - Celsius')

for i in range(0, 100, 10):
    celsius = fahrenheit_a_celsius(i)
    fahrenheit = i
    #Imprimo la tabla
    print(fahrenheit, ' - ', celsius)