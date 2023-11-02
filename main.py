# Importar modulos separados del simulador
from procesos_csv import csv_opener
# Importar modulos de Python para facilitar implementación
import tkinter as tk
from tkinter import filedialog
from time import sleep
from collections import deque

root = tk.Tk()
root.withdraw()

def simulador(arch):
    tiempo_total=0
    nuevos=deque()
    listos=deque()
    mult_P=0
    while True:
        #Cargar Cola de Nuevos

        tiempo_total+=1




# Principal
print("Bienvenido a Simulador ROUND ROBIN de Procesos")
print("Ahora, para iniciar el simulador ingrese el archivo CSV que contendrá los procesos")
sleep(2)
path = filedialog.askopenfilename(title="Seleccionar Archivo CSV", filetypes=[("Archivo csv", "*.csv"), ("Todos los archivos", "*.*")])
arch = csv_opener(path)

# Llamada al Simulador
if arch != None:

else:
    print("El archivo csv estaba vacío o fallo en cargar")
