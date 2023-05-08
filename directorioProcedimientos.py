class Directorio:
    def __init__(self):
        self.tabla = {}
        
    def contextoGlobal(self):
        self.tabla = {}
        self.tabla["global"] = {
            "Tipo de la funcion": "void", "Tabla de variables": {}
        }

    def agregarVariablesGlobales(self, variable):
        _, tipoVariable, contextoVariable, nombreVariable = variable
        self.tabla['global']['tablaVariables'][nombreVariable] = {
            'tipoVariable': tipoVariable, 'contextoVariable': contextoVariable
        }

    def agregarFuncion(self, nombreFuncion, tipoFuncion, variablesFuncion, parametrosFuncion=[]):
        
        self.tabla[nombreFuncion] = {
            "Tipo de la funcion": tipoFuncion, "Tabla de variables": {}
        }
        
        for parametro in parametrosFuncion:
            tipoVariable, contextoVariable, nombreVariable = parametro
            self.tabla[nombreFuncion]['tablaVariables'][nombreVariable] = {
                'tipoVariable' : tipoVariable, 'contextoVariable': contextoVariable
            }
        
        for variable in variablesFuncion:
            _, tipoVariable, contextoVariable, nombreVariable = variable
            self.tabla[nombreFuncion]['tablaVariables'][nombreVariable] = {
                'tipoVariable': tipoVariable, 'contextoVariable': contextoVariable
            }