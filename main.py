#Librerias y Modulos necesarios para iniciar el programa
from procesos_csv import csv_opener
from simulador import sim
import tkinter as tk
from tkinter import filedialog
from time import sleep
import os

root = tk.Tk()
root.withdraw()
#-------------------------------------------------------------------------------------
# Principal
print("Bienvenido a Simulador ROUND ROBIN de Procesos")
print("Ahora, para iniciar el simulador ingrese el archivo CSV que contendrá los procesos")
sleep(2)
path = filedialog.askopenfilename(title="Seleccionar Archivo CSV", filetypes=[
                                  ("Archivo csv", "*.csv"), ("Todos los archivos", "*.*")])
procesos = csv_opener(path) #Lista de Todos los procesos
# Llamada al Simulador
if procesos != None:
    os.system('cls||clear')
    sim.cargarArch(procesos)
    sim.programa()
else:
    print("El archivo csv estaba vacío o fallo en cargar")
