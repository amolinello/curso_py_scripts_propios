from LoggerBase import log
from Conexion import Conexion


class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug('Inicio del método with __enter__')
        self._conexion = Conexion.obtenerConexion()
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
        Conexion.liberarConexion(self._conexion)