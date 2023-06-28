from pprint import pprint
from constantes import Constantes
from directorioProcedimientos import Directorio
from cuadruplos import Cuadruplos

class MaquinaVirtual:
    def __init__(self, _id):
        self.memoria = {}
        self.id = _id

    def insertar(self, dirV, valor):
        self.memoria[dirV] = valor

    def obtenerValorPorDir(self, dirV):
        return self.memoria[dirV]

global memoriaLocal
memoriaLocal = MaquinaVirtual(None)
memoriaGlobal = MaquinaVirtual("global")
saltosPendientes = []

def ejecutar_maquina_virtual(directorioProcedimientos: Directorio, constantes: Constantes, cuadruplos: Cuadruplos):
    print("Ejecutando máquina virtual: ")
    print("")
    global _directorioProc
    _directorioProc = directorioProcedimientos
    apuntadorInstrucciones = 0
    for idConst, dataConstante in constantes.items():
        guardarEnMemoria(dataConstante["direccionVirtual"], idConst)
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
            valor = cuadruplos.listaCuadruplos[apuntadorInstrucciones][1]
            dirV = cuadruplos.listaCuadruplos[apuntadorInstrucciones][3]
            #print("Dirección: ", dirV)
            guardarEnMemoria(dirV, valor)
        
        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "+":
            print("Suma:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
            direccionIzq = cuadruplos.listaCuadruplos[apuntadorInstrucciones][1]
            direccionDer = cuadruplos.listaCuadruplos[apuntadorInstrucciones][2]
            resultado = cuadruplos.listaCuadruplos[apuntadorInstrucciones][3]
            #print("Memoria global: ", memoriaGlobal.memoria)
            #print("Memoria local: ", memoriaLocal.memoria)
            
            if direccionIzq in memoriaLocal.memoria.keys():
                valorIzq = memoriaLocal.memoria[direccionIzq]
            elif direccionIzq in memoriaGlobal.memoria.keys():
                valorIzq = memoriaGlobal.memoria[direccionIzq]
            
            if direccionDer in memoriaLocal.memoria.keys():
                valorDer = memoriaLocal.memoria[direccionDer]
            elif direccionDer in memoriaGlobal.memoria.keys():
                valorDer = memoriaGlobal.memoria[direccionDer]

            #print("Valor izquierdo: ", valorIzq)
            #print("Valor derecho: ", valorDer)
            #print(Resultado: ", resultado)
            
            if type(valorIzq) != str and valorIzq in memoriaLocal.memoria.keys():
                valorIzq = memoriaLocal.memoria[valorIzq]
            
            if type(valorDer) != str and valorDer in memoriaLocal.memoria.keys():
                valorDer = memoriaLocal.memoria[valorDer]

            #print("Valor izquierdo 2: ", valorIzq)
            #print("Valor derecho 2: ", valorDer)

            izqFinal = convertirConstanteEnTipo(valorIzq)
            derFinal = convertirConstanteEnTipo(valorDer)
            #print("Tipo izquierdo: ", type(valorIzq))
            #print("Tipo derecho: ", type(valorDer))

            valor = izqFinal + derFinal

            if type(valor) == float:
                valor = round(valor, 10)
            #print("Valor: ", valor)
            guardarEnMemoria(resultado, valor)
        
        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "-":
            print("Resta:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
            direccionIzq = cuadruplos.listaCuadruplos[apuntadorInstrucciones][1]
            direccionDer = cuadruplos.listaCuadruplos[apuntadorInstrucciones][2]
            resultado = cuadruplos.listaCuadruplos[apuntadorInstrucciones][3]
            #print("Memoria global: ", memoriaGlobal.memoria)
            #print("Memoria local: ", memoriaLocal.memoria)
            
            if direccionIzq in memoriaLocal.memoria.keys():
                valorIzq = memoriaLocal.memoria[direccionIzq]
            elif direccionIzq in memoriaGlobal.memoria.keys():
                valorIzq = memoriaGlobal.memoria[direccionIzq]
            
            if direccionDer in memoriaLocal.memoria.keys():
                valorDer = memoriaLocal.memoria[direccionDer]
            elif direccionDer in memoriaGlobal.memoria.keys():
                valorDer = memoriaGlobal.memoria[direccionDer]

            #print("Valor izquierdo: ", valorIzq)
            #print("Valor derecho: ", valorDer)
            #print("Resultado: ", resultado)
            
            if type(valorIzq) != str and valorIzq in memoriaLocal.memoria.keys():
                valorIzq = memoriaLocal.memoria[valorIzq]
            
            if type(valorDer) != str and valorDer in memoriaLocal.memoria.keys():
                valorDer = memoriaLocal.memoria[valorDer]

            #print("Valor izquierdo 2: ", valorIzq)
            #print("Valor derecho 2: ", valorDer)

            izqFinal = convertirConstanteEnTipo(valorIzq)
            derFinal = convertirConstanteEnTipo(valorDer)
            #print("Tipo izquierdo: ", type(valorIzq))
            #print("Tipo derecho: ", type(valorDer))

            valor = izqFinal - derFinal

            if type(valor) == float:
                valor = round(valor, 10)
            #print("Valor: ", valor)
            guardarEnMemoria(resultado, valor)

        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "*":
            print("Multiplicación:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
            direccionIzq = cuadruplos.listaCuadruplos[apuntadorInstrucciones][1]
            direccionDer = cuadruplos.listaCuadruplos[apuntadorInstrucciones][2]
            resultado = cuadruplos.listaCuadruplos[apuntadorInstrucciones][3]
            #print("Memoria global: ", memoriaGlobal.memoria)
            #print("Memoria local: ", memoriaLocal.memoria)
            
            if direccionIzq in memoriaLocal.memoria.keys():
                valorIzq = memoriaLocal.memoria[direccionIzq]
            elif direccionIzq in memoriaGlobal.memoria.keys():
                valorIzq = memoriaGlobal.memoria[direccionIzq]
            
            if direccionDer in memoriaLocal.memoria.keys():
                valorDer = memoriaLocal.memoria[direccionDer]
            elif direccionDer in memoriaGlobal.memoria.keys():
                valorDer = memoriaGlobal.memoria[direccionDer]

            #print("Valor izquierdo: ", valorIzq)
            #print("Valor derecho: ", valorDer)
            #print("Resultado: ", resultado)
            
            if type(valorIzq) != str and valorIzq in memoriaLocal.memoria.keys():
                valorIzq = memoriaLocal.memoria[valorIzq]
            
            if type(valorDer) != str and valorDer in memoriaLocal.memoria.keys():
                valorDer = memoriaLocal.memoria[valorDer]

            #print("Valor izquierdo 2: ", valorIzq)
            #print("Valor derecho 2: ", valorDer)

            izqFinal = convertirConstanteEnTipo(valorIzq)
            derFinal = convertirConstanteEnTipo(valorDer)
            #print("Tipo izquierdo: ", type(valorIzq))
            #print("Tipo derecho: ", type(valorDer))

            valor = izqFinal * derFinal

            if type(valor) == float:
                valor = round(valor, 10)
            #print("Valor: ", valor)
            guardarEnMemoria(resultado, valor)
        
        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "/":
            print("División:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
            direccionIzq = cuadruplos.listaCuadruplos[apuntadorInstrucciones][1]
            direccionDer = cuadruplos.listaCuadruplos[apuntadorInstrucciones][2]
            resultado = cuadruplos.listaCuadruplos[apuntadorInstrucciones][3]
            #print("Memoria global: ", memoriaGlobal.memoria)
            #print("Memoria local: ", memoriaLocal.memoria)
            
            if direccionIzq in memoriaLocal.memoria.keys():
                valorIzq = memoriaLocal.memoria[direccionIzq]
            elif direccionIzq in memoriaGlobal.memoria.keys():
                valorIzq = memoriaGlobal.memoria[direccionIzq]
            
            if direccionDer in memoriaLocal.memoria.keys():
                valorDer = memoriaLocal.memoria[direccionDer]
            elif direccionDer in memoriaGlobal.memoria.keys():
                valorDer = memoriaGlobal.memoria[direccionDer]

            #print("Valor izquierdo: ", valorIzq)
            #print("Valor derecho: ", valorDer)
            #print("Resultado: ", resultado)
            
            if type(valorIzq) != str and valorIzq in memoriaLocal.memoria.keys():
                valorIzq = memoriaLocal.memoria[valorIzq]
            
            if type(valorDer) != str and valorDer in memoriaLocal.memoria.keys():
                valorDer = memoriaLocal.memoria[valorDer]

            #print("Valor izquierdo 2: ", valorIzq)
            #print("Valor derecho 2: ", valorDer)

            izqFinal = convertirConstanteEnTipo(valorIzq)
            derFinal = convertirConstanteEnTipo(valorDer)

            #print("Tipo izquierdo: ", type(valorIzq))
            #print("Tipo derecho: ", type(valorDer))

            if type(izqFinal) == int and type(derFinal) == int:
                valor = izqFinal // derFinal
            else:
                valor = izqFinal / derFinal

            if type(valor) == float:
                valor = round(valor, 10)

            #print("Valor: ", valor)
            guardarEnMemoria(resultado, valor)

        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "print":
            
            dirV = cuadruplos.listaCuadruplos[apuntadorInstrucciones][3]
            
            if dirV in memoriaLocal.memoria.keys():
                valorPrint = memoriaLocal.memoria[dirV]
            elif dirV in memoriaGlobal.memoria.keys():
                valorPrint = memoriaGlobal.memoria[dirV]

            if valorPrint in memoriaLocal.memoria.keys():
                valorFinal = memoriaLocal.memoria[valorPrint]
            elif valorPrint in memoriaGlobal.memoria.keys():
                valorFinal = memoriaGlobal.memoria[valorPrint]
            else:
                valorFinal = valorPrint
            
            print(str(valorFinal))

        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "read":
            resultado = input()
            resultadoConvertido = convertirConstanteEnTipo(resultado)
            guardarEnMemoria(cuadruplos.listaCuadruplos[apuntadorInstrucciones][3], resultadoConvertido)
        
        apuntadorInstrucciones+=1
        
    print("")
    print("Memoria en la máquina virtual: ")
    print("Global: ", memoriaGlobal.memoria)
    print("Local: ", memoriaLocal.memoria)

def guardarEnMemoria(dirV, valor):
    global memoriaLocalActual
    if esVariableGlobal(dirV):
        memoriaGlobal.insertar(dirV, valor)
    else:
        memoriaLocal.insertar(dirV, valor)

def esVariableGlobal(dirV):
    if (dirV >= 0 and dirV <= 11999) or (dirV >= 36000 and dirV <= 47999):
        return True
    return False

def traducirDirVirtualConstante(dirV):
    diferencia = 0
    if dirV >= 0 and dirV <= 2999:
        diferencia = dirV
        return 36000 + diferencia
    elif dirV >= 3000 and dirV <= 5999:
        diferencia = dirV - 3000
        return 39000 + diferencia
    elif dirV >= 6000 and dirV <= 8999:
        diferencia = dirV - 6000
        return 42000 - diferencia
    elif dirV >= 9000 and dirV <= 11999:
        diferencia = dirV - 9000
        return 45000 + diferencia

def convertirConstanteEnTipo(valor):
    if type(valor) == str:
        if valor.isdigit():
            #print("Es entero.")
            return int(valor)
        elif valor.replace('.','',1).isdigit() and valor.count('.') < 2:
            #print("Es flotante.")
            return float(valor)
        else:
            print("No es ni entero ni flotante.")
            return valor
    else:
        return valor
