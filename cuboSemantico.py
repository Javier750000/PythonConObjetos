'''
int: 1
float: 2
char: 3
bool: 4
+: 11
-: 12
*: 13
/: 14
<: 15
<=: 16
>: 17
>=: 18
=: 19
==: 20
<>: 21
&&: 22
||: 23
Error: -1
'''

class CuboSemantico:
    def __init__(self):
        self.table = {
            ('int', 'int', '+'): 'int',
            ('int', 'int', '-'): 'int',
            ('int', 'int', '*'): 'int',
            ('int', 'int', '/'): 'int',
            ('int', 'int', '<'): 'bool',
            ('int', 'int', '<='): 'bool',
            ('int', 'int', '>'): 'bool',
            ('int', 'int', '>='): 'bool',
            ('int', 'int', '='): 'int',
            ('int', 'int', '=='): 'bool',
            ('int', 'int', '<>'): 'bool',

            ('int', 'float', '+'): 'float',
            ('int', 'float', '-'): 'float',
            ('int', 'float', '*'): 'float',
            ('int', 'float', '/'): 'float',
            ('int', 'float', '<'): 'bool',
            ('int', 'float', '<='): 'bool',
            ('int', 'float', '>'): 'bool',
            ('int', 'float', '>='): 'bool',
            ('int', 'float', '='): 'int',
            ('int', 'float', '=='): 'bool',
            ('int', 'float', '<>'): 'bool',

            ('float', 'int', '+'): 'float',
            ('float', 'int', '-'): 'float',
            ('float', 'int', '*'): 'float',
            ('float', 'int', '/'): 'float',
            ('float', 'int', '<'): 'bool',
            ('float', 'int', '<='): 'bool',
            ('float', 'int', '>'): 'bool',
            ('float', 'int', '>='): 'bool',
            ('float', 'int', '='): 'float',
            ('float', 'int', '=='): 'bool',
            ('float', 'int', '<>'): 'bool',

            ('float', 'float', '+'): 'float',
            ('float', 'float', '-'): 'float',
            ('float', 'float', '*'): 'float',
            ('float', 'float', '/'): 'float',
            ('float', 'float', '<'): 'bool',
            ('float', 'float', '<='): 'bool',
            ('float', 'float', '>'): 'bool',
            ('float', 'float', '>='): 'bool',
            ('float', 'float', '='): 'float',
            ('float', 'float', '=='): 'bool',
            ('float', 'float', '<>'): 'bool',

            ('char', 'char', '='): 'char',
            ('char', 'char', '=='): 'bool',
            ('char', 'char', '<>'): 'bool',

            ('bool', 'bool', '='): 'bool',
            ('bool', 'bool', '=='): 'bool',
            ('bool', 'bool', '<>'): 'bool',
            ('bool', 'bool', '&&'): 'bool',
            ('bool', 'bool', '||'): 'bool',
        }

    def validarTipos(self, tipoIzq, tipoDer, operador):
        if (tipoIzq, tipoDer, operador) in self.table:
            return self.table[(tipoIzq, tipoDer, operador)]
        return None
