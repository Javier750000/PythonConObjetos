class Constantes:
    def __init__(self):
        self.table = {'int': {}, 'float': {}, 'char': {}, 'bool': {}}

    def agregarConstante(self, tipo, constante, direccion):
        self.table[tipo][constante] = direccion

    def existeConstante(self, tipo, constante):
        return constante in self.table[tipo].keys()

    def direccionConstante(self, tipo, constante):
        return self.table[tipo][constante]
