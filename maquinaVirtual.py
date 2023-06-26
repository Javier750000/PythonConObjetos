from glob import glob
import pprint
from constantes import Constantes
from directorioProcedimientos import Directorio
from cuadruplos import Cuadruplos

class MaquinaVirtual:

    def __init__(self, _id):
        self.memoria = {}
        self.id = _id

    def insertar(self, dir, valor, tipo):
        self.memoria[dir] = {"valor": valor, "tipo": tipo}


global memoriaLocal
memoriaLocal = MaquinaVirtual(None)
memoriaGlobal = MaquinaVirtual("global")
saltosPendientes = []


def ejecutar_maquina_virtual(directorioProcedimientos: Directorio, constantes: Constantes,cuadruplos: Cuadruplos):
    print('""""""""""""""""""""""""""""""""""""""""""""""""""""""')
    print('""""""""""""""""""""""""""""""""""""""""""""""""""""""')
    print('""""""""""""""""""""""""""""""""""""""""""""""""""""""')
    print('""""""""""""""""""""""""""""""""""""""""""""""""""""""')
    print('""""""""""""""""""""""""""""""""""""""""""""""""""""""')
    print('""""""""""""""""""""""""""""""""""""""""""""""""""""""')
    print('Ejecutando maquina virtual')
    #saltosPendientes.append(len(cuadruplos)-1)

    global _directorioProc
    _directorioProc = directorioProcedimientos

    apuntadorInstrucciones = 0

    for idConst, dataConstante in constantes.items():
        guardarEnMemoria(dataConstante["direccionVirtual"],idConst,dataConstante["tipoConstante"])

    print("QUADS",cuadruplos.listaCuadruplos)


    
    while cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] != "End":
        global memoriaLocal

        if cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "=":
            print("ASIG",cuadruplos.listaCuadruplos[apuntadorInstrucciones])
            apuntadorInstrucciones+=1
        
        if cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "+":
            print("SUMA",cuadruplos.listaCuadruplos[apuntadorInstrucciones])
            apuntadorInstrucciones+=1
        
        if cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "-":
            print("RESTA",cuadruplos.listaCuadruplos[apuntadorInstrucciones])
            apuntadorInstrucciones+=1

        if cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "*":
            print("MULT",cuadruplos.listaCuadruplos[apuntadorInstrucciones])
            apuntadorInstrucciones+=1
        
        if cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "/":
            print("DIV",cuadruplos.listaCuadruplos[apuntadorInstrucciones])
            apuntadorInstrucciones+=1
        apuntadorInstrucciones+=1

    print("memoria global en maquina")
    print(memoriaGlobal.memoria)




def guardarEnMemoria(dir, valor, tipo):
    global memoriaLocalActual
    if esVariableGlobal(dir):
        memoriaGlobal.insertar(dir, valor, tipo)
    else:
        memoriaLocal.insertar(dir, valor, tipo)

def esVariableGlobal(dir):
    if (dir >= 0 and dir <= 11999) or (dir >= 36000 and dir <= 47999):
        return True
    return False


# def extraerValorPorDir(dir, noAsignada=True):
#     global memoriaLocal

#     try:
#         if noAsignada:
#             if esVariableGlobal(dir):
#                 if