# Leer contenido Online
from urllib.request import urlopen


# Leer contenido online
import urllib
from urllib.request import urlopen

palabras = []
# Debido a cambios en la libreria se deben hacer los siguientes cambios:


palabras = []
prueba = 1
if prueba == 0:
    with urlopen('https://es.wikipedia.org/wiki/Endodermo') as mensaje:
        # contenido = mensaje.read()
        # print(contenido) # Muestra toda la información en HTML, en bytes, es una cadena de bytes
        #
        #  Mejor lectura

        contenido = mensaje.read().decode('utf-8') # Tambien muestra el html de la pagina
        print(contenido)

    with open('NuevoArchivo.txt','w',encoding='utf-8') as archivo:
        archivo.write(contenido)

# Leer las palabras de un archivo

elif prueba == 1:
    with urlopen('https://es.wikipedia.org/wiki/Endodermo') as mensaje:
        print(mensaje.read())
        for linea in mensaje:
            palabras_por_linea = linea.decode('utf-8').split()
        print(palabras_por_linea)

else:
    print('Mensaje')
    

# No hacer mucho caso a esto, el URLLIB cambio y se debe modificar este codigo

