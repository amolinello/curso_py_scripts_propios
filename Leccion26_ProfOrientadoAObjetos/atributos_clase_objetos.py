class Persona:
    contador_personas = 0

    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido


if __name__ == '__main__':
    persona1 = Persona('Juan', 'Molinello')
    persona2 = Persona('Andres', 'Salamanca')
    print(persona1.__dict__) # Entrega un diccionario con los atributos asociados al objeto, no a la clase

    # Crear un atributo al momento
    persona1.contador_personas = 10

    print(persona1.contador_personas) # Modifica la variable en el objeto, pero no en la clase
    print(Persona.contador_personas) # Este podría modificar todas las clases

    print(persona1.__dict__) # Contador persona ya pasa a estar asociado al objeto y no a la clase

    Persona.contador_personas = 35 # Como se asocio contador persona en el objeto, cambia solo los objetos que no 
                                    # tocaran nada de esta variable de clase

    print('Este es persona uno modificada', persona1.contador_personas)
    print(Persona.contador_personas)
    print('Este es persona 2 sin modificar', persona2.contador_personas)

    print(persona1.__dict__)
    print(persona2.__dict__)

    # Asociar un atributo de clase de manera rapida
    Persona.variableNueva = 12
    
    print('Este es persona uno modificada', persona1.variableNueva)
    print(Persona.contador_personas)
    print('Este es persona 2 sin modificar', persona2.variableNueva)
    persona3 = Persona('Camila','Ramirez')
    print('Este es persona tres sin modificar', persona3.variableNueva)
    Persona.variableNueva = 44

    print('Este es persona uno modificada', persona1.variableNueva)
    print(Persona.contador_personas)
    print('Este es persona 2 sin modificar', persona2.variableNueva)
    persona3 = Persona('Camila','Ramirez')
    print('Este es persona tres sin modificar', persona3.variableNueva)
    
    print(persona1.__dict__)
    print(persona2.__dict__)

