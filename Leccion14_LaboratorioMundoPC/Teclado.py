from DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contador_teclado = 0
    def __init__(self, tipo_entrada, marca):
        DispositivoEntrada.__init__(self, tipo_entrada, marca)
        Teclado.contador_teclado += 1
        self.__id_teclado = Teclado.contador_teclado
    
    @property
    def id_teclado(self):
        return self.__id_teclado
    
    def __str__(self):
        return f'''
        {' Teclado: '.center(60, '-')}
        ID: {self.__id_teclado} / {DispositivoEntrada.__str__(self)}'''

if __name__ == '__main__':
    tecladoPrueba = Teclado('USB', 'Unitec')
    print(tecladoPrueba)
    tecladoPrueba.marca = 'Otra'
    tecladoPrueba.tipo_entrada = 'Cables'
    print(tecladoPrueba)

    tecladoPrueba2 = Teclado('USB C', 'HP')
    print(tecladoPrueba2)