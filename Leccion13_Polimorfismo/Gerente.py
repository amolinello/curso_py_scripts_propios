from Empleado import Empleado

class Gerente(Empleado):

    def __init__(self, nombre, sueldo, departamento):
        self._departamento = departamento
        super().__init__(nombre, sueldo) # Como solo hereda de 1 clase, se llama por super
                                         # Cuando herede de mas clases se llama con Empleado.__init__(nombre, sueldo)
    
    @property
    def departamento(self):
        return self._departamento
    
    @departamento.setter
    def departamento(self, departamento):
        self._departamento = departamento
    
    def __str__(self):
        return f'Datos del superior:\n{super().__str__()}, Departamento: {self._departamento}'

if __name__ == '__main__':
    sami = Gerente('Sami Gata', 6000000, 'Gatuno')
    print(sami)
    # print(sami._departamento) # se puede llamar el atributo
    # sami._departamento = 'otro' # Se puede cambiar el valor del atributo, no se deberia hacer ya que es privada
    # print(sami)