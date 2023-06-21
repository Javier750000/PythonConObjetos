class Constantes:
    def __init__(self):
        self.tabla = {}

    def agregarConstante(self, constante, tipo, dirV):
        self.tabla[constante] = {
            "tipoConstante": tipo, "direccionVirtual": dirV
        }
