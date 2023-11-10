from Logger_basePool import log

class PersonaPool:
    
    def __init__(self, id_persona = None, nombre = None, apellido = None, email = None):
        self.__id_persona = id_persona
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email

    @property
    def id_persona(self):
        return self.__id_persona
    
    @id_persona.setter
    def id_persona(self, id):
        self.__id_persona = id

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email

    def __str__(self):
        return f'ID: {self.__id_persona}, Nombre: {self.__nombre}, Apellido: {self.__apellido}, Email: {self.__email}'

if __name__ == '__main__':
    caminante = PersonaPool(123, 'Ana', 'Guerrero', 'aguerrero@mail.com')
    log.debug(caminante)

    # Simular un insert

    otro_caminante = PersonaPool(nombre='Camila', apellido='Marquez', email='cmarquez@mail.com')
    log.debug(otro_caminante)