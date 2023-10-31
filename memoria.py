# Memoria es el módulo encargado de manejar las particiones y la política de asignación establecida.

# Particiones
class Particion:
    def __init__(self, idpart, dir, tam):
        self.idpart = idpart
        self.dir = dir
        self.tam = tam
        self.fragmInt = 0
        self.ocupado = 0

    def cargar(self, idproc, tamProc):
        self.idproc = idproc
        self.fragmInt = self.tam - tamProc
        self.ocupado = 1


memoria_Principal = [
    Particion(0, '000', 105),
    Particion(1, '100', 250),
    Particion(2, '350', 120),
    Particion(3, '470', 60)
]
