
class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    @classmethod
    def crear_persona_vacia(cls):
        return cls(None, None)
        # Manda a llamar el metodo init

    @classmethod
    def crear_persona_con_valores(cls, nombre, apellido):
        return cls(nombre, apellido)

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}'

    # Este no sirve, lo que hace es que init sea este nuevo metodo inicializador
    #def __init__(self, nombre, apellido, edad):
    #    self.nombre = nombre
    #    self.apellido = apellido
    #    self.edad = edad

persona1 = Persona('Juan Carlos', 'Molinello')
persona2 = Persona('Andres', 'Salamanca')
persona_vacia = Persona.crear_persona_vacia()
persona_valores = Persona.crear_persona_con_valores('Luisa','Osa')

print(persona1)
print(persona2)
print(persona_vacia)
print(persona_valores)