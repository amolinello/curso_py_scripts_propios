from FuncionPadre import *

# print(Vehiculo(4, 'Mazda', 180)) # Llama a la clase Vehiculo con esos datos y llama al metodo str

class moto(Vehiculo):

    def __init__(self, precio, marca, ruedas, velocidad_maxima):

        super().__init__(ruedas, marca, velocidad_maxima)
        self._precio = precio

    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, precio):
        self._precio = precio

    def __str__(self):
        return super().__str__() + f' \nTodo por un precio de: {100} o de ' + str(self._precio)

motos = moto(1000, 'Yamaha', 2, 210)
print(motos)
    