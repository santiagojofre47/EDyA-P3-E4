import csv
from claseListaPosicion import ListaEncadenada
from claseDesignacion import Designacion

class Manejador:
    __lista = None

    def __init__(self):
        self.__lista = ListaEncadenada()
    
    def cargar_datos(self):
        archivo = open('estadistica-designacion-magistrados-federal-nacional-por-genero-20220323.csv')
        reader = csv.reader(archivo, delimiter = ',')
        band = True
        i = 1
        for fila in reader:
            if band:
                band = False
            else:
                designacion = Designacion(fila[0], fila[1], fila[2], fila[3], fila[4], int(fila[5]), int(fila[6]))
                self.__lista.insertar(designacion,i)
                i+=1
        archivo.close()
    
    def mostrar_datos(self):
        self.__lista.recorrer()
    
    def getMujeresPorCargo(self,tipo_cargo):
        anio = 2000#año inicial
        cant_mujeres = 0
        encontro = False
        for i in range(self.__lista.getCantidadElementos()):
       
            objeto_designacion = self.__lista.recuperar(i)
            if objeto_designacion.getTipoCargo().lower() == tipo_cargo:
                encontro = True
                if i == 0:
                   anio = objeto_designacion.getAnio()
                
                if objeto_designacion.getAnio() == anio:
                    cant_mujeres+=objeto_designacion.getCantidadMujeres()
                else:
                    print('Cantidad de mujeres designadas en el cargo {} en el anio {}: {}'.format(tipo_cargo,anio,cant_mujeres))
                    cant_mujeres = objeto_designacion.getCantidadMujeres()
                    anio = objeto_designacion.getAnio()
            
            i+=1
        if not encontro:
            print('ERROR: No se encontro el cargo solicitado!')
    
    def getCantidadAgentes(self, materia, cargo, anio):
        i = 0
        cant_agentes = 0
        encontro = False
        for i in range(self.__lista.getCantidadElementos()):
            objeto_designacion = self.__lista.recuperar(i)
            if objeto_designacion.getAnio() == anio and objeto_designacion.getTipoCargo().lower() == cargo and objeto_designacion.getMateria().lower() == materia:
                encontro = True
                cant_agentes+= (objeto_designacion.getCantidadVarones())+(objeto_designacion.getCantidadMujeres())
        if encontro:
            print('Cantidad de agentes en el cargo {}, materia {} en el anio {}: {}'.format(cargo,materia,anio,cant_agentes))
        else:
            print('ERROR: No se encontraron agentes  con los datos ingresados!')