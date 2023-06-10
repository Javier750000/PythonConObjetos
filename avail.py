class Avail:
    def __init__(self):
        self.table = {
            'globales': {'int': [0, 0, 2999], 'float': [3000, 3000, 5999], 'char': [6000, 6000, 8999], 'bool': [9000, 9000, 11999]},
            'locales': {'int': [12000, 12000, 14999], 'float': [15000, 15000, 17999], 'char': [18000, 18000, 20999], 'bool': [21000, 21000, 23999]},
            'temporales': {'int': [24000, 24000, 26999], 'float': [27000, 27000, 29999], 'char': [30000, 30000, 32999], 'bool': [33000, 33000, 35999]},
            'constantes': {'int': [36000, 36000, 38999], 'float': [39000, 39000, 41999], 'char': [42000, 42000, 44999], 'bool': [45000, 45000, 47999]}
        }

    def generarDireccionNueva(self, tipo, contexto):
        if self.table[contexto][tipo][0] > self.table[contexto][tipo][2]:
            raise Exception("Ya no hay espacio en memoria para más variables.")
        else:
            direccionActual = self.table[contexto][tipo][0]
            self.table[contexto][tipo][0] += 1
            return direccionActual

    def generarDireccionesNueva(self, tipo, contexto, tamaño):
        if self.table[contexto][tipo][0] + tamaño - 1 > self.table[contexto][tipo][2]:
            raise Exception("Ya no hay espacio en memoria para más variables.")
        else:
            direccionActual = self.table[contexto][tipo][0]
            self.table[contexto][tipo][0] += tamaño
            return direccionActual

    def generarGlobalNuevo(self, tipo):
        if self.table['globales'][tipo][0] > self.table['globales'][tipo][2]:
            raise Exception("Ya no hay espacio en memoria para más variables.")
        else:
            direccionGlobal = self.table['globales'][tipo][0]
            self.table['globales'][tipo][0] += 1
            return direccionGlobal

    def generarTemporalNuevo(self, tipo):
        if self.table['temporales'][tipo][0] > self.table['temporales'][tipo][2]:
            raise Exception("Ya no hay espacio en memoria para más variables.")
        else:
            direccionTemporal = (self.table['temporales'][tipo][0])
            self.table['temporales'][tipo][0] += 1
            return direccionTemporal

    def reinicializar(self):
        self.table['locales']['int'][0] = self.table['locales']['int'][1]
        self.table['locales']['float'][0] = self.table['locales']['float'][1]
        self.table['locales']['char'][0] = self.table['locales']['char'][1]
        self.table['locales']['bool'][0] = self.table['locales']['bool'][1]

        self.table['temporales']['int'][0] = self.table['temporales']['int'][1]
        self.table['temporales']['float'][0] = self.table['temporales']['float'][1]
        self.table['temporales']['char'][0] = self.table['temporales']['char'][1]
        self.table['temporales']['bool'][0] = self.table['temporales']['bool'][1]

    def regresarDireccionesOcupadas(self, contexto):
        tipos = self.table[contexto]
        direccionesOcupadas = {tipo: arr[0] - arr[1] for tipo, arr in tipos.items()}
        return direccionesOcupadas
