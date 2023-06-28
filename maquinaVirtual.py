import pprint
from constantes import Constantes
from directorioProcedimientos import Directorio
from cuadruplos import Cuadruplos

class MaquinaVirtual:

    def __init__(self, _id):
        self.memoria = {}
        self.id = _id

    def insertar(self, dir, valor):
        self.memoria[dir] = valor

    def obtenerValorPorDir(self, dir):
        return self.memoria[dir]


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
        guardarEnMemoria(dataConstante["direccionVirtual"],idConst)

    print("QUADS",cuadruplos.listaCuadruplos)


    
    while cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] != "End":
        global memoriaLocal

        if cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == '=':
            print("ASIG",cuadruplos.listaCuadruplos[apuntadorInstrucciones])
            valor = cuadruplos.listaCuadruplos[apuntadorInstrucciones][1]
            dir = cuadruplos.listaCuadruplos[apuntadorInstrucciones][3]
            print("direccion", dir)
            guardarEnMemoria(dir,valor)
            apuntadorInstrucciones+=1
        
        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "+":
            print("SUMA",cuadruplos.listaCuadruplos[apuntadorInstrucciones])
            leftDir = cuadruplos.listaCuadruplos[apuntadorInstrucciones][1]
            rightDir = cuadruplos.listaCuadruplos[apuntadorInstrucciones][2]
            res = cuadruplos.listaCuadruplos[apuntadorInstrucciones][3]
            print("MEMORIAGLOBAL",memoriaGlobal.memoria)
            print("MEMORIALOCAL",memoriaLocal.memoria)
            
            if leftDir in memoriaGlobal.memoria.keys():
                leftVal = memoriaGlobal.memoria[leftDir]

            if leftDir in memoriaLocal.memoria.keys():
                leftVal = memoriaLocal.memoria[leftDir]
            
            if rightDir in memoriaGlobal.memoria.keys():
                rightVal = memoriaGlobal.memoria[rightDir]
            
            if rightDir in memoriaLocal.memoria.keys():
                rightVal = memoriaLocal.memoria[rightDir]

            print("leftVal", leftVal)
            print("rightVal", rightVal)
            print("res", res)
            
            if type(leftVal) != str and leftVal in memoriaLocal.memoria.keys():
                leftVal = memoriaLocal.memoria[leftVal]
            
            if type(rightVal) != str and rightVal in memoriaLocal.memoria.keys():
                rightVal = memoriaLocal.memoria[rightVal]

            print("leftVal2", leftVal)
            print("rightVal2", rightVal)

            lFinal = convertirConstanteEnTipo(leftVal)
            rFinal = convertirConstanteEnTipo(rightVal)
            print("tipo lef",type(leftVal))
            print("tipo rig",type(rightVal))

            valor = lFinal + rFinal

            if type(valor) == float:
                valor = round(valor,10)
            print("VALOR", valor)
            guardarEnMemoria(res, valor)
            apuntadorInstrucciones += 1
        
        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "-":
            print("RESTA",cuadruplos.listaCuadruplos[apuntadorInstrucciones])
            leftDir = cuadruplos.listaCuadruplos[apuntadorInstrucciones][1]
            rightDir = cuadruplos.listaCuadruplos[apuntadorInstrucciones][2]
            res = cuadruplos.listaCuadruplos[apuntadorInstrucciones][3]
            print("MEMORIAGLOBAL",memoriaGlobal.memoria)
            print("MEMORIALOCAL",memoriaLocal.memoria)
            
            if leftDir in memoriaGlobal.memoria.keys():
                leftVal = memoriaGlobal.memoria[leftDir]

            if leftDir in memoriaLocal.memoria.keys():
                leftVal = memoriaLocal.memoria[leftDir]
            
            if rightDir in memoriaGlobal.memoria.keys():
                rightVal = memoriaGlobal.memoria[rightDir]
            
            if rightDir in memoriaLocal.memoria.keys():
                rightVal = memoriaLocal.memoria[rightDir]

            print("leftVal", leftVal)
            print("rightVal", rightVal)
            print("res", res)
            
            if type(leftVal) != str and leftVal in memoriaLocal.memoria.keys():
                leftVal = memoriaLocal.memoria[leftVal]
            
            if type(rightVal) != str and rightVal in memoriaLocal.memoria.keys():
                rightVal = memoriaLocal.memoria[rightVal]

            print("leftVal2", leftVal)
            print("rightVal2", rightVal)

            lFinal = convertirConstanteEnTipo(leftVal)
            rFinal = convertirConstanteEnTipo(rightVal)
            print("tipo lef",type(leftVal))
            print("tipo rig",type(rightVal))

            valor = lFinal - rFinal

            if type(valor) == float:
                valor = round(valor,10)
            print("VALOR", valor)
            guardarEnMemoria(res, valor)
            apuntadorInstrucciones+=1

        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "*":
            print("MULT",cuadruplos.listaCuadruplos[apuntadorInstrucciones])
            leftDir = cuadruplos.listaCuadruplos[apuntadorInstrucciones][1]
            rightDir = cuadruplos.listaCuadruplos[apuntadorInstrucciones][2]
            res = cuadruplos.listaCuadruplos[apuntadorInstrucciones][3]
            print("MEMORIAGLOBAL",memoriaGlobal.memoria)
            print("MEMORIALOCAL",memoriaLocal.memoria)
            
            if leftDir in memoriaGlobal.memoria.keys():
                leftVal = memoriaGlobal.memoria[leftDir]

            if leftDir in memoriaLocal.memoria.keys():
                leftVal = memoriaLocal.memoria[leftDir]
            
            if rightDir in memoriaGlobal.memoria.keys():
                rightVal = memoriaGlobal.memoria[rightDir]
            
            if rightDir in memoriaLocal.memoria.keys():
                rightVal = memoriaLocal.memoria[rightDir]

            print("leftVal", leftVal)
            print("rightVal", rightVal)
            print("res", res)
            
            if type(leftVal) != str and leftVal in memoriaLocal.memoria.keys():
                leftVal = memoriaLocal.memoria[leftVal]
            
            if type(rightVal) != str and rightVal in memoriaLocal.memoria.keys():
                rightVal = memoriaLocal.memoria[rightVal]

            print("leftVal2", leftVal)
            print("rightVal2", rightVal)

            lFinal = convertirConstanteEnTipo(leftVal)
            rFinal = convertirConstanteEnTipo(rightVal)
            print("tipo lef",type(leftVal))
            print("tipo rig",type(rightVal))

            valor = lFinal * rFinal

            if type(valor) == float:
                valor = round(valor,10)
            print("VALOR", valor)
            guardarEnMemoria(res, valor)
            apuntadorInstrucciones+=1
        
        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "/":
            print("DIV",cuadruplos.listaCuadruplos[apuntadorInstrucciones])
            leftDir = cuadruplos.listaCuadruplos[apuntadorInstrucciones][1]
            rightDir = cuadruplos.listaCuadruplos[apuntadorInstrucciones][2]
            res = cuadruplos.listaCuadruplos[apuntadorInstrucciones][3]
            print("MEMORIAGLOBAL",memoriaGlobal.memoria)
            print("MEMORIALOCAL",memoriaLocal.memoria)
            
            if leftDir in memoriaGlobal.memoria.keys():
                leftVal = memoriaGlobal.memoria[leftDir]

            if leftDir in memoriaLocal.memoria.keys():
                leftVal = memoriaLocal.memoria[leftDir]
            
            if rightDir in memoriaGlobal.memoria.keys():
                rightVal = memoriaGlobal.memoria[rightDir]
            
            if rightDir in memoriaLocal.memoria.keys():
                rightVal = memoriaLocal.memoria[rightDir]

            print("leftVal", leftVal)
            print("rightVal", rightVal)
            print("res", res)
            
            if type(leftVal) != str and leftVal in memoriaLocal.memoria.keys():
                leftVal = memoriaLocal.memoria[leftVal]
            
            if type(rightVal) != str and rightVal in memoriaLocal.memoria.keys():
                rightVal = memoriaLocal.memoria[rightVal]

            print("leftVal2", leftVal)
            print("rightVal2", rightVal)

            lFinal = convertirConstanteEnTipo(leftVal)
            rFinal = convertirConstanteEnTipo(rightVal)
            print("tipo lef",type(leftVal))
            print("tipo rig",type(rightVal))
            if type(lFinal) == int and type(rFinal) == int:
                valor = lFinal // rFinal
            else:
                valor = lFinal / rFinal

            if type(valor) == float:
                valor = round(valor,10)

            print("VALOR", valor)
            guardarEnMemoria(res, valor)
            apuntadorInstrucciones+=1
        else:
            apuntadorInstrucciones+=1
    
    print("memoria GLOBAL en maquina")
    print(memoriaGlobal.memoria)
    print("memoria LOCAL en maquina")
    print(memoriaLocal.memoria)




