from procesos_csv import csv_opener
from procesos_csv import Proceso

path = input('Ingrese la dirección del .csv\n')
arch = csv_opener(path)


# TESTING-> Borrar cuando se continue con la implementacion
# print(len(arch))  -> La cantidad de procesos a ingresar

# Con este código puede comprobar que se copiaron correctamente los valores del .csv.
for proc in arch:
    print("Proceso ", proc.id, "Tamaño ", proc.tam,
          "TA ", proc.arribo, "TI ", proc.irrup)
