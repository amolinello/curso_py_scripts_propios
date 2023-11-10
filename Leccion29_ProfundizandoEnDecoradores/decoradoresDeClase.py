# Decoradores de clase

# Permite modificar de madera programática nuestra clase
# Similar a los decoradores de funciones
#(metaprogramación)

#Decorador de clase
def decorador_repr(cls):
    print('Se ejecuta el decorador')
    print(f'Recibimos el objeto de la clase: {cls.__name__}')
    #Se ejecuta el decorador
    #Recibimos el objeto de la clase: Persona

    # Revisar los atributos de la clase con el método vars
    atributos = vars(cls)
    for nombre, valor in atributos.items():
        print(f'Nombre: {nombre}')
        print(f'Valor: {valor}')

    # Revisar si se sobreescribió el metodo init
    if '__init__' not in atributos:
        raise TypeError(f'{cls.__name__} No se ha sobreescrito el método init')

    # Inspeccionar una clase (No funciona en visual studio, primero se importa el modulo inspect - import inspect)
    #firma_init = inspect.signature(cls.__init__)
    #print(f'Firma del metodo init {firma_init}')

    # Si no se modifica nada debemos hacer un return el objeto que ingreso
    return cls

@decorador_repr
class Persona:
    def __init__ (self, nombre, apellido):
        print('Se ejecuta el inicializador')
        self._nombre = nombre
        self._apellido = apellido

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    def __repr__(self):
        return f'Persona({self._nombre}, {self._apellido})'

if __name__ == '__main__':
    persona1 = Persona('Armando', 'Muros')

    # Primero ejecuta el decorador y luego el inicializador
