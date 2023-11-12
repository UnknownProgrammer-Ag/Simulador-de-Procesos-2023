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

    def cargar(self, proceso):
        self.proceso = proceso
        self.fragmInt = self.tam - self.proceso.tam
        self.ocupado = 1

    def descargar(self):
        self.proceso = None
        self.fragmInt = 0
        self.ocupado = 0


class Memoria:
    def __init__(self, particiones):
        self.particiones = particiones
        self.ocupadas = 0

    def best_Fit(self, proceso):
        mejor_ajuste = None

        for particion in self.particiones:
            if not particion.idpart == 0:
                if not particion.ocupado and particion.tam >= proceso.tam:
                    if mejor_ajuste is None or particion.tam < mejor_ajuste.tam:
                        mejor_ajuste = particion

        if mejor_ajuste is not None:
            mejor_ajuste.cargar(proceso)
            print(
                f"Proceso {proceso.id} asignado a la partición {mejor_ajuste.idpart}.")
            self.ocupadas += 1
            mejor_ajuste.proceso.estado = 'Listos'
            return True
        else:
            print(
                f"Proceso {proceso.id} no se pudo asignar a ninguna partición de memoria.")
            return False


# Crear particiones de memoria
particiones = [
    Particion(0, '000', 100),
    Particion(1, '100', 250),
    Particion(2, '350', 120),
    Particion(3, '470', 60)
]
# Crear una instancia de Memoria
memoria_principal = Memoria(particiones)
