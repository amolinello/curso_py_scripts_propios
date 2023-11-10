import os

class CatalogoPeliculas:
    
    ruta_archivo = 'Peliculas.txt'

    def __init__(self, ruta_archivo):
        self._ruta_archivo = ruta_archivo
    
    @classmethod
    def agregar_pelicula(cls, pelicula):
        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    @classmethod
    def lista_peliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf8') as archivo:
            print('Catalogo Peliculas'.center(50, '-'))
            print(archivo.read())
    @classmethod
    def eliminar_peliculas(cls):
        try:
            os.remove(cls.ruta_archivo)
            print(f'Archivo Eliminado {cls.ruta_archivo}')
        except Exception as ex:
            print('No hay lista de peliculas por eliminar')

