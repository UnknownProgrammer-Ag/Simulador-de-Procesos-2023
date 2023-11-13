from terminaltables import AsciiTable


class OutPut:
    def __init__(self, id, tA, tI, tFin):
        self.id = id
        self.tI = tI
        self.tA = tA
        self.tFin = tFin

    def tiempos(self):
        self.retorno = self.tFin-self.tA
        self.espera = self.retorno - self.tI


class Salidas:
    def __init__(self, total):
        self.total = total

    def estado_procesador(self, proc, estado):
        print(f"Actualmente el proceso {proc} tiene el estado {estado}")

    def estado_procesador(self):
        print("Actualmente el procesador se encuentra desocupado")

    def tabla_memoria(self):
        data = [['ID Part', 'Dir. Comienzo', 'Tamaño', 'IdProc', 'Fragment']]
        for part in memoria_principal.particiones:
            data.append([part.idpart, part.dir, part.tam,
                        part.proceso.id, part.fragmInt])
        table = AsciiTable(data)
        table.title = 'Tabla de Memoria'
        table.inner_row_border = True
        print(table.table)

    def mostrar_listos(self, cola):
        print("El estado de la cola de listos es la siguiente:\n")

    def estadistico(self, lista):
        self.lista = lista
        est = [['ID Proceso', 'T_Fin', 'T_Retorno', 'T_Espera']]
        for element in self.lista:
            ret += element.retorno
            wait += element.espera
            est.append([element.id, element.tFin,
                       element.retorno, element.espera])
        estable = AsciiTable(est)
        estable.title = 'Informe Final'
        estable.inner_row_border = True
        print(estable.table)
        print(
            f"Promedios:\n Tiempo de Retorno:{ret/self.total}\t\tTiempo de Espera:{wait/self.total}")
