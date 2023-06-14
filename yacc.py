from lex import lexer, tokens
from ply.yacc import yacc
from directorioProcedimientos import Directorio
from avail import Avail
from cuadruplos import Cuadruplos
from cuboSemantico import CuboSemantico
from constantes import Constantes
from pprint import pprint

directorio = Directorio()
avail = Avail()
cuadruplos = Cuadruplos()
cuboSemantico = CuboSemantico()
constantes = Constantes()
pilaOperandos = []
pilaOperadores = []
pilaTipos = []
pilaContextos = []
pilaSaltos = []
pilaDimensiones = []

def p_programa(p):
    '''
    programa : PROGRAM inicializarDirectorio ID PUNTOYCOMA cuadruploMain clases vars2 funciones MAIN PARENTESISINICIAL PARENTESISFINAL saltoMain vars2 bloque
    '''
    print("Directorio: ")
    pprint(directorio.tabla, sort_dicts=False)
    print("")

    print("Tabla de constantes: ")
    pprint(constantes.tabla, sort_dicts=False)
    print("")

    print("Cuádruplos: ")
    i=1
    for cuadruplo in cuadruplos.listaCuadruplos:
        print(f'{i}: {cuadruplo}')
        i+=1;
    print("")

    print("Pila de operandos: ")
    print(pilaOperandos)
    print("")
    print("Pila de tipos: ")
    print(pilaTipos)
    print("")
    print("Pila de operadores: ")
    print(pilaOperadores)
    print("")
    print("Pila de saltos: ")
    print(pilaSaltos)
    print("")

def p_inicializarDirectorio(p):
    '''
    inicializarDirectorio : empty
    '''
    directorio.contextoGlobal()
    pilaContextos.append("global")

def p_cuadruploMain(p):
    '''
    cuadruploMain : empty
    '''
    cuadruplos.generarCuadruploNuevo('GoTo', None, None, None)
    pilaSaltos.append(cuadruplos.contador-1)

def p_clases(p):
    '''
    clases : CLASE ID herencia bloqueClase clases
           | empty
    '''

def p_herencia(p):
    '''
    herencia : HEREDA ID
             | empty
    '''

def p_bloqueClase(p):
    '''
    bloqueClase : LLAVEINICIAL ATRIBUTOS bloqueAtributos METODOS bloqueMetodos LLAVEFINAL PUNTOYCOMA
    '''

def p_bloqueAtributos(p):
    '''
    bloqueAtributos : LLAVEINICIAL listaVarsSimples LLAVEFINAL
    '''

def p_bloqueMetodos(p):
    '''
    bloqueMetodos : LLAVEINICIAL funciones LLAVEFINAL
    '''

def p_funciones(p):
    '''
    funciones : funcionSimple
              | funcionVoid
              | empty
    '''

def p_funcionSimple(p):
    '''
    funcionSimple : FUNC tipo ID agregarFuncion PARENTESISINICIAL param PARENTESISFINAL contadorParametros vars2 contadorLocales contadorCuadruplos bloqueFuncional terminarFuncion eliminarContexto funciones
    '''

def p_funcionVoid(p):
    '''
    funcionVoid : FUNC VOID ID agregarFuncion PARENTESISINICIAL param PARENTESISFINAL contadorParametros vars2 contadorLocales contadorCuadruplos bloque terminarFuncion eliminarContexto funciones
    '''

def p_agregarFuncion(p):
    '''
    agregarFuncion :
    '''
    directorio.agregarFuncion(p[-1], p[-2])
    pilaContextos.append(p[-1])
    directorio.contadorParametros = 0
    directorio.reinicializarContadorLocales()
    avail.reinicializar()

def p_eliminarContexto(p):
    '''
    eliminarContexto : 
    '''
    pilaContextos.pop()

def p_terminarFuncion(p):
    '''
    terminarFuncion : empty
    '''
    directorio.tabla[pilaContextos[-1]]["tablaVariables"].clear()
    cuadruplos.generarCuadruploNuevo('EndFunc', None, None, None)
    print("Número de temporales:")
    directorio.temporales = avail.regresarDireccionesOcupadas('temporales')
    print(directorio.temporales)
    print("")

def p_param(p):
    '''
    param : tipo ID agregarParam paramsAdicionales
          | empty
    '''

