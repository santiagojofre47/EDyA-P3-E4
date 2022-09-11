class Designacion:
    __anio = None
    __tipo_justicia = None
    __tipo_cargo = None
    __tipo_instancia = None
    __materia = None
    __cant_varones = None
    __cant_mujeres = None

    def __init__(self, anio, tipo_justicia, tipo_cargo, tipo_instancia, materia, cant_varones, cant_mujeres):
        assert tipo_justicia == 'Nacional' or tipo_justicia == 'Federal'
        self.__anio = anio
        self.__tipo_justicia = tipo_justicia
        self.__tipo_cargo = tipo_cargo
        self.__tipo_instancia = tipo_instancia
        self.__materia = materia
        self.__cant_varones = cant_varones
        self.__cant_mujeres = cant_mujeres
    
    def __str__(self):
        return 'Anio designacion: {} Tipo: {} Cargo: {} Instancia: {} Materia: {} cantidad de varones: {} cantidad de mujeres: {}'.format(self.__anio,self.__tipo_justicia, self.__tipo_cargo, self.__tipo_instancia, self.__materia, self.__cant_varones, self.__cant_mujeres)
    
    def getCantidadMujeres(self):
        return self.__cant_mujeres
    
    def getCantidadVarones(self):
        return self.__cant_varones
    
    def getTipoCargo(self):
        return self.__tipo_cargo
    
    def getAnio(self):
        return self.__anio
    
    def getMateria(self):
        return self.__materia
    