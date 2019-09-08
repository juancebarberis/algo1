
# 1 PRÓLOGO
# 1.1 Presentación
# 1.1.1 Título
print('convertidor de números enteros a romanos.')
print()
# 1.1.2 Bienvenida  
print('Bienvenid@.')
print()
# 1.1.3 Objetivo
print('Este programa se encargará de convertir los números enteros a números romanos.')
print()
# 1.2 Obtención de los años y los meses de ambas fechas
# 1.2.1 Solicitud e ingreso del número
numero=int(input('Ingrese un número,(comprendido por el intervalo 1-3999): '))
print()
# 2 RESOLUCIÓN
# 2.1 cálculos
# 2.1.1 Cálculo # SECCIÓN DECLARATIVA (Definición de Recursos) y SECCIÓN ALGORÍTMICA (Desarrollo de la Solución)
# Nombre del programa Calculadora de diferencia entre fechas
# Objetivo del programa convertir numeros enteros en numeros romanos
# Autor, fecha, versión Pachón Pintos Nicolás, 02/08/19, 3.3.4de la unidad, Decena, Centena y Unidad de mil del número
if numero>=1 and numero<=9:
    C1=numero%10
    C2=0
    C3=0
    C4=0
elif numero>=10 and numero<=99:
    C1=numero%10
    C2=(numero%100-C1)/10
    C3=0
    C4=0
elif numero>=100 and numero<=999:
    C1=numero%10
    C2=(numero%100-C1)/10
    C3=(numero%1000-C1-C2*10)/100
    C4=0
else:
    C1=numero%10
    C2=(numero%100-C1)/10
    C3=(numero%1000-C1-C2*10)/100
    C4=(numero%10000-C1-C2*10-C3*100)/1000
# 2.2 Análisis de las cifras y asignación de números romanos
if C1==1:
    U='I'
elif C1==2:
    U='II'
elif C1==3:
    U='III'
elif C1==4:
    U='IV'
elif C1==5:
    U='V'
elif C1==6:
    U='VI'
elif C1==7:
    U='VII'
elif C1==8:
    U='VIII'
elif C1==9:
    U='IX'
else:
    U=''
if C2==1:
    D='X'
elif C2==2:
    D='XX'
elif C2==3:
    D='XXX'
elif C2==4:
    D='XL'
elif C2==5:
    D='L'
elif C2==6:
    D='LX'
elif C2==7:
    D='LXX'
elif C2==8:
    D='LXXX'
elif C2==9:
    D='XC'
else:
    D=''
if C3==1:
    C='C'
elif C3==2:
    C='CC'
elif C3==3:
    C='CCC'
elif C3==4:
    C='CD'
elif C3==5:
    C='D'
elif C3==6:
    C='DC'
elif C3==7:
    C='DCC'
elif C3==8:
    C='DCC'
elif C3==9:
    C='CM'
else:
    C=''
if C4==1:
    Um='M'
elif C4==2:
    Um='MM'
elif C4==3:
    Um='MMM'
else:
    Um=''


# 2.3 Exhibición de los datos
print('Equivale al número romano: ',Um+C+D+U)