import csv

class Proceso:
    def __init__(self, id, tam, tA, tI):
        self.id = id
        self.tam = tam
        self.tA = tA
        self.tI = tI
        self.estado = 0  #0: Nuevo| 1: Listos| 2:Listos/Suspendidos| 3: Terminado|
        self.tFin = 0  #Tiempo en que el proceso termina

    def __str__(self):
        return f"{self.id} {self.tam} {self.tA} {self.tI}"

    def actEstado(self,estado):
        self.estado = estado

    def tiempos(self):
        self.retorno = self.tFin - self.tA
        self.espera = self.retorno - self.tI


def csv_opener(direc):
    file = open(direc, newline='')
    reader = csv.reader(file)
    next(reader) # Adelanta el cabezal del csv
    arch_procesos = []
    for row in reader:
        if int(row[1]<=250):
            proc = Proceso(int(row[0]), int(row[1]), int(row[2]), int(row[3]))
            arch_procesos.append(proc)
        else:
            print (f'El proceso {row[0]} supera el tamaño máximo de partición')
            print("Corrija este error, por ahora el proceso se pasara de largo")
    return arch_procesos




