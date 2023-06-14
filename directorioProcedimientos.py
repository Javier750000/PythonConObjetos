class Directorio:
    def __init__(self):
        self.tabla = {}
        self.tipo = None
        self.contadorParametros = 0
        self.contadorLocales = {'int': 0, 'float': 0, 'char': 0, 'bool': 0}
        self.contador = 0
        self.temporales = {}

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

    def agregarCantidadParametros(self, nombreFuncion):
        self.tabla[nombreFuncion]["cantidadParametros"] = len(self.tabla[nombreFuncion]["listaParametros"].keys())

    def actualizarContadorLocales(self, tipo):
        self.contadorLocales[tipo] += 1

    def reinicializarContadorLocales(self):
        self.contadorLocales['int'] = 0
        self.contadorLocales['float'] = 0
        self.contadorLocales['char'] = 0
        self.contadorLocales['bool'] = 0
