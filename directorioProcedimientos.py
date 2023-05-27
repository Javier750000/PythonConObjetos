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
        self.tabla[nombreFuncion]["Tabla de variables"][variable] = {
            "Tipo de la variable": tipo
        }

    def agregarFuncion(self, nombreFuncion, tipoFuncion):
        self.tabla[nombreFuncion] = {
            "Tipo de la funcion": tipoFuncion, "Tabla de variables": {}, "Lista de parámetros": []
        }

    def agregarParametros(self, tipoParametro, nombreFuncion):
        self.tabla[nombreFuncion]["Lista de parámetros"].append(tipoParametro)
