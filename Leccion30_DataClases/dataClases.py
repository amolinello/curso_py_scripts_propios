# Modulo de python que provee decoradores y funciones a python

from dataclasses import dataclass
from typing import ClassVar

# Por default esta en True, pero se puede poner en false
# Para que los objetos no sean "Iguales"
# frozen es para especificar si son mutables o no, por default es False
@dataclass(eq=True, frozen=False)
class Persona:
    nombre: str
    apellido: str
    contador_personas: ClassVar[int] = 0

    def __post_init__(self):
        if not self.nombre:
            raise ValueError(f'Valor de nombre vacío: {self.nombre}')

if __name__ == '__main__':
    persona1 = Persona('Armando', 'Casas')
    print(persona1)
    #Variable de clase
    print(f'Variable de clase: {Persona.contador_personas}')
    #Variables de intancia:
    print(f'Variables de intancia: {persona1.__dict__}')

    #persona_vacia = Persona('', '')
    #print('Persona vacia',persona_vacia)

    # Revisar igualdad entre objetos
    persona2 = Persona('Armando', 'Casas')

    #Este es __eq__
    print(f'Objetos iguales?: {persona1 == persona2}')
    print(f'Objetos iguales?: {persona1 is persona2}')
    #coleccion = {persona1, persona2} # con frozen = True







