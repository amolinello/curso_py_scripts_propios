
# _nombre => Es para indicar que no se debería modificar
# tanto para atibutos como metodos

from mi_modulo import funcion_publica
from mi_modulo import _funcion_protegida # con * da error
from mi_modulo import *

class MiClase:
    def __init__(self):
        self.mi_variable_publica = 10
        self._mi_variable_protegida = 11
        self.__mi_variable_privada = 12

if __name__ == "__main__":

    # Usar el guion bajo al final para palabras protegidas
    class_ = 1
    print(class_)
    '''
    objeto = MiClase()
    print(objeto.mi_variable_publica)
    print(objeto.__mi_variable_privada) # Salta error

    # Acceder a las funciones del modulo importado

    # Si se usa el import con * la función protegida da error
    funcion_publica()
    _funcion_protegida() # Sale ModuleNotFoundError
    '''

    lista, *_, cosas = 1,2,3,4,5,6,7,8,9

    print(lista) # 1
    print(_) # [2,3,4,5,6,7,8]
    print(cosas) # 9