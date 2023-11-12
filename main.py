# Importar modulos separados del simulador
from procesos_csv import csv_opener
from memoria import Memoria, memoria_principal
from procesador import Procesador, CPU
# Importar modulos de Python para facilitar implementación
import tkinter as tk
from tkinter import filedialog
from time import sleep
from collections import deque
from terminaltables import AsciiTable

root = tk.Tk()
root.withdraw()


def simulador(arch):
    tiempo_total = 0
    nuevos = deque()
    listos = deque()
    while True:
        # Cargar Cola de Nuevos mientras exista contenido en arch
        while arch:
            temp = arch.popleft()
            if temp.arribo == tiempo_total:
                nuevos.append(temp)
            else:
                arch.appendleft(temp)
                list(nuevos)
                break
        # Cargar Listos si la memoria no esta ocupada -> Mantener Multiprogramación de 5
        while len(listos) < 5:
            if nuevos:
                temp = nuevos.popleft()
                temp.estado = 'Listos / Suspendidos'
                listos.append(temp)
                cant += 1  # Contar cantidad de elementos nuevos cargados a listos
            else:
                list(listos)
                break
        listos.rotate(cant)

        # Cargar Particiones
        while (memoria_principal.ocupadas != 3):
            temp = listos.popleft()
            if memoria_principal.best_Fit(temp):
                temp.estado = 'Listos'
            listos.append(temp)
        list(listos)

        # Cargar Procesador
        if not CPU.ocupado:
            # Simple Variable para obtener menor ID (presuntamente el proceso que debe ingresar)
            min = 11  # SE sabe que hay un maximo de 10 procesos
            for part in memoria_principal:
                if part.proceso.id < min:
                    min = part.proceso.id
                    temp = part.proceso

            CPU.cargar(temp)

        CPU.procesar()
        tiempo_total += 1
        if CPU.proceso.irrup == 0:
            print(f"Proceso {CPU.proceso.id} termino...")
        else:
            if CPU.quantum == 0:
                # Actualizacion de Procesos
                for part in memoria_principal:
                    if part.proceso.id == CPU.proceso.id:
                        part.proceso.irrup = CPU.proceso.irrup
                        loc = listos.index(CPU.proceso)
                        listos[loc].irrup = CPU.proceso.irrup
                        if len(listos) > 3:
                            part.descargar()

                CPU.reiniciar_q()

        if not nuevos and not listos and not arch and not memoria_principal.particiones and not CPU.ocupado:
            break
        else:
            continue

    data = [['ID Part', 'Dir. Comienzo', 'Tamaño', 'IdProc', 'Fragment']]
    for part in memoria_principal.particiones:
        data.append([part.idpart, part.dir, part.tam,
                    part.proceso.id, part.fragmInt])
    table = AsciiTable(data)
    table.title = 'Tabla de Memoria'
    table.inner_row_border = True
    print(table.table)


# Principal
print("Bienvenido a Simulador ROUND ROBIN de Procesos")
print("Ahora, para iniciar el simulador ingrese el archivo CSV que contendrá los procesos")
sleep(2)
path = filedialog.askopenfilename(title="Seleccionar Archivo CSV", filetypes=[
                                  ("Archivo csv", "*.csv"), ("Todos los archivos", "*.*")])
arch = csv_opener(path)

# Llamada al Simulador
if arch != None:
    simulador(arch)
else:
    print("El archivo csv estaba vacío o fallo en cargar")
