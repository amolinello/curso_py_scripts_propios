from PadreAbstracto import FigurasGeometricas
from PadreColor import PadreColor

class Cuadrados(PadreColor, FigurasGeometricas):

    def __init__(self, color, lado):
        #super(Color).__init__(color)
        #super(FiguraGeometrica).__init__(lado, lado)
        PadreColor.__init__(self, color)
        FigurasGeometricas.__init__(self, lado, lado)

    def area(self):
        return self._alto * self._ancho # Llama a la variable privada donde esta el valor de alto y ancho
    
    def __str__(self):
        return f'''
        El cuadrado tiene:
        {PadreColor.__str__(self)}
        {FigurasGeometricas.__str__(self)}
        El area del cuadrado es:
        {self.area()}
        '''

if __name__ == '__main__':

    figuraRoja = Cuadrados('Rojo', 3)
    print(figuraRoja)
    print(Cuadrados.mro())