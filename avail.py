class Avail:
    def __init__(self):
        self.contador = 0
        self.listaTemporales = []

    def generarTemporalNuevo(self, tipo):
        self.contador += 1
        arrTemporales = ('t'+str(self.contador), tipo)
        self.listaTemporales.append(arrTemporales)
        return arrTemporales