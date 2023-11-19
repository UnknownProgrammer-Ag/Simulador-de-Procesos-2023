from terminaltables import AsciiTable
from memoria import memoria_principal

class Salidas:
    def __init__(self):
        self.total = total
        self.ret = 0
        self.wait = 0
    def estado_procesador(self,proc):
        if proc != None:
            print(f"Actualmente el proceso {proc.id} tiene el estado {proc.estado}\n")
        else:
            print("Actualmente el procesador esta desocupado")
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


    def mostrar_listos(self, cola):
        print("El estado de la cola de listos es la siguiente:\n")
        if cola:
            for proceso in cola:
                if proceso.estado == 'Listo':
                    print(f"Proceso ID: {proceso.id}, Estado: {proceso.estado}")
            print("\n")
        else:
            print("La cola actualmente esta vacía")

    def estadistico(self, lista):
        self.lista = lista
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
            f"\nPromedios:\n Tiempo de Retorno:{self.ret/self.total}\t\tTiempo de Espera:{self.wait/self.total}")
