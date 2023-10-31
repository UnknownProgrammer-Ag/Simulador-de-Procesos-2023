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

    def descargar(self):
        self.idproc = 0
        self.fragmInt = 0
        self.ocupado = 0
class Memoria:
    def __init__(self, particiones):
        self.particiones = particiones

    def best_Fit(self, proceso):
        mejor_ajuste = None

        for particion in self.particiones:
            if not particion.ocupado and particion.tam >= proceso.tam:
                if mejor_ajuste is None or particion.tam < mejor_ajuste.tam:
                    mejor_ajuste = particion

        if mejor_ajuste is not None:
            mejor_ajuste.cargar(proceso.id, proceso.tam)
            #Esto se debería eliminar o enlazar a otra parte del simulador
            print(f"Proceso {proceso.id} asignado a la partición {mejor_ajuste.idpart}.")
            return True
        #Esto deberia hacer que el proceso pase a la cola de listos devuelta
        print(f"Proceso {proceso.id} no se pudo asignar a ninguna partición de memoria.")
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




