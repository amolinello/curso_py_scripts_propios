
class ManejoArchivos:

    def __init__(self, nombreArchivo):
        self._nombreArchivo = nombreArchivo

    def __enter__(self):
        print(f'Obetenermos el recurso {self._nombreArchivo}'.center(50, ' '))
        self._nombreArchivo = open(self._nombreArchivo, 'r', encoding='utf8')
        return self._nombreArchivo

    def __exit__(self, tipoExcepcion, valorExcepcion, trazaDelError):
        print('Cerrando el archivo'.center(50, ' '))
        if self._nombreArchivo:
            self._nombreArchivo.close()