from glob import glob
from pprint import pprint
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

def ejecutar_maquina_virtual(directorioProcedimientos: Directorio, constantes: Constantes, cuadruplos: Cuadruplos):
    print('Ejecutando máquina virtual: ')
    print("")
    #saltosPendientes.append(len(cuadruplos)-1)
    global _directorioProc
    _directorioProc = directorioProcedimientos
    apuntadorInstrucciones = 0
    for idConst, dataConstante in constantes.items():
        guardarEnMemoria(dataConstante["direccionVirtual"], idConst, dataConstante["tipoConstante"])
    print("Cuádruplos: ")
    i=1
    for cuadruplo in cuadruplos.listaCuadruplos:
        print(f'{i}: {cuadruplo}')
        i+=1;
    print("")
    while cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] != "End":
        global memoriaLocal
        if cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "=":
            print("Asignación:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
        if cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "print":
            print("Escritura:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
        if cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "read":
            print("Lectura:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "+":
            print("Suma:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "-":
            print("Resta:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "*":
            print("Multiplicación:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "/":
            print("División:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == ">":
            print("Mayor que:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == ">=":
            print("Mayor igual que:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "<":
            print("Menor que:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "<=":
            print("Menor igual que:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "==":
            print("Equivalente a:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "<>":
            print("Diferente de:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "&&":
            print("And:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "||":
            print("Or:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
        apuntadorInstrucciones+=1
    print("")
    print("Memoria global en la máquina virtual: ")
    pprint(memoriaGlobal.memoria)

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
