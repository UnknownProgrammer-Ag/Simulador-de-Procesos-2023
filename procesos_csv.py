import csv
from collections import deque


class Proceso:
    def __init__(self, id, tam, tA, tI):
        self.id = id
        self.tam = tam
        self.arribo = tA
        self.irrup = tI
        self.resgirrup = tI
        self.estado = ' '


def csv_opener(direc):
    file = open(direc, newline='')
    reader = csv.reader(file)
    next(reader)
    arch_procesos = deque()
    for row in reader:
        proc = Proceso(int(row[0]), int(row[1]), int(row[2]), int(row[3]))
        arch_procesos.append(proc)
    return arch_procesos
