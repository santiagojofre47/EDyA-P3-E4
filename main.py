from manejadorDesignaciones import Manejador

if __name__ == '__main__':
    objManejador = Manejador()
    objManejador.cargar_datos()
    objManejador.mostrar_datos()
    tipo_cargo = input('Ingrese un tipo de cargo: ')
    objManejador.getMujeresPorCargo(tipo_cargo)
    tipo_cargo = input('Ingrese un tipo de cargo: ')
    materia = input('Ingrese una materia: ')
    anio = input('Ingrese un anio: ')
    objManejador.getCantidadAgentes(materia, tipo_cargo, anio)

