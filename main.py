# Importar modulos separados del simulador
from procesos_csv import csv_opener
from memoria import Memoria, memoria_principal
from procesador import Procesador, CPU
from salidas import Salidas, OutPut
# Importar modulos de Python para facilitar implementación
import tkinter as tk
from tkinter import filedialog
from time import sleep
from collections import deque

root = tk.Tk()
root.withdraw()


def simulador(arch):
    tiempo_total = 0
    lista_sal = []
    nuevos = deque()
    listos = deque()
    contProc = 0
    sal = Salidas(len(arch))
    while True:
        # Cargar Cola de Nuevos mientras exista contenido en arch
        while arch:
            temp = arch.popleft()
            if temp.arribo == tiempo_total:
                nuevos.append(temp)
            else:
                arch.appendleft(temp)
                if tiempo_total == 0:
                    sal.estado_procesador()
                else:
                    sal.estado_procesador(CPU.proceso.id, CPU.proceso.estado)

                sal.tabla_memoria()
                sal.mostrar_listos()

                while True:
                    user = input("Ingrese Enter para Continuar...")
                    if user == "":
                        print("Continuando...")
                        sleep(1)
                        break
                    else:
                        print("Debe ser enter para continuar...")
        # Cargar Listos si la memoria no esta ocupada -> Mantener Multiprogramación de 5
        while contProc < 5:
            if nuevos:
                temp = nuevos.popleft()
                temp.estado = 'Listos / Suspendidos'
                listos.append(temp)
                contProc += 1
            else:
                list(listos)
                break
        # Cargar Particiones
        while (memoria_principal.ocupadas != 3):
            if listos:
                temp = listos.popleft()

                if not memoria_principal.best_Fit(temp):
                    listos.append(temp)
                    # Quiere decir que no hay particion en este momento que aloje al tamaño, pero si hay disponible
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

            item = OutPut(CPU.proceso.id, CPU.proceso.arribo,
                          CPU.proceso.resgirrup, tiempo_total)
            lista_sal.append(item)
            for part in memoria_principal:

                if part.proceso.irrup == CPU.proceso.id:
                    part.descargar()
            CPU.reiniciar_q()

            sal.estado_procesador()
            sal.tabla_memoria()
            sal.mostrar_listos()
            while True:

                user = input("Ingrese Enter para Continuar...")
                if user == "":
                    print("Continuando...")

                    sleep(1)
                    break
                else:
                    print("Debe ser enter para continuar...")
            contProc -= 1
        else:
            if CPU.quantum == 0:
                # Actualizacion de Procesos
                for part in memoria_principal:
                    if part.proceso.id == CPU.proceso.id:
                        part.proceso.irrup = CPU.proceso.irrup
                        if contProc > 3 and memoria_principal.ocupadas == 3:
                            temp = part.descargar()
                            temp.estado = 'Listos/Suspendidos'
                            listos.append(temp)
                CPU.reiniciar_q()


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
