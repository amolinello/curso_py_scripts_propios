# Generar un string o cadena con el estado del objeto
# REPR es mas usado por los programadores
# STR es mas usado para el usuario final


# Representacion de objetos: str, repr y format - Estos pertenecen a la clase object

# print(dir(object))

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    # REPR es mas usado por los programadores
    def __repr__(self):
        #return f'Persona(nombre={self.nombre},apellido={self.apellido})'
        return f'{self.__class__.__name__}(nombre={self.nombre},apellido={self.apellido})'

    # STR es mas usado para el usuario final u otros sistemas
    # Por default siempre llama al repr
    def __str__(self):
        return f'{self.__class__.__name__}: {self.nombre} {self.apellido}'

    # Por default es STR el que se implementa y se manda a llamar cuando se usa el f''
    def __format__(self, __format_spec: str):
        return f'{self.__class__.__name__} con nombre: {self.nombre} y apellido: {self.apellido}'

if __name__ == '__main__':
    persona1 = Persona('Juan', 'Molinello')
    print(persona1)
    print(f'Mi objeto Persona: {persona1!r}') # llamar especificamen el metodo repr

    # Si se manda a llamar el metodo str, por default imprime el repr
    # print(persona1.__str__())

    print(persona1) # El metodo print llama automaticamente el metodo STR
    print(f'{persona1}') # El metodo f'' llama automaticamente el metodo format