def guardarEnMemoria(dir, valor):
    global memoriaLocalActual
    if esVariableGlobal(dir):
        memoriaGlobal.insertar(dir, valor)
    else:
        memoriaLocal.insertar(dir, valor)

def esVariableGlobal(dir):
    if (dir >= 0 and dir <= 11999) or (dir >= 36000 and dir <= 47999):
        return True
    return False


def traducirDirVirtualConstante(dir):
    diff = 0
    if dir >= 0 and dir <= 2999:
        diff = dir
        return 36000+diff
    elif dir >= 3000 and dir <= 5999:
        diff = dir - 3000
        return 39000+diff
    elif dir >= 6000 and dir <= 8999:
        diff = dir - 6000
        return 42000-diff
    elif dir >= 9000 and dir <= 11999:
        diff = dir - 9000
        return 45000+diff
    


def convertirConstanteEnTipo(valor):
    if type(valor) == str:
        if valor.isdigit():
            print("Yes it is Integer")
            return int(valor)
        elif valor.replace('.','',1).isdigit() and valor.count('.') < 2:
            print("Its Float")
            return float(valor)
        else:
            print("Its is Neither Integer Nor Float! Something else")
            return valor
    else:
        return valor
# def esFlotante(valorString):
#     try:
#         if valorString
#             return True
#     except ValueError:
#         return False

# def esEntero(valorString):
#     try:
#         int(valorString)
#         return True
#     except ValueError:
#         return False




# def esDireccionVirtual(dir):
#     if esVariableGlobal(dir):
#         if dir >= 


# def extraerValorPorDir(dir, noAsignada=True):
#     global memoriaLocal

#     try:
#         if noAsignada:
#             if esVariableGlobal(dir):
#                 if