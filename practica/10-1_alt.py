#Ejercicio 10.1. Escribir una función, llamada head que reciba un archivo y un número N e im-
#prima las primeras N líneas del archivo.

def head(entrada, salida, n):
    """"""
    with open(entrada, 'r') as arch_entrada, open(salida, 'w') as arch_salida:
        for i in range(n):
            arch_salida.write(arch_entrada.readline().rstrip('\n'))

def tail(entrada, salida, n):
    """"""
    ventana = []

    with open(entrada, 'r') as arch:

        for i in range(n):
            linea = arch.readline()

            if not linea:
                break
            ventana.append(linea)

        for linea in arch:
            ventana.append(linea)
            ventana.pop(0)

    with open(salida, 'w') as arch:
        arch.writelines(ventana)

tail('archivos/101.txt', 'archivos/101_salida.txt', 3)