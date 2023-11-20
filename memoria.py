# Memoria es el módulo encargado de manejar las particiones y la política de asignación establecida.

# Particiones
class Particion:
    def __init__(self, idpart, dir, tam):
        self.idpart = idpart
        self.dir = dir
        self.tam = tam
        self.fragmInt = 0
        self.ocupado = 0
        self.proceso = None

    def modificarPart(self,proceso,ocupado,fragmInt):
        self.proceso = proceso
        self.ocupado = ocupado
        self.fragmInt = fragmInt
        if self.ocupado:
            self.proceso.actEstado(1)

class Memoria:
    def __init__(self, particiones):
        self.particiones = particiones
        self.ocupadas = 0

    def bestFit(self, proceso):
        mejorAjuste = None

        for particion in self.particiones:
            if not particion.idpart == 0:
                if not particion.ocupado and particion.tam >= proceso.tam:
                    if mejorAjuste is None or particion.tam < mejorAjuste.tam:
                        mejorAjuste = particion

        if mejorAjuste is not None:
            mejorAjuste.modificarPart(proceso,1,mejorAjuste.tam-proceso.tam)
            self.ocupadas += 1
            return True
        else:
            return False

    def obtPartID(self,proc):
        for i in range(len(self.particiones)):
            if (self.particiones[i].idpart != 0 and self.particiones[i].proceso == proc):
                return i

# Crear particiones de memoria
particiones = [
    Particion(0, '000', 100),
    Particion(1, '100', 250),
    Particion(2, '350', 120),
    Particion(3, '470', 60)
]
# Crear una instancia de Memoria
memoria_principal = Memoria(particiones)
