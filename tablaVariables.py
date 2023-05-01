class tablaVariables(object):

    def __init__(self, contexto):
        self.contexto = contexto
        self.variables = {}

    def declararVariable(self, id, tipo):
        if id not in self.variables:
            self.variables[id] = (tipo, None)
        else:
            raise Exception("La variable " + id + " ha sido declarado varias veces en el contexto " + self.contexto + ".")

    def declararValor(self, id, valor):
        if id in self.variables:
            self.variables[id] = (self.variables[id][0], valor)
        else:
            raise Exception("La variable " + id + " no ha sido declarada en el contexto " + self.contexto + ".")

    def buscarVariable(self, id):
        if id in self.variables:
            return id
        else:
            raise Exception("La variable " + id + " no ha sido declarada en el contexto " + self.contexto + ".")
    
    def buscarTipo(self, id):
        if id in self.variables:
            return self.variables[id][0]
        else:
            raise Exception("La variable " + id + " no ha sido declarada en el contexto " + self.contexto + ".")
