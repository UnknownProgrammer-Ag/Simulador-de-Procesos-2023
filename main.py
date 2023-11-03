# Importar modulos separados del simulador
from procesos_csv import csv_opener
from memoria import Memoria,memoria_principal
# Importar modulos de Python para facilitar implementación
import tkinter as tk
from tkinter import filedialog
from time import sleep
from collections import deque
from terminaltables import AsciiTable

root = tk.Tk()
root.withdraw()

def simulador(arch):
    tiempo_total=0
    nuevos=deque()
    listos=deque()
    mult_P=0
    #while True:
    for i in range(5):
        #Cargar Cola de Nuevos
        temp = arch.popleft()
        if temp.arribo == tiempo_total:
            nuevos.append(temp)
        else:
            arch.appendleft(temp)

        #Cargar Listos --> Mantener Multiprogramación de 5
        while (nuevos):
            if (len(listos)<5):
                listos.append(nuevos.popleft())

        #Cargar Particiones
        while (memoria_principal.ocupadas!=3):
            temp = listos.popleft()
            memoria_principal.best_Fit(temp)

        data = [['ID Part','Dir. Comienzo','Tamaño', 'IdProc', 'Fragment']]
        for part in memoria_principal.particiones:
            data.append([part.idpart,part.dir,part.tam,part.idproc,part.fragmInt])
        table = AsciiTable(data)
        table.title = 'Tabla de Memoria'
        table.inner_row_border = True
        print(table.table)

        tiempo_total+=1




# Principal
print("Bienvenido a Simulador ROUND ROBIN de Procesos")
print("Ahora, para iniciar el simulador ingrese el archivo CSV que contendrá los procesos")
sleep(2)
path = filedialog.askopenfilename(title="Seleccionar Archivo CSV", filetypes=[("Archivo csv", "*.csv"), ("Todos los archivos", "*.*")])
arch = csv_opener(path)

# Llamada al Simulador
if arch != None:
    simulador(arch)
else:
    print("El archivo csv estaba vacío o fallo en cargar")
