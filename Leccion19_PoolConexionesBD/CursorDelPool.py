
# With es resource manager
from Logger_basePool import log
from ConexionPool import ConexionPool


class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug('Inicio del método with __enter__')
        self._conexion = ConexionPool.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, traceback_excepcion):
        log.debug('Se ejecuta método __exit__')
        if valor_excepcion: # Si es diferente de nulo
            self._conexion.rollback()
            log.error(f'Ocurrio una excepcion, se hace rollback: {valor_excepcion} {tipo_excepcion} {traceback_excepcion}')
        else:
            self._conexion.commit()
            log.debug('Commit de la transaccion')
        
        self._cursor.close()
        ConexionPool.liberarConexion(self._conexion)

if __name__ == '__main__':
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM "personasAdmitidas"')
        registros = cursor.fetchall()
        log.debug(f'Elementos de la base de datos: {registros}')
