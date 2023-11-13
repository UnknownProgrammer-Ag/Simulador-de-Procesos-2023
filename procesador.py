# Módulo encargado de manejar el proceso elegido de la cola de listo, cargado en memoria
# El módulo maneja el quantum y maneja el avance del tiempo total a su vez.

class Procesador:
    def __init__(self):
        self.proceso = None
        self.ocupado = 0
        self.quantum = 2

    def cargar(self, proceso):
        self.proceso = proceso
        self.proceso.estado = 'En Ejecución'

    def procesar(self):
        self.quantum -= 1
        self.proceso.irrup -= 1

    def reiniciar_q(self):
        self.quantum = 2
        self.ocupado = 0
        self.proceso = None


cPU = Procesador()
