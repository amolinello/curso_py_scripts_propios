
class Orden:
    contador_ordenes = 0
    def __init__(self, computadoras):
        Orden.contador_ordenes += 1
        self.__id_orden = Orden.contador_ordenes
        self.__computadoras = computadoras
    
    @property
    def id_orden(self):
        return self.__id_orden

    def agregar_computadora(self, computadora):
        self.__computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ''
        for computadora in self.__computadoras:
            computadoras_str += computadora.__str__()

        return f'''
        La Orden: {self.__id_orden}
        Computadoras:
        {computadoras_str}
        '''
    
