from ply.lex import lex

palabrasReservadas = {
    'program': 'PROGRAM',
    'var': 'VAR',
    'main': 'MAIN',
    'print': 'PRINT',
    'read': 'READ',
    'func': 'FUNC',
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'void': 'VOID',
    'return': 'RETURN',
    'for': 'FOR',
    'until': 'UNTIL',
    'while': 'WHILE',
    'if': 'IF',
    'else': 'ELSE'
}

tokens = [
        'SUMA',
        'RESTA',
        'MULTIPLICACION',
        'DIVISION',
        'MENORQUE',
        'MENORIGUALQUE',
        'MAYORQUE',
        'MAYORIGUALQUE',
        'IGUALA',
        'EQUIVALENTE',
        'DIFERENTEDE',
        'AND',
        'OR',
        'PARENTESISINICIAL',
        'PARENTESISFINAL',
        'LLAVEINICIAL',
        'LLAVEFINAL',
        'CORCHETEINICIAL',
        'CORCHETEFINAL',
        'COMA',
        'PUNTOYCOMA',
        'DOSPUNTOS',
        'ID', 
        'CTE_I', 
        'CTE_F',
        'CTE_STRING'] + list(palabrasReservadas.values())

t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'\/'
t_MENORQUE = r'<'
t_MENORIGUALQUE = r'<='
t_MAYORQUE = r'>'
t_MAYORIGUALQUE = r'>='
t_IGUALA = r'='
t_EQUIVALENTE = r'=='
t_DIFERENTEDE = r'<>'
t_AND = r'&&'
t_OR = r'\|\|'
t_PARENTESISINICIAL = r'\('
t_PARENTESISFINAL = r'\)'
t_LLAVEINICIAL = r'{'
t_LLAVEFINAL = r'}'
t_CORCHETEINICIAL = r'\['
t_CORCHETEFINAL = r']'
t_COMA = r','
t_PUNTOYCOMA = r';'
t_DOSPUNTOS = r':'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = palabrasReservadas.get(t.value, 'ID')
    return t

def t_CTE_I(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_CTE_F(t):
    r'\d+.\d+'
    t.value = float(t.value)    
    return t

def t_CTE_STRING(t):
    r'\"[a-zA-Z0-9_!\s]*\"'
    t.value = t.value[1:-1]
    return t

def t_númeroLínea(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

t_ignore = ' \t'

def t_error(t):
    print(f'Carácter no reconocido: {t.value[0]!r}.')
    t.lexer.skip(1)

lexer = lex()