
# Si en una clase se agrega un metodo abstracto, toda la clase se vuelve abstracta
# PARA CONVERTIR LA CLASE EN ABSTRACTA SE TIENE QUE EXTENDER DE ABC = ABSTRACT BASE CLASS
from abc import ABC, abstractmethod

class FigurasGeometricas(ABC):
    def __init__(self, alto = 0, ancho = 0):
        self._alto = alto
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto
    
    @alto.setter
    def alto(self, alto):
        self._alto = alto

    @property
    def ancho(self):
        return self.ancho

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    @abstractmethod # Para considerarse un metodo abstracto
    def area(self):
        pass
    
    def __str__(self):
        return f'Tiene Alto {self._alto} y Ancho {self._ancho}'


# No se puede instanciar una clase abstracta
# Sirve para obligar a las clases hijas implementar los metodos abstractos