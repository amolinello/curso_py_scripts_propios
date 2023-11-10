# En python cada archivo puede tener muchas clases

class Vehiculo:

    def __init__(self, ruedas = 0, marca = " ", velocidad_maxima = 0):

        self._ruedas = ruedas
        self._marca = marca
        self._velocidad_maxima = velocidad_maxima
    
    @property
    def ruedas(self):
        return self._ruedas
    
    @ruedas.setter
    def ruedas(self, ruedas):
        self._ruedas = ruedas
    
    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def velocidad_maxima(self):
        return self._velocidad_maxima
    
    @velocidad_maxima.setter
    def velocidad_maxima(self, vmax):
        self._velocidad_maxima = vmax

    def __str__(self):
        return f'El Vehiculo de marca: {self._marca}, con {self._ruedas} ruedas y alcanza una velocidad máxima de {self._velocidad_maxima}'
    
# Carga pesada es hija de la clase Vehiculo

class CargaPesada(Vehiculo):
    def __init__(self, peso):

        # Super sirve para llamar lo que pertenezca a la clase padre, en este caso su metodo inicializador y sus getter y setters
        super().__init__(6, None, 200)

        self._peso = peso

    @property
    def peso(self):
        return self._peso
    
    @peso.setter
    def peso(self, peso):
        self._peso = peso

if __name__ == '__main__':

    vehiculo_pesado = CargaPesada(600)
    print(vehiculo_pesado.peso)
    print(vehiculo_pesado.marca)
    print(vehiculo_pesado.ruedas)
    print(vehiculo_pesado.velocidad_maxima)


