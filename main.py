#Librerias y Modulos necesarios para iniciar el programa
from procesos_csv import csv_opener
from simulador import
import tkinter as tk
from tkinter import filedialog
from time import sleep

root = tk.Tk()
root.withdraw()
#-------------------------------------------------------------------------------------
    while True:



        # Cargar Listos si la memoria no esta ocupada -> Mantener Multiprogramación de 5

        # Cargar Particiones
        # PENSAR MEJOR MANERA DE IMPLEMENTAR resguardo de listos, FUNCIONA RECORRIDO DE COLA E INTENTO
        intento = 0
        while (memoria_principal.ocupadas != 3):
            if listos and (intento <= len(listos)):
                temp = listos.popleft()

                if not memoria_principal.best_Fit(temp):
                    intento += 1
                    print(f"Intento {intento} y Proceso Actual {temp.id}")
                    # Esto va a evitar un bucle infinito, de manera que si intento supera la cantidad de procesos en listos salga
                    listos.append(temp)
                    # Quiere decir que no hay particion en este momento que aloje al tamaño, pero si hay disponible
                else:
                    resg_Listos.append(temp)
                    cPU.lista_prioridad.append(temp)
            else:
                break




        # REVISAR PROCESADOR COMPLETO, ERRORES GARRAFALES PRIORIDAD ALTA
        # Cargar Procesador en Tiempo=0
        if tiempo_total == 0:
            cPU.buscar_proceso()

        # -> Pensar en la estructura manejada por contador un for que represente el quantum de 2, y susodichas consecuencias.
        cPU.procesar()
        # REVISAR TODA LA ESTRUCTURA DE ESTA SECCION
        if cPU.proceso.irrup == 0:
            print(f"Proceso {cPU.proceso.id} termino...")

            item = OutPut(cPU.proceso.id, cPU.proceso.arribo,
                          cPU.proceso.resgirrup, tiempo_total)
            lista_sal.append(item)
            for part in memoria_principal.particiones:
                if part.proceso != None:
                    if part.proceso.irrup == cPU.proceso.id:
                        cPU.lista_prioridad.remove(part.proceso)
                        part.descargar()
                        memoria_principal.ocupadas -= 1
                        resg_Listos = [
                            item for item in resg_Listos if item.id != cPU.proceso.id]
            cPU.reiniciar_q()
            cPU.buscar_proceso()

            print(f"Tiempo Actual: {tiempo_total}\n")
            sal.estado_procesador(cPU.proceso)
            sal.tabla_memoria()
            sal.mostrar_listos(resg_Listos)
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
            if cPU.quantum == 0:
                # Actualizacion de Procesos
                for part in memoria_principal.particiones:
                    if part.proceso != None:
                        if part.proceso.id == cPU.proceso.id:
                            part.proceso.irrup = cPU.proceso.irrup
                            part.proceso.estado = 'Listo'
                            if contProc > 3 and memoria_principal.ocupadas == 3 and part.tam >= listos[0].tam:
                                temp = part.descargar()
                                memoria_principal.ocupadas -= 1
                                temp.estado = 'Listos/Suspendidos'
                                listos.append(temp)
                                resg_Listos = [
                                    item for item in resg_Listos if item.id != temp.id]
                                cPU.lista_prioridad.remove(temp)
                cPU.lista_prioridad.rotate(-1)
                cPU.reiniciar_q()
                cPU.buscar_proceso()
        # MOSTRAR SALIDAS A NUEVO PROCESO
        if band_nuevos:
            print(f"Tiempo Actual: {tiempo_total}\n")
            sal.estado_procesador(cPU.proceso)
            sal.tabla_memoria()
            sal.mostrar_listos(resg_Listos)
            while True:
                user = input("Ingrese Enter para Continuar...")
                if user == "":
                    print("Continuando...")
                    sleep(1)
                    band_nuevos = False
                    break
                else:
                    print("Debe ser enter para continuar...")

        tiempo_total += 1
        # Finalizar Simulador
        if not arch:
            if not nuevos:
                if not listos:
                    if memoria_principal.ocupadas == 0:
                        if not cPU.ocupado:
                            break
    sal.estadistico(lista_sal)

# Principal
print("Bienvenido a Simulador ROUND ROBIN de Procesos")
print("Ahora, para iniciar el simulador ingrese el archivo CSV que contendrá los procesos")
sleep(2)
path = filedialog.askopenfilename(title="Seleccionar Archivo CSV", filetypes=[
                                  ("Archivo csv", "*.csv"), ("Todos los archivos", "*.*")])
procesos = csv_opener(path) #Lista de Todos los procesos
# Llamada al Simulador
if procesos != None:
    (procesos)
else:
    print("El archivo csv estaba vacío o fallo en cargar")
