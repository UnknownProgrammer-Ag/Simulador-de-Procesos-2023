from procesos_csv import csv_opener
from terminaltables import AsciiTable
from memoria import Memoria,memoria_principal
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
def simulador(self):
    path = filedialog.askopenfilename(title="Seleccionar Archivo CSV",filetypes=[("Archivo csv","*.csv"),("Todos los archivos","*.*")])
    arch = csv_opener(path)


