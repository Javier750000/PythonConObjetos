from lex import lexer, tokens
from ply.yacc import yacc
from directorioProcedimientos import Directorio
from avail import Avail
from cuadruplos import Cuadruplos
from cuboSemantico import CuboSemantico
from constantes import Constantes

directorio = Directorio()
avail = Avail()
cuadruplos = Cuadruplos()
cuboSemantico = CuboSemantico()
constantes = Constantes()
pilaOperandos = []
pilaOperadores = []
pilaSaltos = []
pilaVariableControl = []
pilaDimensiones = []

def p_programa(p):
    '''
    programa : PROGRAM inicializarDirectorio ID PUNTOYCOMA clases vars2 funciones bloque MAIN PARENTESISINICIAL PARENTESISFINAL vars2 bloque
    '''
    print("Variables función:", p[12]);
    print("")
    '''
    directorio.agregarFuncion(nombreFuncion=p[9], tipoFuncion='void', variablesFuncion=p[12])
    '''
    print(cuadruplos.listaCuadruplos)
    print("")

def p_inicializarDirectorio(p):
    '''
    inicializarDirectorio : empty
    '''
    directorio.contextoGlobal()

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
    funcionSimple : FUNC tipo ID PARENTESISINICIAL param PARENTESISFINAL vars2 bloqueFuncional funciones
    '''

def p_funcionVoid(p):
    '''
    funcionVoid : FUNC VOID ID PARENTESISINICIAL param PARENTESISFINAL vars2 bloque funciones
    '''

def p_param(p):
    '''
    param : tipo ID paramsAdicionales
          | empty
    '''

def p_paramsAdicionales(p):
    '''
    paramsAdicionales : COMA param
                      | empty
    '''

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
    listaVarsSimples : tipo DOSPUNTOS listaIDsSimples PUNTOYCOMA varsAdicionales
    '''
    p[0] = p[3]

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
    '''
    p[0] += (p[1] + p[3])
    '''

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

    '''
    Este código está fallando.
    
    if len(p) == 2:
        p[0] += p[1]
    else:
        p[0] = []
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
    '''

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
    asignacion : variable IGUALA hiperexpresion PUNTOYCOMA
               | variable IGUALA CTE_STRING PUNTOYCOMA 
    '''
    valorVariable = p[1]
    '''
    valorHiperexpresion, tipoHiperexpresion = pilaOperandos.pop()
    tipoResultado = cuboSemantico.validarTipos(tipoVariable, tipoHiperexpresion, '=')
    if tipoResultado:
        cuadruplos.generarCuadruploNuevo('=', valorHiperexpresion, None, valorVariable)
    else:
        print(f'Los tipos de la hiperexpresión y de la variable no son compatibles.')
        print("")
    '''

def p_condicion(p):
    '''
    condicion : IF PARENTESISINICIAL hiperexpresion PARENTESISFINAL bloque bloqueCondicional
    '''

def p_bloqueCondicional(p):
    '''
    bloqueCondicional : ELSE bloque
                      | empty
    '''

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
    condicionFuncional : IF PARENTESISINICIAL hiperexpresion PARENTESISFINAL bloqueFuncional bloqueCondicionalFuncional
    '''

def p_bloqueCondicionalFuncional(p):
    '''
    bloqueCondicionalFuncional : ELSE bloqueFuncional
                               | empty
    '''

def p_escritura(p):
    '''
    escritura : PRINT PARENTESISINICIAL listaExpresiones PARENTESISFINAL PUNTOYCOMA
    '''

def p_listaExpresiones(p):
    '''
    listaExpresiones : hiperexpresion cuadruploEscritura expresionesAdicionales
                     | CTE_STRING cuadruploEscritura expresionesAdicionales
    '''

def p_expresionesAdicionales(p):
    '''
    expresionesAdicionales : COMA cuadruploEscritura listaExpresiones
                           | empty
    '''

