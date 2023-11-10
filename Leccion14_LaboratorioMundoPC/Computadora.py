from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado


class Computadora(Monitor, Teclado, Raton):
    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self.__id_computadora = Computadora.contador_computadoras
        self.__nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton
        
    # def __init__(self, nombre, monitorMarca, monitorTamaño, tecladoEntrada, tecladoMarca, ratonEntrada, ratonMarca):
    #     Monitor.__init__(self, monitorMarca, monitorTamaño)
    #     Teclado.__init__(self, tecladoEntrada, tecladoMarca)
    #     Raton.__init__(self, ratonEntrada, ratonMarca)
    #     Computadora.contador_computadoras += 1
    #     self.__id_computadora = Computadora.contador_computadoras
    #     self.__nombre = nombre
    

    @property
    def id_computadora(self):
        return self.__id_computadora

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    def __str__(self):
        # return f'''
        # Computadora: {self.__nombre}
        # ID: {self.__id_computadora}
        # {Monitor.__str__(self)}
        # {Teclado.__str__(self)}
        # {Raton.__str__(self)}
        # '''
        return f'''
        {''.center(60, '*')}
        Computadora: {self.__nombre}
        ID: {self.__id_computadora}
        {self._monitor}
        {self._teclado}
        {self._raton}
        '''

if __name__ == '__main__':
    # computadoraPrueba = Computadora('La Maquina', 'HP', 1600, 'USB C', 'Muy Buena', 'Bluetooth', 'Iraton')
    # print(computadoraPrueba)
    tecladoPrueba = Teclado('USB', 'La mejor')
    ratonPrueba = Raton('Wifi', 'Unitec')
    monitorPrueba = Monitor('Janus', 1250)
    computadoraConEntradas = Computadora('PC Gamer', monitorPrueba, tecladoPrueba, ratonPrueba)
    print(computadoraConEntradas)

    tecladoPrueba = Teclado('Bluetooth', 'La 2da mejor')
    computadoraConEntradas2 = Computadora('PC Normal', monitorPrueba, tecladoPrueba, ratonPrueba)
    print(computadoraConEntradas2)