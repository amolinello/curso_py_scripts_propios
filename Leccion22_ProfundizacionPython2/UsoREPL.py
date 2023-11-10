#REPL = Read Evaluate Print Loop

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, id: {hex(id(self)).upper()}'

if __name__ == '__main__':
    civil = Persona('Juan', 'Molinello')
    print(civil)


    # None = Ausencia de valor
    variable = None

    if variable:
        print('Verdadera')
        print(type(variable))
    else:
        print('Falso')
        print(type(variable))

    '''
    Formas de generar bool False
    1. Comilla vacia "" o ''
    2. Lista vacia: []
    3. Tupla vacia: ()
    4. Diccionario vacio: {}
    5. Entero: 0
    6. Flotante: 0.0
    7. bool: False
    8. None


    '''