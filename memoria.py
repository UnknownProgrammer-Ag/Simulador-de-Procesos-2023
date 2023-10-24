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

memoria=[]
part0=Particiones(0,0,100,0,1)
part1=Particiones(1,100000,250,0,0)
part2=Particiones(2,350000,120,0,0)
part3=Particiones(3,470000,60,0,0)
memoria.append(part0)
memoria.append(part1)
memoria.append(part2)
memoria.append(part3)
