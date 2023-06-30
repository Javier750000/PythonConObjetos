from pprint import pprint
from avail import Avail
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
stackMemoria = []
esFuncion = False
stackMemoria.append(memoriaGlobal)
saltosPendientes = []

def ejecutar_maquina_virtual(directorioProcedimientos: Directorio, constantes: Constantes, cuadruplos: Cuadruplos, avail: Avail):
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
        i+=1
    print("---------------------------------------------------")
    while cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] != "End":
        
        global memoriaLocal

        if cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "=":
            # print("Asignación:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
            valor = cuadruplos.listaCuadruplos[apuntadorInstrucciones][1]
            dirV = cuadruplos.listaCuadruplos[apuntadorInstrucciones][3]
            #print("VALOR:", valor)
            if(esFuncion):
                # print("VALOR EN IF:", valor)
                valorFinal = extraerValorPorDirVirtual(valor)
                # print("VALORFINAL EN IF:", valorFinal)
                guardarEnMemoria(dirV,valorFinal)
            else:    
                # print("Dirección asignación:", dirV)
                # print("VALOR EN ASIG:", valor)
                guardarEnMemoria(dirV, valor)
                # print("MEMORIA GLOBAL EN ASIG:",memoriaGlobal.memoria)
                # print("MEMORIA LOCAL EN ASIG:",memoriaLocal.memoria)
        
        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "+":
            # print("Suma:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
            direccionIzq = cuadruplos.listaCuadruplos[apuntadorInstrucciones][1]
            direccionDer = cuadruplos.listaCuadruplos[apuntadorInstrucciones][2]
            resultado = cuadruplos.listaCuadruplos[apuntadorInstrucciones][3]

            # print("Memoria global:", memoriaGlobal.memoria)
            # print("Memoria local:", memoriaLocal.memoria)

            valorIzq = extraerValorPorDirVirtual(direccionIzq)
            valorDer = extraerValorPorDirVirtual(direccionDer)

            #print("Valor izquierdo suma 2:", valorIzq)
            #print("Valor derecho suma 2:", valorDer)

            izqFinal = convertirConstanteEnTipo(valorIzq)
            derFinal = convertirConstanteEnTipo(valorDer)
            #print("Tipo izquierdo:", type(valorIzq))
            #print("Tipo derecho:", type(valorDer))

            valor = izqFinal + derFinal

            if type(valor) == float:
                valor = round(valor, 10)
            #print("Valor suma:", valor)
            guardarEnMemoria(resultado, str(valor))

        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "-":
            # print("Resta:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
            direccionIzq = cuadruplos.listaCuadruplos[apuntadorInstrucciones][1]
            direccionDer = cuadruplos.listaCuadruplos[apuntadorInstrucciones][2]
            resultado = cuadruplos.listaCuadruplos[apuntadorInstrucciones][3]
           

            valorIzq = extraerValorPorDirVirtual(direccionIzq)
            valorDer = extraerValorPorDirVirtual(direccionDer)

            #print("Valor izquierdo resta 2:", valorIzq)
            #print("Valor derecho resta 2:", valorDer)

            izqFinal = convertirConstanteEnTipo(valorIzq)
            derFinal = convertirConstanteEnTipo(valorDer)
            
            #print("Tipo izquierdo:", type(valorIzq))
            #print("Tipo derecho:", type(valorDer))

            valor = izqFinal - derFinal

            if type(valor) == float:
                valor = round(valor, 10)
            #print("Valor resta:", valor)
            guardarEnMemoria(resultado, str(valor))

        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "*":
            # print("Multiplicación:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
            direccionIzq = cuadruplos.listaCuadruplos[apuntadorInstrucciones][1]
            direccionDer = cuadruplos.listaCuadruplos[apuntadorInstrucciones][2]
            resultado = cuadruplos.listaCuadruplos[apuntadorInstrucciones][3]
            
            valorIzq = extraerValorPorDirVirtual(direccionIzq)
            valorDer = extraerValorPorDirVirtual(direccionDer)

            #print("Valor izquierdo multiplicación 2:", valorIzq)
            #print("Valor derecho multiplicación 2:", valorDer)

            izqFinal = convertirConstanteEnTipo(valorIzq)
            derFinal = convertirConstanteEnTipo(valorDer)

            valor = izqFinal * derFinal

            if type(valor) == float:
                valor = round(valor, 10)
            #print("Valor multiplicación:", valor)
            guardarEnMemoria(resultado, str(valor))
        
        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "/":
            # print("División:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
            direccionIzq = cuadruplos.listaCuadruplos[apuntadorInstrucciones][1]
            direccionDer = cuadruplos.listaCuadruplos[apuntadorInstrucciones][2]
            resultado = cuadruplos.listaCuadruplos[apuntadorInstrucciones][3]
            

            valorIzq = extraerValorPorDirVirtual(direccionIzq)
            valorDer = extraerValorPorDirVirtual(direccionDer)

            #print("Valor izquierdo división 2:", valorIzq)
            #print("Valor derecho división 2:", valorDer)

            izqFinal = convertirConstanteEnTipo(valorIzq)
            derFinal = convertirConstanteEnTipo(valorDer)

            #print("Tipo izquierdo:", type(valorIzq))
            #print("Tipo derecho:", type(valorDer))

            if type(izqFinal) == int and type(derFinal) == int:
                valor = izqFinal // derFinal
            else:
                valor = izqFinal / derFinal

            if type(valor) == float:
                valor = round(valor, 10)

            #print("Valor división:", valor)
            guardarEnMemoria(resultado, str(valor))
        
        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == ">":
            # print("Mayor que:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
            # print("Global:", memoriaGlobal.memoria)
            # print("Local:", memoriaLocal.memoria)

            direccionIzq = cuadruplos.listaCuadruplos[apuntadorInstrucciones][1]
            direccionDer = cuadruplos.listaCuadruplos[apuntadorInstrucciones][2]

            resultado = cuadruplos.listaCuadruplos[apuntadorInstrucciones][3]

            valorIzq = extraerValorPorDirVirtual(direccionIzq)
            valorDer = extraerValorPorDirVirtual(direccionDer)

            # print("Valor izquierdo 2:", valorIzq)
            # print("Valor derecho 2:", valorDer)
            
            izqFinal = convertirConstanteEnTipo(valorIzq)
            derFinal = convertirConstanteEnTipo(valorDer)

            valor = bool(izqFinal > derFinal)
            guardarEnMemoria(resultado, valor)

        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == ">=":
            # print("Mayor igual que:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
            # print("Global:", memoriaGlobal.memoria)
            # print("Local:", memoriaLocal.memoria)
            direccionIzq = cuadruplos.listaCuadruplos[apuntadorInstrucciones][1]
            direccionDer = cuadruplos.listaCuadruplos[apuntadorInstrucciones][2]

            resultado = cuadruplos.listaCuadruplos[apuntadorInstrucciones][3]

            valorIzq = extraerValorPorDirVirtual(direccionIzq)
            valorDer = extraerValorPorDirVirtual(direccionDer)

            # print("Valor izquierdo 2:", valorIzq)
            # print("Valor derecho 2:", valorDer)
            
            izqFinal = convertirConstanteEnTipo(valorIzq)
            derFinal = convertirConstanteEnTipo(valorDer)

            valor = bool(izqFinal >= derFinal)
            guardarEnMemoria(resultado, valor)

        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "<":
            # print("Menor que:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
            # print("Global:", memoriaGlobal.memoria)
            # print("Local:", memoriaLocal.memoria)
            direccionIzq = cuadruplos.listaCuadruplos[apuntadorInstrucciones][1]
            direccionDer = cuadruplos.listaCuadruplos[apuntadorInstrucciones][2]

            # print("MENOR QUE direccionIzq:", direccionIzq)
            # print("MENOR QUE direccionDer:", direccionDer)

            resultado = cuadruplos.listaCuadruplos[apuntadorInstrucciones][3]

            valorIzq = extraerValorPorDirVirtual(direccionIzq)
            valorDer = extraerValorPorDirVirtual(direccionDer)

            # print("MENOR QUE Valor izquierdo 2:", valorIzq)
            # print("MENOR QUE Valor derecho 2:", valorDer)
            
            izqFinal = convertirConstanteEnTipo(valorIzq)
            derFinal = convertirConstanteEnTipo(valorDer)

            valor = bool(izqFinal < derFinal)
            guardarEnMemoria(resultado, valor)

        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "<=":
            # print("Menor igual que:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
            # print("Global:", memoriaGlobal.memoria)
            # print("Local:", memoriaLocal.memoria)
            direccionIzq = cuadruplos.listaCuadruplos[apuntadorInstrucciones][1]
            direccionDer = cuadruplos.listaCuadruplos[apuntadorInstrucciones][2]

            resultado = cuadruplos.listaCuadruplos[apuntadorInstrucciones][3]

            valorIzq = extraerValorPorDirVirtual(direccionIzq)
            valorDer = extraerValorPorDirVirtual(direccionDer)

            # print("Valor izquierdo 2:", valorIzq)
            # print("Valor derecho 2:", valorDer)
            
            izqFinal = convertirConstanteEnTipo(valorIzq)
            derFinal = convertirConstanteEnTipo(valorDer)

            valor = bool(izqFinal <= derFinal)
            guardarEnMemoria(resultado, valor)

        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "==":
            # print("Equivalente a:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
            # print("Global:", memoriaGlobal.memoria)
            # print("Local:", memoriaLocal.memoria)
            direccionIzq = cuadruplos.listaCuadruplos[apuntadorInstrucciones][1]
            direccionDer = cuadruplos.listaCuadruplos[apuntadorInstrucciones][2]

            resultado = cuadruplos.listaCuadruplos[apuntadorInstrucciones][3]

            valorIzq = extraerValorPorDirVirtual(direccionIzq)
            valorDer = extraerValorPorDirVirtual(direccionDer)

            # print("Valor izquierdo 2:", valorIzq)
            # print("Valor derecho 2:", valorDer)
            
            izqFinal = convertirConstanteEnTipo(valorIzq)
            derFinal = convertirConstanteEnTipo(valorDer)

            valor = bool(izqFinal == derFinal)
            guardarEnMemoria(resultado, valor)

        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "<>":
            # print("Diferente de:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
            # print("Global:", memoriaGlobal.memoria)
            # print("Local:", memoriaLocal.memoria)
            direccionIzq = cuadruplos.listaCuadruplos[apuntadorInstrucciones][1]
            direccionDer = cuadruplos.listaCuadruplos[apuntadorInstrucciones][2]

            resultado = cuadruplos.listaCuadruplos[apuntadorInstrucciones][3]

            valorIzq = extraerValorPorDirVirtual(direccionIzq)
            valorDer = extraerValorPorDirVirtual(direccionDer)

            # print("Valor izquierdo 2:", valorIzq)
            # print("Valor derecho 2:", valorDer)
            
            izqFinal = convertirConstanteEnTipo(valorIzq)
            derFinal = convertirConstanteEnTipo(valorDer)

            valor = bool(izqFinal != derFinal)
            guardarEnMemoria(resultado, valor)

        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "&&":
            # print("And:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
            # print("Global:", memoriaGlobal.memoria)
            # print("Local:", memoriaLocal.memoria)
            direccionIzq = cuadruplos.listaCuadruplos[apuntadorInstrucciones][1]
            direccionDer = cuadruplos.listaCuadruplos[apuntadorInstrucciones][2]

            resultado = cuadruplos.listaCuadruplos[apuntadorInstrucciones][3]

            valorIzq = extraerValorPorDirVirtual(direccionIzq)
            valorDer = extraerValorPorDirVirtual(direccionDer)

            # print("Valor izquierdo 2:", valorIzq)
            # print("Valor derecho 2:", valorDer)
            
            izqFinal = convertirConstanteEnTipo(valorIzq)
            derFinal = convertirConstanteEnTipo(valorDer)

            valor = bool(izqFinal and derFinal)
            guardarEnMemoria(resultado, valor)

        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "||":
            # print("Or:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
            # print("Global:", memoriaGlobal.memoria)
            # print("Local:", memoriaLocal.memoria)
            direccionIzq = cuadruplos.listaCuadruplos[apuntadorInstrucciones][1]
            direccionDer = cuadruplos.listaCuadruplos[apuntadorInstrucciones][2]

            resultado = cuadruplos.listaCuadruplos[apuntadorInstrucciones][3]

            valorIzq = extraerValorPorDirVirtual(direccionIzq)
            valorDer = extraerValorPorDirVirtual(direccionDer)

            # print("Valor izquierdo 2:", valorIzq)
            # print("Valor derecho 2:", valorDer)
            
            izqFinal = convertirConstanteEnTipo(valorIzq)
            derFinal = convertirConstanteEnTipo(valorDer)

            valor = bool(izqFinal or derFinal)
            guardarEnMemoria(resultado, valor)

        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == 'GoTo':
            # if quadruples[instruction_pointer][4] is not None:
            # print("Se detectó un GoTo. El apuntador de instrucciones se cambió al cuádruplo: " + str(cuadruplos.listaCuadruplos[apuntadorInstrucciones][3]-1) + ".")
            apuntadorInstrucciones = cuadruplos.listaCuadruplos[apuntadorInstrucciones][3]-2
            # print("GOTO",cuadruplos.listaCuadruplos[apuntadorInstrucciones][3])
        
        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "GoToF":
            # print("GoToF", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
            direccionBool = cuadruplos.listaCuadruplos[apuntadorInstrucciones][1]
            valorBool = extraerValorPorDirVirtual(direccionBool)
            # print("GOTOF",valorBool)
            
            if not valorBool:
                # print("Se detectó un GoToF. El apuntador de instrucciones se cambió al cuádruplo: " + str(cuadruplos.listaCuadruplos[apuntadorInstrucciones][3]-1) + ".")
                apuntadorInstrucciones = cuadruplos.listaCuadruplos[apuntadorInstrucciones][3]-1
                continue
        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "param":
            # Obtain paramater index
            indiceParametro = cuadruplos.listaCuadruplos[apuntadorInstrucciones][1] - 1  ## ???
            # print(current_local_memory.return_val())
            dirVParam = cuadruplos.listaCuadruplos[apuntadorInstrucciones][1]
            # print("DIR PARAM:",dirVParam)
            dirVirtualEnNuevoContexto = cuadruplos.listaCuadruplos[apuntadorInstrucciones][3]
            valor = extraerValorPorDirVirtual(cuadruplos.listaCuadruplos[apuntadorInstrucciones][3])
            stackMemoria[-1].memoria[dirVParam] = valor
            # instruction_pointer += 1
        
        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "ERA":
            nombreFuncion = cuadruplos.listaCuadruplos[apuntadorInstrucciones][3]
            nombreSeparado = nombreFuncion.split(".")

            if len(nombreSeparado) != 1:
                continue
            else:
                # print("NOMBRE FUNC:",nombreFuncion)
                funcion = directorioProcedimientos.tabla[nombreFuncion]
                # print("DIRECTORIO EN ERA:",funcion)
                memoriaNuevoContexto = MaquinaVirtual(nombreFuncion)
                for variable in funcion["tablaVariables"].items():
                    # print("variables ERA:", variable[1]["direccionVirtual"])
                    memoriaNuevoContexto.insertar(variable[1]["direccionVirtual"], None)
                funcionDataGlobal = directorioProcedimientos.tabla["global"]["tablaVariables"][nombreFuncion]
                memoriaNuevoContexto.insertar(funcionDataGlobal["direccionVirtual"], nombreFuncion)
                # print("memoria NUEVO CONTEXTO:", memoriaNuevoContexto.memoria)
                stackMemoria.append(memoriaNuevoContexto)
        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "GoSub":
            esFuncion=True
            # print("cuadruplo GOSUB:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
            saltosPendientes.append(apuntadorInstrucciones+1)
            # print("stackMEMORIA GOSUB", stackMemoria[-1].memoria)
            memoriaLocal = stackMemoria[-1]
            # print("memoriaLocal en GOSUB:",memoriaLocal.memoria)
            apuntadorInstrucciones = cuadruplos.listaCuadruplos[apuntadorInstrucciones][3] - 2
        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "Return":
            if cuadruplos.listaCuadruplos[apuntadorInstrucciones][1] is not None:
                apuntadorReturn = saltosPendientes.pop()
                apuntadorInstrucciones = apuntadorReturn
                continue
            else:
                apuntadorReturn = 0
                if not (len(stackMemoria) <= 1):
                    # print("memoria en RETURN:")
                    #for espacio in stackMemoria:
                        # print("Espacio En RETURN:", espacio.memoria)
                    memoriaBorrada = stackMemoria.pop()
                    nuevaMemoria = stackMemoria[-1]
                    # print("memoria FINAL RETURN:",stackMemoria[-1].memoria)
                    memoriaLocal = nuevaMemoria
                    apuntadorReturn = saltosPendientes.pop()
                    apuntadorInstrucciones = apuntadorReturn
                    continue
        
        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "EndFunc":
            esFuncion=False
            if cuadruplos.listaCuadruplos[apuntadorInstrucciones][1] is not None:
                apuntadorReturn = saltosPendientes.pop()
                apuntadorInstrucciones = apuntadorReturn
                continue
            else:
                apuntadorReturn = 0
                if not (len(stackMemoria) <= 1):
                    # print("memoria en ENDFUNC:")
                    #for espacio in stackMemoria:
                        # print("Espacio EN ENDFUNC:", espacio.memoria)
                    memoriaBorrada = stackMemoria.pop()
                    nuevaMemoria = stackMemoria[-1]
                    memoriaLocal = nuevaMemoria
                    apuntadorReturn = saltosPendientes.pop()
                    apuntadorInstrucciones = apuntadorReturn
                    continue
        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "print":
            # print("Escritura:", cuadruplos.listaCuadruplos[apuntadorInstrucciones])
            dirV = cuadruplos.listaCuadruplos[apuntadorInstrucciones][3]
            # print("dirV", dirV)
            valorFinal = extraerValorPorDirVirtual(dirV)
            
            print(str(valorFinal))

        elif cuadruplos.listaCuadruplos[apuntadorInstrucciones][0] == "read":
            resultado = input()
            resultadoTipo = convertirConstanteEnTipo(resultado)
            if type(resultadoTipo) == int:
               resultadoConvertido = avail.generarDireccionNueva("int", "globales")
            elif type(resultadoTipo) == float:
                resultadoConvertido = avail.generarDireccionNueva("float", "globales")
            else:
                resultadoConvertido = avail.generarDireccionNueva("char", "globales")
            
            # print("Resultado direccion:", resultadoConvertido)
            # print("direccion cuadruplos:", cuadruplos.listaCuadruplos[apuntadorInstrucciones][3])
            # print("resultado tipo:", resultadoTipo)
            guardarEnMemoria(cuadruplos.listaCuadruplos[apuntadorInstrucciones][3], resultadoConvertido)
            guardarEnMemoria(resultadoConvertido, resultado)

        apuntadorInstrucciones+=1
        
    print("---------------------------------------------------")
    print("Ejecucion finalizada.")
    print("Memoria en la máquina virtual: ")
    print("Global:", memoriaGlobal.memoria)
    print("Local:", memoriaLocal.memoria)
    print("STACK:")
    for espacio in stackMemoria:
        print("Espacio:", espacio.memoria)
    memoriaGlobal.memoria = {}
    memoriaLocal.memoria = {}

def guardarEnMemoria(dirV, valor):
    global memoriaLocal
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


def extraerValorPorDirVirtual(dir):
    valorTentativo = None
    valorFinal = None
    # print("MEMORIA GLOBAL AL EXTRAER:", memoriaGlobal.memoria)
    # print("MEMORIA LOCAL AL EXTRAER:", memoriaLocal.memoria)
    if dir in memoriaGlobal.memoria.keys():
        valorTentativo = memoriaGlobal.memoria[dir]

    if dir in memoriaLocal.memoria.keys():
        valorTentativo = memoriaLocal.memoria[dir]
    
    # print("DIR AL EXTRAER:", dir)
    # print("Valor tentativo:", valorTentativo)
    valorFinal = valorTentativo

    if type(valorTentativo) != str and type(valorTentativo) != bool and valorTentativo in memoriaGlobal.memoria.keys():
        valorFinal = memoriaGlobal.memoria[valorTentativo]

    if type(valorTentativo) != str and type(valorTentativo) != bool and valorTentativo in memoriaLocal.memoria.keys():
        valorFinal = memoriaLocal.memoria[valorTentativo]
    
    # print("Valor final:", valorFinal)
    return valorFinal
