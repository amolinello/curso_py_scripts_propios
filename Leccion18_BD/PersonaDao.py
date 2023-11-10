from Conexion import Conexion
from Persona import Persona
from Logger_base import log

# DAO = DATA ACCESS OBJECT

class PersonaDao:
    
    _SELECCIONAR = 'SELECT * FROM "personasAdmitidas"'
    _INSERTAR = 'INSERT INTO "personasAdmitidas"(nombre, apellido, mail) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE "personasAdmitidas" SET nombre = %s, apellido = %s, mail = %s WHERE id_persona = %s'
    _ELIMINAR = 'DELETE FROM "personasAdmitidas" WHERE id_persona = %s'

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                listaPersonas = []

                for registro in registros:
                    registroPersona = Persona(*registro)
                    listaPersonas.append(registroPersona)
                
                return listaPersonas

    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:

                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Persona a insertar: {persona}')
                return cursor.rowcount
    
    @classmethod
    def actualizar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:

                valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'Persona a actualizar: {persona}')
                return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:

                valores = (persona.id_persona, )
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f'Persona a borrar: {persona}')
                return cursor.rowcount

if __name__ == '__main__':

    # Eliminar un Objero
    personaEliminada = Persona(id_persona=20)
    personasEliminadas = PersonaDao.eliminar(personaEliminada)
    log.debug(personasEliminadas)

    # Actualizar un objeto
    #personaCambiada = Persona(20, 'Fabian', 'Molina', 'fmolina@mail.com')
    #personasCambiadas = PersonaDao.actualizar(personaCambiada)
    #log.debug(personasCambiadas)

    # Insertar un objeto
    #personaNueva = Persona(nombre='Armando', apellido='Muros', email='amuros@mail.com')
    #personasInsertadas = PersonaDao.insertar(personaNueva)
    #log.debug(personasInsertadas)

    # Seleccionar todos los objetos
    personas = PersonaDao.seleccionar()
    for persona in personas:
        log.debug(persona)