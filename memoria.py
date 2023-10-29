class Particiones:
    def __init__(self, id, dir, tam, frag, restringida):
        self.id = id
        self.dir = dir
        self.tam = tam
        self.frag = frag
        self.restringida = restringida

    def cargar_particion(self, id, tam, fragm):
        self.idpart = id
        self.frag = self.tam-tam
        self.tam = tam
        self.ocupado = 1

    def descargar_particion(self):
        self.idpart = 0
        self.tam = self.tam + self.frag
        self.frag = 0
        self.ocupado = 0



