import psycopg2 as bd
from Logger_base import log
import sys

class Conexion:
    
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _HOST = '127.0.0.1'
    _DB_PORT = '5433'
    _DATABASE = 'test_db'
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(
                    user= cls._USERNAME,
                    password= cls._PASSWORD,
                    host= cls._HOST,
                    port= cls._DB_PORT,
                    database= cls._DATABASE)

                log.debug(f'Conexion exitosa: {cls._conexion}')
                return cls._conexion

            except BaseException as ex:
                log.error(f'Ocurrio un error con la conexion: {ex}')

                sys.exit() # Termina por completo el programa
        
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()

                log.debug(f'Abrio correctamente el cursor: {cls._cursor}')
                return cls._cursor

            except Exception as ex:
                log.error(f'Ocurrio un error al obtener el cursor: {ex}')

                sys.exit() # Termina por completo el programa
                
        else:
            return cls._cursor

if __name__ == '__main__':

    pruebaConexion = Conexion()
    cursor = pruebaConexion.obtenerCursor()
    sentencia = 'SELECT * FROM "personasAdmitidas"'
    cursor.execute(sentencia)
    registros = cursor.fetchall()
    print(registros)