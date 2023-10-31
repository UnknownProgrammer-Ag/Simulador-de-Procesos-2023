# Importar modulos separados del simulador
from procesos_csv import csv_opener
from memoria import Memoria, memoria_principal

# Importar modulos de Python para facilitar implementación
from terminaltables import AsciiTable
import tkinter as tk
from tkinter import filedialog
from time import sleep
from threading import Event, Thread

root = tk.Tk()
root.withdraw()
pausa_simulador = Event()

estado_Simulador = {"ejecutando": True, "salida": ""}


# Principal
print("Bienvenido a Simulador ROUND ROBIN de Procesos")
print("Ahora, para iniciar el simulador ingrese el archivo CSV que contendra los procesos")
sleep(2)

path = filedialog.askopenfilename(title="Seleccionar Archivo CSV", filetypes=[
                                  ("Archivo csv", "*.csv"), ("Todos los archivos", "*.*")])
arch = csv_opener(path)

# Llamada al Simulador
if arch != None:
    tiempo_total = 0
    print(tiempo_total)

else:
    print("El archivo csv estaba vacío o fallo en cargar")
