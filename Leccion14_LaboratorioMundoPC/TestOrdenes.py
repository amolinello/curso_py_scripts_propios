
from Computadora import *
from Orden import Orden

if __name__ == '__main__':
    
    tecladoUno = Teclado('USB', 'La mejor')
    ratonUno = Raton('Wifi', 'Unitec')
    monitorUno = Monitor('Janus', 1250)
    computadoraGamer = Computadora('PC Gamer', monitorUno, tecladoUno, ratonUno)
    print(computadoraGamer)

    ratonDos = Raton('Cable', 'Pirata')
    tecladoDos = Teclado('Bluetooth', 'La 2da mejor')
    monitorDos = Monitor('Apple', 1900)
    computadoraNormal = Computadora('PC Normal', monitorDos, tecladoDos, ratonDos)
    print(computadoraNormal)

    monitorTres = Monitor('HP', 2300)
    tecladoTres = Teclado('Wifi', 'El 3er mejor')
    computadoraPirata = Computadora('El peor', monitorTres, tecladoTres, ratonUno)
    print(computadoraPirata)

    pcs = [computadoraGamer, computadoraNormal]

    ordenUno = Orden(pcs)
    print(ordenUno)

    ordenDos = Orden([computadoraNormal]) # Mirar como cambiar esto para poder ingresar sin que este en lista, opcional
    ordenDos.agregar_computadora(computadoraPirata)
    ordenDos.agregar_computadora(computadoraGamer)
    print('\n\n\n\n\n\n\n')
    print(ordenUno)
    print(ordenDos)

