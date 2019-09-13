# NOMBRE_APELLIDO = JUAN CELESTINO BARBERIS
# PADRÓN = 105147
# MATERIA = 7540 Algoritmos y Programación 1, curso Essaya
# Ejercicio 2 de entrega obligatoria

#Ejercicio 6.9. Implementar la función pedir_entero(mensaje, min, max) , que debe imprimir
#el mensaje y luego esperar a que el usuario ingrese un valor. Si el valor ingresado no es un
#número entero, o no es un número entre min y max (inclusive), se le debe avisar al usuario y
#pedir el ingreso de otro valor. Una vez que el usuario ingresa un valor válido, la función lo debe
#devolver.

def pedirEntero(mensaje, min, max):
    """Esta función recibe un <mensaje>, un valor mínimo <min> y un máximo <max> en números enteros.
    Muestra al usuario <mensaje>, el intervalo <min>|<max> y le pide ingresar un <valor>. 
    Si el valor se encuentra entre <min> y <max>, devuelve el <valor>
    """

    mensajeError = f'Por favor, ingrese un valor entre {min} y {max}.'
    mensajeInput = f"{mensaje} [{min} | {max}]:"

    while True:
        valor = input(mensajeInput)

        if valor.isalpha() == True or valor == '':
            print(mensajeError)
            continue
        
        if (int(valor) >= min) and (int(valor) <= max):
            break
        else:
            print(mensajeError)

    return valor

z = pedirEntero("¿Cuál es tu número favorito?", -50, 50)
print(z)