def p_agregarParam(p):
    '''
    agregarParam :
    '''
    directorio.agregarVariables(p[-1], p[-2], pilaContextos[-1])
    directorio.agregarParametros(p[-1], p[-2], pilaContextos[-1])
    directorio.contadorParametros+=1;

def p_paramsAdicionales(p):
    '''
    paramsAdicionales : COMA param
                      | empty
    '''

def p_contadorParametros(p):
    '''
    contadorParametros : empty
    '''
    print("La función tiene el siguiente número de parámetros:")
    print(directorio.contadorParametros)
    print("")
    directorio.agregarCantidadParametros(pilaContextos[-1])

def p_contadorLocales(p):
    '''
    contadorLocales : empty
    '''
    print("La función tiene el siguiente número de variables locales:")
    print(directorio.contadorLocales)
    print("")

def p_contadorCuadruplos(p):
    '''
    contadorCuadruplos : empty
    '''
    directorio.contador = cuadruplos.contador
    print("La función empieza en el cuádruplo siguiente:")
    print(directorio.contador)
    print("")

def p_vars2(p):
    '''
    vars2 : vars
          | empty
    '''
    p[0] = p[1]

def p_vars(p):
    '''
    vars : VAR listaVarsSimples
         | VAR listaVarsCompuestas
    '''
    p[0] = p[2]

def p_listaVarsSimples(p):
    '''
    listaVarsSimples : tipo guardarTipo DOSPUNTOS listaIDsSimples PUNTOYCOMA varsAdicionales
    '''
    p[0] = p[4]

def p_guardarTipo(p):
    '''
    guardarTipo : 
    '''
    directorio.tipo = p[-1]

def p_listaVarsCompuestas(p):
    '''
    listaVarsCompuestas : ID DOSPUNTOS listaIDsCompuestos PUNTOYCOMA varsAdicionales
    '''

def p_listaIDsSimples(p):
    '''
    listaIDsSimples : ID array comasAdicionalesSimples
    '''
    print("Variable:", p[1])
    print("")
    
    directorio.agregarVariables(p[1], directorio.tipo, pilaContextos[-1])
    directorio.actualizarContadorLocales(directorio.tipo)

def p_array(p):
    '''
    array : CORCHETEINICIAL CTE_I CORCHETEFINAL matrix
          | empty
    '''

def p_matrix(p):
    '''
    matrix : CORCHETEINICIAL CTE_I CORCHETEFINAL
           | empty
    '''

def p_listaIDsCompuestos(p):
    '''
    listaIDsCompuestos : ID comasAdicionalesCompuestas
    '''

def p_comasAdicionalesSimples(p):
    '''
    comasAdicionalesSimples : COMA listaIDsSimples
                            | empty
    '''

def p_comasAdicionalesCompuestas(p):
    '''
    comasAdicionalesCompuestas : COMA listaIDsCompuestos
                               | empty
    '''

def p_varsAdicionales(p):
    '''
    varsAdicionales : listaVarsSimples
                    | listaVarsCompuestas
                    | empty
    '''

def p_tipo(p):
    '''
    tipo : INT
         | FLOAT
         | CHAR
         | BOOL
    '''
    p[0] = p[1]

def p_saltoMain(p):
    '''
    saltoMain : empty
    '''
    cuadruploMain = pilaSaltos.pop()
    cuadruplos.llenarCuadruploPendiente(cuadruploMain, cuadruplos.contador)

def p_bloque(p):
    '''
    bloque : LLAVEINICIAL estatuto2 LLAVEFINAL
    '''

def p_estatuto2(p):
    '''
    estatuto2 : estatuto estatuto2
	          | empty
    '''

def p_estatuto(p):
    '''
    estatuto : asignacion
	         | condicion
	         | escritura
             | lectura
             | cicloFor
             | cicloWhile
             | llamada
    '''
    p[0] = p[1]

def p_asignacion(p):
    '''
    asignacion : variable IGUALA hiperexpresion cuadruploAsignacion PUNTOYCOMA
    '''

def p_cuadruploAsignacion(p):
    '''
    cuadruploAsignacion : empty
    '''
    if directorio.tabla[pilaContextos[-1]]["tablaVariables"][p[-3]] != pilaTipos[-1]:
        raise Exception("A la variable «"+ p[-3] + "» no se le puede asignar ese tipo de dato.")
    else:
        cuadruplos.generarCuadruploNuevo('=', pilaOperandos.pop(), None, p[-3])
        pilaTipos.pop()