def p_cuadruploEscritura(p):
    '''
    cuadruploEscritura : empty
    '''
    listaOperandos = pilaOperandos.pop()
    cuadruplos.generarCuadruploNuevo('print', None, None, listaOperandos)

def p_lectura(p):
    '''
    lectura : READ PARENTESISINICIAL listaVariables PARENTESISFINAL PUNTOYCOMA
    '''

    '''
    for variable in p[3]:
        cuadruplos.generarCuadruploNuevo('read', None, None, variable)
    '''

def p_listaVariables(p):
    '''
    listaVariables : variable variablesAdicionales
    '''

    '''
    p[0] = [p[1]] + p[2]
    '''

def p_variablesAdicionales(p):
    '''
    variablesAdicionales : COMA listaVariables
                         | empty
    '''

def p_cicloFor(p):
    '''
    cicloFor : FOR PARENTESISINICIAL ID IGUALA hiperexpresion UNTIL hiperexpresion PARENTESISFINAL bloque
    '''

def p_cicloWhile(p):
    '''
    cicloWhile : WHILE PARENTESISINICIAL hiperexpresion PARENTESISFINAL bloque
    '''

def p_llamada(p):
    '''
    llamada : ID PARENTESISINICIAL listaHiperexpresiones PARENTESISFINAL
            | ID PUNTO ID PARENTESISINICIAL listaHiperexpresiones PARENTESISFINAL
    '''

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
    variable : ID arrayVariable
             | ID PUNTO ID
    '''
    p[0] = p[1]

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
    hiperexpresion : superexpresion cuadruploHiperexpresion andOr
    '''

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
    agregarCuadruplo(['&&', '||'])

def p_superexpresion(p):
    '''
    superexpresion : exp cuadruploSuperexpresion comparaciones
    '''

def p_comparaciones(p):
    '''
    comparaciones : MAYORQUE cuadruploSuperexpresion exp
                  | MAYORIGUALQUE cuadruploSuperexpresion exp
                  | MENORQUE cuadruploSuperexpresion exp
                  | MENORIGUALQUE cuadruploSuperexpresion exp
                  | EQUIVALENTE cuadruploSuperexpresion exp
                  | DIFERENTEDE cuadruploSuperexpresion exp
                  | empty
    '''

def p_cuadruploSuperexpresion(p):
    '''
    cuadruploSuperexpresion : empty
    '''
    agregarCuadruplo(['>', '>=', '<', '<=', '==', '<>'])

def p_exp(p):
    '''
    exp : termino cuadruploExpresion sumaRestaExpresiones
    '''

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
    agregarCuadruplo(['+', '-'])

def p_termino(p):
    '''
    termino : factor cuadruploTermino multiplicacionDivisionTerminos
    '''

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
    agregarCuadruplo(['*', '/'])


def agregarCuadruplo(listaOperadores):
    if pilaOperadores and pilaOperadores[-1] in listaOperadores:
        valorDer, tipoDer = pilaOperandos.pop()
        valorIzq, tipoIzq = pilaOperandos.pop()
        operador = pilaOperadores.pop()
        tipoResultado = cuboSemantico.validarTipos(tipoIzq, tipoDer, operador)
        if tipoResultado:
            temporal = avail.generarTemporalNuevo(tipoResultado)
            cuadruplos.generarCuadruploNuevo(operador, valorIzq, valorDer, temporal)
            pilaOperandos.append(temporal)
        else:
            print(f'Los tipos de los operandos no son compatibles.')
            print("")

def p_factor(p):
    '''
    factor : PARENTESISINICIAL agregarParentesis hiperexpresion PARENTESISFINAL eliminarParentesis
	       | var_cte
           | variable
           | llamada
           | empty
    '''
    if len(p) == 2:
        temporal = p[1]
        pilaOperandos.append(temporal)

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
    var_cte : CTE_I
	        | CTE_F
    '''
    p[0] = p[1]

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print(f'Hay un error en la línea {p.lineno}. Se leyó un símbolo inesperado: {p.value!r}.')
    print("")
    exit()

parser = yacc(debug=True)