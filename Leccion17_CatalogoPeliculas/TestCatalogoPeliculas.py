from Dominio.Pelicula import Pelicula
from Servicio.CatalogoPeliculas import CatalogoPeliculas


opcion = None

while opcion != 4:
    print('Opciones: ')
    print('''
    1. Agregar Peliculas
    2. Listar Peliculas
    3. Eliminar Peliculas
    4. Salir
    ''')
    try:
        opcion = int(input('Escribe la opción (1-4): '))
    except BaseException as ex:
        print('Eso no es valido!')
        print(ex)
        opcion = None
    
    if opcion == 1:
        nombre_pelicula = input('Ingrese el nombre de la pelicula: ')
        pelicula = Pelicula(nombre_pelicula)
        CatalogoPeliculas.agregar_pelicula(pelicula)
    
    elif opcion == 2:
        CatalogoPeliculas.lista_peliculas()
    
    elif opcion == 3:
        CatalogoPeliculas.eliminar_peliculas()
    

else:
    print('\nSaliendo del programa')