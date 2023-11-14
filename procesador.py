# Módulo encargado de manejar el proceso elegido de la cola de listo, cargado en memoria
# El módulo maneja el quantum y maneja el avance del tiempo total a su vez.
from memoria import memoria_principal
from collections import deque

class Procesador:
    def __init__(self):
        self.proceso = None
        self.ocupado = 0
        self.quantum = 2
        self.lista_prioridad = deque()

    def cargar(self, proceso):
        self.proceso = proceso
        self.proceso.estado = 'En Ejecución'
        self.ocupado = 1

    def procesar(self):
        self.quantum -= 1
        self.proceso.irrup -= 1

    def reiniciar_q(self):
        self.quantum = 2
        self.ocupado = 0
        self.proceso = None

    def buscar_proceso(self):
        if not self.ocupado:
            # Simple Variable para obtener menor ID (presuntamente el proceso que debe ingresar)
            min = 11  # SE sabe que hay un maximo de 10 procesos
            for part in memoria_principal.particiones:
                if part.proceso != None:
                    if part.proceso.id < min and part.proceso.id == self.lista_prioridad[0].id:
                        min = part.proceso.id
                        temp = part.proceso
                else:
                    continue
            self.cargar(temp)

cPU = Procesador()
