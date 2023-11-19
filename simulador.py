# Importar modulos separados del simulador
from memoria import memoria_principal
from procesador import cPU
from salidas import Salidas, OutPut

class Simulador:
    def __init__(self,procesos):
        #Elementos basicos del simulador
        self.procesos = procesos
        self.tiempo_total = 0

        #Estructuras principales en el manejo de procesos
        self.nuevos = []
        self.listos5 = []  # Solo puede contener 5 procesos
        self.terminados = []

        #Banderas que marcan las salidas
        self.bandListo = False
        self.bandTerminado = False
        self.bandNuevo = False
        self.sal = Salidas()

    def colaNuevos(self):
        self.bandNuevo = False
        for i in range(len(self.procesos)):
            if(self.procesos[i].tA == self.tiempo_total):
                    self.nuevos.append(self.procesos[i])
                    self.bandNuevo = True #Marca que n procesos entraron al sistema

    def colaListos(self):
        self.bandListo = False
        for i in range(len(self.nuevos)):
            if len(self.listos5)<5:
                self.nuevos[0].actEstado(2) #Cambia a Listos/Suspendidos
                self.listos5.append(self.nuevos.pop(0))
                self.bandListo = True #Uno o màs procesos entraron a listos

    def cargarBestFit(self):
        if memoria_principal.ocupadas != 3:
            for i in range(len(self.listos5[:3])):
                if self.listos5[i].id not in [particion.proceso.id for particion in memoria_principal.particiones if particion.proceso != None]:
                    memoria_principal.bestFit(self.listos5[i])


