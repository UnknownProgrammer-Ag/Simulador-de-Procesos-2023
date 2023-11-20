# Importar modulos separados del simulador
from memoria import memoria_principal
from procesador import cPU
from salidas import sal
from time import sleep
from collections import deque

class Simulador:
    def __init__(self):
        # Elementos basicos del simulador
        self.procesos = None
        self.tiempo_total = 0
        self.quantum = 0

        # Estructuras principales en el manejo de procesos
        self.nuevos = []
        self.listos5 = deque()  # Solo puede contener 5 procesos
        self.terminados = []
        self.listaPrioridad = deque()

        # Banderas que marcan las salidas
        self.bandListo = False
        self.bandTerminado = False
        self.bandNuevo = False

    def cargarArch(self,procesos):
        self.procesos = procesos

    def colaNuevos(self):
        self.bandNuevo = False
        for i in range(len(self.procesos)):
            if (self.procesos[i].tA == self.tiempo_total):
                self.nuevos.append(self.procesos[i])
                print(f"Proceso Nuevo: {self.procesos[i]}")
                self.bandNuevo = True  # Marca que n procesos entraron al sistema

    def colaListos(self):
        self.bandListo = False
        for i in range(len(self.nuevos)):
            if len(self.listos5) < 5:
                self.nuevos[0].actEstado(2)  # Cambia a Listos/Suspendidos
                self.listos5.append(self.nuevos.pop(0))
                self.bandListo = True  # Uno o màs procesos entraron a listos
        list(self.listos5)

    def cargarBestFit(self):
        n = 0
        print(f"Tamaño de Listos: {len(self.listos5)}")
        while True:
            # Mientras existan particiones vacias
            if memoria_principal.ocupadas <3:
                if self.listos5: #Si la cola de listos tiene procesos
                    if (len(self.listos5))>memoria_principal.ocupadas:
                        print(f"Valor de N: {n}")
                        if n<=((len(self.listos5))-1):
                            if self.listos5[n].id not in [part.proceso.id for part in memoria_principal.particiones if part.proceso != None]:
                                #Si el proceso en el tope no se encuentra ya en memoria
                                if memoria_principal.bestFit(self.listos5[n]):
                                    if (n == 0):
                                    #Si bestFit devuelve True se rota al final
                                        self.listos5.rotate(-1)
                                    else:
                                    # Se mantiene el valor que no entro en prioridad y mueve otro proceso encontrado
                                        print(f"Cola de listos Antes de Rotar:")
                                        for i in self.listos5:
                                            print(i)
                                        self.listos5.rotate(-n)
                                        temp = self.listos5.pop()
                                        self.listos5.rotate(n)
                                        print(f"Cola de listos despues de rotar:")
                                        for i in self.listos5:
                                            print(i)
                                        print("\n")
                                        self.listos5.append(temp)
                                else:
                                    n += 1
                            else:
                                self.listos5.rotate(-1)
                        else:
                            break
                    else:
                        break
                else:
                    break
            else:
                break

    def filtrarListos(self):
        # Funcion que va a utilizar la herramienta filtro para obtener los procesos que estan en memoria
        def estadosListos(proc):
            if (proc.estado == 1):
                return True
            else:
                return False
        # Verifica que no sea vacío
        if len(self.listos5) > 0:
            procMemoria = deque(filter(estadosListos, self.listos5))  # Filtro solo aquellos procesos con estado listos
        return procMemoria

    def cargarProcesador(self):
        if self.listaPrioridad is None: #Si esta vacia es por ser el inicio de la lista
            self.listaPrioridad=self.filtrarListos()
        else:
            temp = self.filtrarListos()
            if len(self.listaPrioridad) < len(temp): #Porque solo pueden llegar a existir 3 procesos listos y prioridad puede tener 2 o 1 menos.
                for i in temp:
                    if i not in self.listaPrioridad:
                        self.listaPrioridad.append(i)

        print("Lista de Prioridades:")
        for i in self.listaPrioridad:
            print(i)

        if (cPU.proceso == None): #Si el proceso esta desocupado se carga el proceso a tope de pila
            cPU.cargar(self.listaPrioridad[0],memoria_principal.obtPartID(self.listaPrioridad[0]),self.listaPrioridad[0].tIVar)
            cPU.proceso.actEstado(4)

    def procesamiento2Q(self):
        self.bandTerminado = False
        #Bandera para imprimir salidas
        if (cPU.proceso != None):
            print(f"\nAntes de procesar: Proceso: {cPU.proceso} Quantum: {self.quantum}  TIProceso: {cPU.tIProceso}")
            cPU.tIProceso -= 1
            self.quantum += 1
            print(f"Despues de procesar: Proceso: {cPU.proceso} Quantum: {self.quantum}  TIProceso: {cPU.tIProceso}")
            if (cPU.tIProceso == 0):
                #Actualizacion de Proceso
                self.bandTerminado = True
                print (f"Proceso {cPU.proceso.id} termino...")
                cPU.proceso.actEstado(3)
                cPU.proceso.fin(self.tiempo_total)
                cPU.proceso.tIVariable(cPU.tIProceso)
                cPU.proceso.tiempos()
                #Eliminación del Sistema
                memoria_principal.particiones[cPU.particion].modificarPart(None,0,0)
                memoria_principal.ocupadas -= 1
                self.listos5.remove(cPU.proceso)
                self.terminados.append(cPU.proceso)
                self.listaPrioridad.remove(cPU.proceso)
                cPU.cargar(None,0,0)
                self.quantum = 0
            else:
                if (self.quantum == 2):
                    #Si Quantum es el que termino y no el proceso
                    #Actualizo valores del proceso
                    cPU.proceso.actEstado(1)
                    cPU.proceso.tIVariable(cPU.tIProceso)
                    if (memoria_principal.ocupadas == 3 and memoria_principal.particiones[cPU.particion].tam >= self.listos5[0].tam):
                    #Si la memoria esta ocupada y la particion puede alojar al proceso en el tope de pila
                        cPU.proceso.actEstado(2)
                        memoria_principal.particiones[cPU.particion].modificarPart(None,0,0)
                        memoria_principal.ocupadas -= 1
                        self.listaPrioridad.remove(cPU.proceso)
                    else:
                        self.listaPrioridad.rotate(-1)

                    cPU.cargar(None,0,0)
                    self.quantum = 0
            print("Lista de Prioridades:")
            for i in self.listaPrioridad:
                print(i)

    def imprimirSalidas(self):
        if (self.bandListo or self.bandNuevo or self.bandTerminado):
            print(f"\nTiempo actual: {self.tiempo_total}")

            if cPU.proceso != None:
                print(cPU)
            else:
                print("Actualmente el procesador esta desocupado")

            print(f"Estado de Cola de Listos: ")
            for particion in memoria_principal.particiones:
                if (particion.proceso != None) and (particion.proceso != cPU.proceso):
                    print(particion.proceso)
            print("\n")
            sal.tabla_memoria()

            while True:
                user = input("Ingrese Enter para Continuar...")
                if user == "":
                    print("Continuando...")
                    sleep(1)
                    band_nuevos = False
                    break
                else:
                    print("Debe ser enter para continuar...")

    def programa(self):
        self.colaNuevos()
        self.colaListos()
        self.cargarBestFit()
        self.cargarProcesador()
        self.procesamiento2Q()
        self.imprimirSalidas()
        self.tiempo_total += 1
        while ((len(self.terminados)) != (len(self.procesos))):
            self.colaNuevos()
            self.colaListos()
            self.cargarBestFit()
            self.cargarProcesador()
            self.procesamiento2Q()
            self.imprimirSalidas()
            self.tiempo_total += 1

        print("\nSimulación Terminada...")
        print("\nCalculando Estadistica...")
        sal.cargarProcesos(self.procesos)
        sleep(1)
        sal.estadistico(self.terminados)
        input("\nPresione cualquier tecla para cerrar")

sim = Simulador()