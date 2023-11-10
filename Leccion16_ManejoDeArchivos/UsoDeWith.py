# Automaticamente abre y cierra el archivo

#with open('Prueba.txt','r',encoding='utf8') as archivo:
#    print(archivo.read())

    # Manda a llamar los metodos __enter__() y __exit__()

from ManejoArchivos import ManejoArchivos

with ManejoArchivos('Prueba.txt') as archivo:
    print(archivo.read())