from psycopg2 import pool
from LoggerBase import log
import sys

# Un pool permite almacenar varias sentencias a ejecutar en la base de datos de manera dinamica, con un mismo objeto de conexion

class Conexion:
    
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _HOST = '127.0.0.1'
    _DB_PORT = '5433'
    _DATABASE = 'test_db'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CON,
                    cls._MAX_CON,
                    user= cls._USERNAME,
                    password= cls._PASSWORD,
                    host= cls._HOST,
                    port= cls._DB_PORT,
                    database= cls._DATABASE)

                log.debug(f'Creacion de pool Exitosa {cls._pool}')
                return cls._pool

            except Exception as ex:
                log.error(f'Ocurrio un error: {ex}')
                sys.exit()

        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        # getcon() retorna un objeto de conexion hacia la base de datos
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexion obtenida del pool: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        # Devuelve el objeto de conexión al Pool de conexiones
        log.debug(f'Regresamos la conexion al pool: {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()

if __name__ == '__main__':

    conexion1 = Conexion.obtenerConexion()
    conexion2 = Conexion.obtenerConexion()
    conexion3 = Conexion.obtenerConexion()
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion4)
    conexion6 = Conexion.obtenerConexion()
