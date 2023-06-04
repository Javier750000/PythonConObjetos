from directorioProcedimientos import Directorio

class DirectorioClases:
    def __init__(self):
        self.tablaClases = {}

    def add(self, id):
        self.tablaClases[id] = {}
    
    def exists(self, id):
        if id in self.tablaClases.keys():
            print('La clase '+ id +' ya existe')
            return True
        else: 
            return False

    def addAttributes(self, id, tablaVars):
        self.tablaClases[id]['atributos'] = tablaVars
    
    def addMethods(self, id, tablaFuncs):
        self.tablaClases[id]['atributos'] = tablaFuncs
        