class FiguraGeometrica:

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
    
    def __str__(self):
        return f'Tiene Alto {self._alto} y Ancho {self._ancho}'
        