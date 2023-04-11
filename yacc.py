from lex import lexer, tokens
from ply.yacc import yacc

def p_programa(p):
    '''
    programa : PROGRAM ID PUNTOYCOMA clases vars2 funciones MAIN PARENTESISINICIAL PARENTESISFINAL vars2 bloque
    '''

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
    bloqueAtributos : LLAVEINICIAL listaVars LLAVEFINAL
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

def p_vars(p):
    '''
    vars : VAR listaVars
    '''

def p_listaVars(p):
    '''
    listaVars : listaIDs DOSPUNTOS tipo PUNTOYCOMA varsAdicionales
    '''

def p_listaIDs(p):
    '''
    listaIDs : ID array comasAdicionales
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

def p_comasAdicionales(p):
    '''
    comasAdicionales : COMA listaIDs
                     | empty
    '''

def p_varsAdicionales(p):
    '''
    varsAdicionales : listaVars
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

def p_asignacion(p):
    '''
    asignacion : variable IGUALA hiperexpresion PUNTOYCOMA
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
    listaExpresiones : hiperexpresion expresionesAdicionales
                     | CTE_STRING expresionesAdicionales
    '''

def p_expresionesAdicionales(p):
    '''
    expresionesAdicionales : COMA listaExpresiones
                           | empty
    '''

def p_lectura(p):
    '''
    lectura : READ PARENTESISINICIAL listaVariables PARENTESISFINAL PUNTOYCOMA
    '''

def p_listaVariables(p):
    '''
    listaVariables : variable variablesAdicionales
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
    '''

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
    hiperexpresion : superexpresion andOr
    '''

def p_andOr(p):
    '''
    andOr : AND superexpresion
          | OR superexpresion
          | empty
    '''

def p_superexpresion(p):
    '''
    superexpresion : exp comparaciones
    '''

def p_comparaciones(p):
    '''
    comparaciones : MAYORQUE exp
                  | MAYORIGUALQUE exp
                  | MENORQUE exp
                  | MENORIGUALQUE exp
                  | EQUIVALENTE exp
                  | DIFERENTEDE exp
                  | empty
    '''

def p_exp(p):
    '''
    exp : termino sumaRestaExpresiones
    '''

def p_sumaRestaExpresiones(p):
    '''
    sumaRestaExpresiones : SUMA exp
	                     | RESTA exp
                         | empty
    '''

def p_termino(p):
    '''
    termino : factor multiplicacionDivisionTerminos
    '''

def p_multiplicacionDivisionTerminos(p):
    '''
    multiplicacionDivisionTerminos : MULTIPLICACION termino
	                               | DIVISION termino
                                   | empty
    '''

def p_factor(p):
    '''
    factor : PARENTESISINICIAL hiperexpresion PARENTESISFINAL
	       | var_cte
           | variable
           | llamada
    '''

def p_var_cte(p):
    '''
    var_cte : CTE_I
	        | CTE_F
    '''

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print(f'Hay un error en la línea {p.lineno}. Se leyó un símbolo inesperado: {p.value!r}.')
    exit()

parser = yacc(debug=True)