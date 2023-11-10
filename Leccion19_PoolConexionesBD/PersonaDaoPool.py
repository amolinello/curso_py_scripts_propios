from ConexionPool import ConexionPool
from PersonaPool import PersonaPool
from CursorDelPool import CursorDelPool
from Logger_basePool import log

# DAO = DATA ACCESS OBJECT

class PersonaDaoPool:
    
    _SELECCIONAR = 'SELECT * FROM "personasAdmitidas"'
    _INSERTAR = 'INSERT INTO "personasAdmitidas"(nombre, apellido, mail) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE "personasAdmitidas" SET nombre = %s, apellido = %s, mail = %s WHERE id_persona = %s'
    _ELIMINAR = 'DELETE FROM "personasAdmitidas" WHERE id_persona = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            listaPersonas = []

            for registro in registros:
                registroPersona = PersonaPool(*registro)
                listaPersonas.append(registroPersona)
            
            return listaPersonas

        # with ConexionPool.obtenerConexion() as conexion:
        #     with conexion.cursor() as cursor:
        #         cursor.execute(cls._SELECCIONAR)
        #         registros = cursor.fetchall()
        #         listaPersonas = []

        #         for registro in registros:
        #             registroPersona = PersonaPool(*registro)
        #             listaPersonas.append(registroPersona)
                
        #         return listaPersonas

    @classmethod
    def insertar(cls, persona):
        
        with CursorDelPool() as cursor:

            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Persona a insertar: {persona}')
            return cursor.rowcount

        # with ConexionPool.obtenerConexion():
        #     with ConexionPool.obtenerCursor() as cursor:

        #         valores = (persona.nombre, persona.apellido, persona.email)
        #         cursor.execute(cls._INSERTAR, valores)
        #         log.debug(f'Persona a insertar: {persona}')
        #         return cursor.rowcount
    
    @classmethod
    def actualizar(cls, persona):
        
        with CursorDelPool() as cursor:

            valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Persona a actualizar: {persona}')
            return cursor.rowcount

        # with ConexionPool.obtenerConexion():
        #     with ConexionPool.obtenerCursor() as cursor:

        #         valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
        #         cursor.execute(cls._ACTUALIZAR, valores)
        #         log.debug(f'Persona a actualizar: {persona}')
        #         return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        
        with CursorDelPool() as cursor:

            valores = (persona.id_persona, )
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Persona a borrar: {persona}')
            return cursor.rowcount

        # with ConexionPool.obtenerConexion() as conexion:
        #     with conexion.cursor() as cursor:

        #         valores = (persona.id_persona, )
        #         cursor.execute(cls._ELIMINAR, valores)
        #         log.debug(f'Persona a borrar: {persona}')
        #         return cursor.rowcount

if __name__ == '__main__':

    # Eliminar un Objero
    #personaEliminada = PersonaPool(id_persona=20)
    #personasEliminadas = PersonaDaoPool.eliminar(personaEliminada)
    #log.debug(personasEliminadas)

    # Actualizar un objeto
    #personaCambiada = PersonaPool(20, 'Fabian', 'Molina', 'fmolina@mail.com')
    #personasCambiadas = PersonaDaoPool.actualizar(personaCambiada)
    #log.debug(personasCambiadas)

    # Insertar un objeto
    #personaNueva = PersonaPool(nombre='Ana', apellido='Ospina', email='aospina@mail.com')
    #personasInsertadas = PersonaDaoPool.insertar(personaNueva)
    #log.debug(personasInsertadas)

    # Seleccionar todos los objetos
    personas = PersonaDaoPool.seleccionar()
    for persona in personas:
        log.debug(persona)