def p_condicion(p):
    '''
    condicion : IF PARENTESISINICIAL hiperexpresion PARENTESISFINAL cuadruploCondicion bloque bloqueCondicional llenarSaltoPendiente
    '''

def p_cuadruploCondicion(p):
    '''
    cuadruploCondicion : empty
    '''
    if pilaTipos.pop() != 'bool':
        raise Exception("Las condiciones deben ser booleanas.")
    else:
        resultado = pilaOperandos.pop()
        cuadruplos.generarCuadruploNuevo('GoToF', resultado, None, None)
        pilaSaltos.append(cuadruplos.contador-1)

def p_bloqueCondicional(p):
    '''
    bloqueCondicional : ELSE cuadruploElse bloque
                      | empty
    '''

def p_cuadruploElse(p):
    '''
    cuadruploElse : empty
    '''
    cuadruplos.generarCuadruploNuevo('GoTo', None, None, None)
    falso = pilaSaltos.pop()
    pilaSaltos.append(cuadruplos.contador-1)
    cuadruplos.llenarCuadruploPendiente(falso, cuadruplos.contador)

def p_llenarSaltoPendiente(p):
    '''
    llenarSaltoPendiente : empty
    '''
    cuadruploPendiente = pilaSaltos.pop()
    cuadruplos.llenarCuadruploPendiente(cuadruploPendiente, cuadruplos.contador)

def p_bloqueFuncional(p):
    '''
    bloqueFuncional : LLAVEINICIAL estatutoFuncional2 LLAVEFINAL
    '''

def p_estatutoFuncional2(p):
    '''
    estatutoFuncional2 : estatutoFuncional estatutoFuncional2
                       | empty
    '''

def p_estatutoFuncional(p):
    '''
    estatutoFuncional : asignacion
                      | condicionFuncional
                      | escritura
                      | lectura
                      | cicloFor
                      | cicloWhile
                      | llamada
                      | RETURN PARENTESISINICIAL hiperexpresion PARENTESISFINAL PUNTOYCOMA
    '''
    p[0] = p[1]

def p_condicionFuncional(p):
    '''
    condicionFuncional : IF PARENTESISINICIAL hiperexpresion PARENTESISFINAL cuadruploCondicion bloqueFuncional bloqueCondicionalFuncional llenarSaltoPendiente
    '''

def p_bloqueCondicionalFuncional(p):
    '''
    bloqueCondicionalFuncional : ELSE cuadruploElse bloqueFuncional
                               | empty
    '''

def p_escritura(p):
    '''
    escritura : PRINT PARENTESISINICIAL listaExpresiones PARENTESISFINAL PUNTOYCOMA
    '''

def p_listaExpresiones(p):
    '''
    listaExpresiones : hiperexpresion cuadruploEscritura expresionesAdicionales
    '''

def p_expresionesAdicionales(p):
    '''
    expresionesAdicionales : COMA listaExpresiones
                           | empty
    '''

def p_cuadruploEscritura(p):
    '''
    cuadruploEscritura : empty
    '''
    cuadruplos.generarCuadruploNuevo('print', None, None, pilaOperandos.pop())
    pilaTipos.pop()

def p_lectura(p):
    '''
    lectura : READ PARENTESISINICIAL listaVariables PARENTESISFINAL PUNTOYCOMA
    '''

def p_listaVariables(p):
    '''
    listaVariables : variable cuadruploLectura variablesAdicionales
    '''

def p_variablesAdicionales(p):
    '''
    variablesAdicionales : COMA listaVariables
                         | empty
    '''

def p_cuadruploLectura(p):
    '''
    cuadruploLectura : empty
    '''
    cuadruplos.generarCuadruploNuevo('read', None, None, pilaOperandos.pop())
    pilaTipos.pop()

def p_cicloFor(p):
    '''
    cicloFor : FOR PARENTESISINICIAL ID IGUALA hiperexpresion UNTIL hiperexpresion PARENTESISFINAL bloque
    '''

def p_cicloWhile(p):
    '''
    cicloWhile : WHILE guardarSalto PARENTESISINICIAL hiperexpresion PARENTESISFINAL cuadruploWhile bloque llenarCuadruploPendiente
    '''

def p_guardarSalto(p):
    '''
    guardarSalto : empty
    '''
    pilaSaltos.append(cuadruplos.contador)

