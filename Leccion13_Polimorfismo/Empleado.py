
# El polimorfismo es multiples formas en tiempos de ejecución
# Ejecutar varios metodos de diferentes objetos en una clase

# Ejemplo, clase empleado con los atributos nombre y sueldo, con su clase str que retorna nombre y sueldo
# la clase gerente que hereda de la clase empleado
# La clase gerente tiene el atributo departamento y en su clase str, trae la de empleados y le agrega departamento

class Empleado:
    def __init__(self, nombre, sueldo):
        self._nombre = nombre
        self._sueldo = sueldo
    
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def sueldo(self):
        return self._sueldo
    
    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo
    
    def __str__(self):
        return f'Nombre: {self._nombre}, Sueldo: {self._sueldo}'

    def mostrar_detalles(self):
        return self.__str__()

if __name__ == '__main__':
    persona1 = Empleado('Juan Carlos', 1600000)
    print(persona1)