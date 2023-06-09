class Directorio:
    def __init__(self):
        self.tabla = {}
        self.tipo = None

    def contextoGlobal(self):
        self.tabla = {}
        self.tabla["global"] = {
            "tipoFuncion": "void", "tablaVariables": {}
        }

    def agregarVariables(self, variable, tipo, nombreFuncion):
        if variable in self.tabla[nombreFuncion]["tablaVariables"].keys():
            raise Exception("La variable «"+ variable + "» ya existe. Favor de renombrala.")
        else:
            self.tabla[nombreFuncion]["tablaVariables"][variable] = tipo
            
    def agregarFuncion(self, nombreFuncion, tipoFuncion):
        if nombreFuncion in self.tabla.keys():
            raise Exception("La función «"+ nombreFuncion + "» ya existe. Favor de renombrala.")
        else:
            self.tabla[nombreFuncion] = {
                "tipoFuncion": tipoFuncion, "tablaVariables": {}, "listaParametros": {}
            }

    def agregarParametros(self, nombreParametro, tipoParametro, nombreFuncion):
        if nombreParametro in self.tabla[nombreFuncion]["listaParametros"].keys():
            raise Exception("La función «"+ nombreFuncion + "» ya tiene declarado un parámetro con nombre " + nombreParametro + ". Favor de renombrarlo.")
        else:
            self.tabla[nombreFuncion]["listaParametros"][nombreParametro] = tipoParametro
