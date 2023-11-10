class Persona:
    contador_personas = 0


    def __init__(self, nombre, edad):
        self._id_persona = Persona._generar_sigiente_id()
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevoNombre):
        self._nombre = nuevoNombre
    
    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nuevaEdad):
        self._edad = nuevaEdad

    @classmethod
    def _generar_sigiente_id(cls):
        cls.contador_personas += 1
        return cls.contador_personas


    def __str__(self):
        return f'''
        ID: {self._id_persona},
        Nombre: {self._nombre},
        Edad: {self._edad}
        '''

juan_carlos = Persona('Juan Carlos', 59)
andres = Persona('Andres', 24)
ana = Persona('Ana', 34)

print(juan_carlos)
print(andres)
print(ana)