from procesos_csv import csv_opener

path = input('Ingrese la dirección del .csv\n')
data = csv_opener(path)
# len(data)-> La cantidad de procesos a ingresar
