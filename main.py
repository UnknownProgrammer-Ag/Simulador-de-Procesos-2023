from procesos_csv import csv_opener
from terminaltables import AsciiTable
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()


def simulador(self):
    path = filedialog.askopenfilename()
    arch = csv_opener(path)
