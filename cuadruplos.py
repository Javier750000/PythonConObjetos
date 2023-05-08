class Cuadruplos:
    def __init__(self):
        self.contador = 0
        self.listaCuadruplos = []

    def generarCuadruploNuevo(self, operador, operandoIzq, operandoDer, resultado):
        cuadruplo = [operador, operandoIzq, operandoDer, resultado]
        self.listaCuadruplos.append(cuadruplo)
        self.contador += 1