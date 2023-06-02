class Directorio:
    def __init__(self):
        self.tabla = {}
        self.tipo = None

    def contextoGlobal(self):
        self.tabla = {}
        self.tabla["global"] = {
            "Tipo de la funcion": "void", "Tabla de variables": {}
        }

    def agregarVariables(self, variable, tipo, nombreFuncion):
        if variable in self.tabla[nombreFuncion]["Tabla de variables"].keys():
            print('La variable '+ variable + "ya existe, porfavor renombrala")
        else:
            self.tabla[nombreFuncion]["Tabla de variables"][variable] = tipo

    def quitarVariable(self, variable, nombreFuncion):
        self.tabla[nombreFuncion]["Tabla de variables"].pop(variable)
    
    def existeVariable(self, variable, nombreFuncion):
        if variable in self.tabla[nombreFuncion]["Tabla de variables"].keys():
            return True
        else:
            return False
            
    def agregarFuncion(self, nombreFuncion, tipoFuncion):
        self.tabla[nombreFuncion] = {
            "Tipo de la funcion": tipoFuncion, "Tabla de variables": {}, "Lista de parámetros": []
        }

    def agregarParametros(self, tipoParametro, nombreFuncion):
        self.tabla[nombreFuncion]["Lista de parámetros"].append(tipoParametro)

    