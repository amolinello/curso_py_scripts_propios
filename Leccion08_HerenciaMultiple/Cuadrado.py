from Color import Color
from FiguraGeometrica import FiguraGeometrica

class Cuadrado(Color, FiguraGeometrica):

    def __init__(self, color, lado):
        #super(Color).__init__(color)
        #super(FiguraGeometrica).__init__(lado, lado)
        Color.__init__(self, color)
        FiguraGeometrica.__init__(self, lado, lado)

    def area(self):
        return self._alto * self._ancho # Llama a la variable privada donde esta el valor de alto y ancho
    
    def __str__(self):
        return f'''
        El cuadrado tiene:
        {Color.__str__(self)}
        {FiguraGeometrica.__str__(self)}
        El area del cuadrado es:
        {self.area()}
        '''

if __name__ == '__main__':

    figuraRoja = Cuadrado('Rojo', 3)
    print(figuraRoja)

    print(Cuadrado.mro())

"""
MRO = Method Resolution Order

Permite conocer el orden en el que se llaman las clases padres:

print(NombreClaseHijo.mro())



Se modifia en orden de ingreso al metodo hijo
"""