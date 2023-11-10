from psycopg2 import pool
from Logger_basePool import log
import sys

# Un pool permite almacenar varias sentencias a ejecutar en la base de datos de manera dinamica, con un mismo objeto de conexion

class ConexionPool:
    
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _HOST = '127.0.0.1'
    _DB_PORT = '5433'
    _DATABASE = 'test_db'
    _MINIMO_CONEXION = 1
    _MAXIMO_CONEXION = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MINIMO_CONEXION,
                    cls._MAXIMO_CONEXION,
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

    conexion1 = ConexionPool.obtenerConexion()
    conexion2 = ConexionPool.obtenerConexion()
    conexion3 = ConexionPool.obtenerConexion()
    conexion4 = ConexionPool.obtenerConexion()
    conexion5 = ConexionPool.obtenerConexion()
    ConexionPool.liberarConexion(conexion3)
    conexion6 = ConexionPool.obtenerConexion()
    ConexionPool.cerrarConexiones()
    # conexion6 = ConexionPool.obtenerConexion() # La 6ta conexión ya muestra error