def p_cuadruploWhile(p):
    '''
    cuadruploWhile : empty
    '''
    if pilaTipos.pop() != 'bool':
        raise Exception("Las condiciones deben ser booleanas.")
    else:
        resultado = pilaOperandos.pop()
        cuadruplos.generarCuadruploNuevo('GoToF', resultado, None, None)
        pilaSaltos.append(cuadruplos.contador-1)

def p_llenarCuadruploPendiente(p):
    '''
    llenarCuadruploPendiente : empty
    '''
    pendiente = pilaSaltos.pop()
    retorno = pilaSaltos.pop()
    cuadruplos.generarCuadruploNuevo('GoTo', None, None, retorno)
    cuadruplos.llenarCuadruploPendiente(pendiente, cuadruplos.contador)

def p_llamada(p):
    '''
    llamada : ID existeFuncion PARENTESISINICIAL listaHiperexpresiones PARENTESISFINAL
            | ID PUNTO ID PARENTESISINICIAL listaHiperexpresiones PARENTESISFINAL
    '''
    p[0] = p[1]

def p_existeFuncion(p):
    '''
    existeFuncion : 
    '''
    if p[-1] not in directorio.tabla.keys():
        raise Exception("La función «"+ p[-1] + "» no existe. Favor de declararla.")

def p_listaHiperexpresiones(p):
    '''
    listaHiperexpresiones : hiperexpresion hiperexpresionesAdicionales
    '''

def p_hiperexpresionesAdicionales(p):
    '''
    hiperexpresionesAdicionales : COMA listaHiperexpresiones
                                | empty
    '''

def p_variable(p):
    '''
    variable : ID insertarAPilas arrayVariable
             | ID PUNTO ID
    '''
    p[0] = p[1]

def p_insertarAPilas(p):
    '''
    insertarAPilas : empty
    '''
    if p[-1] not in directorio.tabla[pilaContextos[-1]]["tablaVariables"].keys() and p[-1] not in directorio.tabla["global"]["tablaVariables"].keys():
        raise Exception("La variable «"+ p[-1] + "» no existe. Favor de declararla.")
    elif p[-1] in directorio.tabla[pilaContextos[-1]]["tablaVariables"].keys():
        pilaOperandos.append(p[-1])
        pilaTipos.append(directorio.tabla[pilaContextos[-1]]["tablaVariables"][p[-1]])
    elif p[-1] in directorio.tabla["global"]["tablaVariables"].keys():
        pilaOperandos.append(p[-1])
        pilaTipos.append(directorio.tabla["global"]["tablaVariables"][p[-1]])

def p_arrayVariable(p):
    '''
    arrayVariable : CORCHETEINICIAL hiperexpresion CORCHETEFINAL matrixVariable
                  | empty
    '''

def p_matrixVariable(p):
    '''
    matrixVariable : CORCHETEINICIAL hiperexpresion CORCHETEFINAL
                   | empty
    '''

def p_hiperexpresion(p):
    '''
    hiperexpresion : superexpresion validacionHiperexpresion andOr
    '''

def p_validacionHiperexpresion(p):
    '''
    validacionHiperexpresion : empty
    '''
    if len(pilaOperadores) > 0:
        if pilaOperadores[-1] == '&&' or pilaOperadores[-1] == '||':
            agregarCuadruplo()

def p_andOr(p):
    '''
    andOr : AND cuadruploHiperexpresion hiperexpresion
          | OR cuadruploHiperexpresion hiperexpresion
          | empty
    '''

def p_cuadruploHiperexpresion(p):
    '''
    cuadruploHiperexpresion : empty
    '''
    pilaOperadores.append(p[-1])

def p_superexpresion(p):
    '''
    superexpresion : exp validacionSuperexpresion comparaciones
    '''

def p_validacionSuperexpresion(p):
    '''
    validacionSuperexpresion : empty
    '''
    if len(pilaOperadores) > 0:
        if pilaOperadores[-1] == '>' or pilaOperadores[-1] == '>=' or pilaOperadores[-1] == '<' or pilaOperadores[-1] == '<=' or pilaOperadores[-1] == '==' or pilaOperadores[-1] == '<>':
            agregarCuadruplo()

def p_comparaciones(p):
    '''
    comparaciones : MAYORQUE cuadruploSuperexpresion superexpresion
                  | MAYORIGUALQUE cuadruploSuperexpresion superexpresion
                  | MENORQUE cuadruploSuperexpresion superexpresion
                  | MENORIGUALQUE cuadruploSuperexpresion superexpresion
                  | EQUIVALENTE cuadruploSuperexpresion superexpresion
                  | DIFERENTEDE cuadruploSuperexpresion superexpresion
                  | empty
    '''

