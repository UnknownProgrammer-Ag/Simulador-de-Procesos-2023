# Módulo encargado de manejar el proceso elegido de la cola de listo, cargado en memoria
class Procesador:
    def __init__(self):
        self.proceso = None
        self.particion = 0
        self.tIProceso = 0

    def __str__(self):
        return f"Proceso {self.proceso.id} está ejecutandose\n"
    def cargar(self, proceso,particion,tIProceso):
        self.proceso = proceso
        self.particion = particion
        self.tIProceso = tIProceso
        self.proceso.actEstado(4)

cPU = Procesador()
