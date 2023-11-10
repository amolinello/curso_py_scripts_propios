from DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contador_raton = 0
    def __init__(self, tipo_entrada, marca):
        DispositivoEntrada.__init__(self, tipo_entrada, marca)
        Raton.contador_raton += 1
        self.__id_raton = Raton.contador_raton
    
    @property
    def id_raton(self):
        return self.__id_raton
    
    def __str__(self):
        return f'''
        {' Ratón: '.center(60, '-')}
        ID: {self.__id_raton} / {DispositivoEntrada.__str__(self)}'''

if __name__ == '__main__':
    ratonPrueba = Raton('USB', 'Unitec')
    print(ratonPrueba)
    ratonPrueba.marca = 'Otra'
    ratonPrueba.tipo_entrada = 'Cables'
    print(ratonPrueba)

    ratonPrueba2 = Raton('USB C', 'HP')
    print(ratonPrueba2)