def p_cuadruploSuperexpresion(p):
    '''
    cuadruploSuperexpresion : empty
    '''
    pilaOperadores.append(p[-1])

def p_exp(p):
    '''
    exp : termino validacionExp sumaRestaExpresiones
    '''

def p_validacionExp(p):
    '''
    validacionExp : empty
    '''
    if len(pilaOperadores) > 0:
        if pilaOperadores[-1] == '+' or pilaOperadores[-1] == '-':
            agregarCuadruplo()

def p_sumaRestaExpresiones(p):
    '''
    sumaRestaExpresiones : SUMA cuadruploExpresion exp
	                     | RESTA cuadruploExpresion exp
                         | empty
    '''

def p_cuadruploExpresion(p):
    '''
    cuadruploExpresion : empty
    '''
    pilaOperadores.append(p[-1])

def p_termino(p):
    '''
    termino : factor validacionTermino multiplicacionDivisionTerminos
    '''

def p_validacionTermino(p):
    '''
    validacionTermino : empty
    '''
    if len(pilaOperadores) > 0:
        if pilaOperadores[-1] == '*' or pilaOperadores[-1] == '/':
            agregarCuadruplo()

def p_multiplicacionDivisionTerminos(p):
    '''
    multiplicacionDivisionTerminos : MULTIPLICACION cuadruploTermino termino
	                               | DIVISION cuadruploTermino termino
                                   | empty
    '''

def p_cuadruploTermino(p):
    '''
    cuadruploTermino : empty
    '''
    pilaOperadores.append(p[-1])

def agregarCuadruplo():
    valorDer = pilaOperandos.pop()
    tipoDer = pilaTipos.pop()
    valorIzq = pilaOperandos.pop()
    tipoIzq = pilaTipos.pop()
    operador = pilaOperadores.pop()
    tipoResultado = cuboSemantico.validarTipos(tipoIzq, tipoDer, operador)
    if tipoResultado:
        temporal = avail.generarTemporalNuevo(tipoResultado)
        cuadruplos.generarCuadruploNuevo(operador, valorIzq, valorDer, temporal)
        pilaOperandos.append(temporal)
        pilaTipos.append(tipoResultado)
    else:
        raise Exception("Los tipos de los operandos no son compatibles.")
        print("")

def p_factor(p):
    '''
    factor : PARENTESISINICIAL agregarParentesis hiperexpresion PARENTESISFINAL eliminarParentesis
	       | var_cte
           | variable
           | llamada
    '''

def p_agregarParentesis(p):
    '''
    agregarParentesis : empty
    '''
    pilaOperadores.append('(')

def p_eliminarParentesis(p):
    '''
    eliminarParentesis : empty
    '''
    pilaOperadores.pop()

def p_var_cte(p):
    '''
    var_cte : CTE_I insertarEnteros
	        | CTE_F insertarFlotantes
            | CTE_STRING insertarStrings
            | CTE_BOOL insertarBooleanos
    '''
    p[0] = p[1]

def p_insertarEnteros(p):
    '''
    insertarEnteros : empty
    '''
    constantes.agregarConstante(p[-1], 'int')
    pilaOperandos.append(p[-1])
    pilaTipos.append(constantes.tabla[p[-1]])

def p_insertarFlotantes(p):
    '''
    insertarFlotantes : empty
    '''
    constantes.agregarConstante(p[-1], 'float')
    pilaOperandos.append(p[-1])
    pilaTipos.append(constantes.tabla[p[-1]])

def p_insertarStrings(p):
    '''
    insertarStrings : empty
    '''
    constantes.agregarConstante(p[-1], 'char')
    pilaOperandos.append(p[-1])
    pilaTipos.append(constantes.tabla[p[-1]])

def p_insertarBooleanos(p):
    '''
    insertarBooleanos : empty
    '''
    constantes.agregarConstante(p[-1], 'bool')
    pilaOperandos.append(p[-1])
    pilaTipos.append(constantes.tabla[p[-1]])

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print(f'Hay un error en la línea {p.lineno}. Se leyó un símbolo inesperado: {p.value!r}.')
    print("")
    exit()

parser = yacc(debug=True)
