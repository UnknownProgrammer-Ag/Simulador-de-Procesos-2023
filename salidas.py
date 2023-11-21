#Modulo encargado de las salidas por tablas
from terminaltables import AsciiTable
from memoria import memoria_principal

class Salidas:
    def __init__(self):
        self.total = None
        self.ret = 0
        self.wait = 0

    def cargarProcesos(self,proc):
        self.total = proc
    def tabla_memoria(self):
            data = [['ID Part', 'Dir. Comienzo', 'Tamaño', 'IdProc', 'Fragment']]
            for part in memoria_principal.particiones:
                if part.proceso != None:
                    data.append([part.idpart, part.dir, part.tam,part.proceso.id, part.fragmInt])
                else:
                    data.append([part.idpart, part.dir, part.tam,"----", part.fragmInt])
            table = AsciiTable(data)
            table.title = 'Tabla de Memoria'
            table.inner_row_border = True
            print(table.table)
            print("\n")

    def estadistico(self, lista):
        self.lista = lista
        self.lista.sort(key=lambda x: x.id,reverse = False)
        est = [['ID Proceso', 'T_Fin', 'T_Retorno', 'T_Espera']]
        for element in self.lista:
            self.ret += element.retorno
            self.wait += element.espera
            est.append([element.id, element.tFin,
                       element.retorno, element.espera])
        estable = AsciiTable(est)
        estable.title = 'Informe Final'
        estable.inner_row_border = True
        print(estable.table)
        print(
            f"\nPromedios:\n Tiempo de Retorno:{self.ret/len(self.total)}\t\tTiempo de Espera:{self.wait/len(self.total)}")


sal = Salidas()