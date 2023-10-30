from procesos_csv import csv_opener
from terminaltables import AsciiTable
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

path = filedialog.askopenfilename()
arch = csv_opener(path)
# El modulo terminaltables ayuda en el dibujo en la consola de tablas.
# Data almacena la información, cada [] representa una fila, y las comas son las columnas.
data = [['ID', 'Tamaño', 'T.Arribo', 'T.Irrupción']]
# Este while es demostrativo para testear al deque, que es un forma de decir "double-ended queue", con while me muevo por la lista que se carga de izq a der
# try rompe el bucle cuando arch se vacia, con proc almacenamos el elemento actual, popleft es una función del modulo que devuelve el valor del elemento a la izquierda de la lista
# A la vez que lo remueve. Usamos append para poder agregar a data los elementos de la tabla.
while arch:
    try:
        proc = arch.popleft()
        data.append([proc.id, proc.tam, proc.arribo, proc.irrup])
    except StopIteration:
        break
# AscciTable es uno de los posibles estilos, y es el más compatible pero menos estéticos. Inner_row_border agrega las separaciones;y print imprime la tabla.
table = AsciiTable(data)
table.title = 'Procesos'
table.inner_row_border = True
print(table.table)
