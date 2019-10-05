import csv

dict_final = {}
with open('archivos/example.csv') as arch:
    arch_csv = csv.DictReader(arch)
    for linea in arch_csv:
        print(linea)