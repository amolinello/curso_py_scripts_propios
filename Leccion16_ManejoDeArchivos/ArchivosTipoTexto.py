'''
try:
    archivo = open('Prueba.txt','w', encoding='utf8')
    
    # Write
    archivo.write('Información Agregada')
    archivo.write('Adios')
    archivo.write('\nAdios')
    # Lo pone todo junto

except Exception as ex:
    print(f'Sucedio un error: {ex}')
finally:
    archivo.close()
    # Una vez cerrado ya no se puede hacer nada más
    print('Fin del archivo')
'''


# Leer el archivo

try:
    archivoNuevo = open('C:\\Users\\PC\\Desktop\\Programacion Alejo\\Python\\Programacion basica\\Prueba.txt','r', encoding='utf8')
    # print(archivoNuevo.read(5)) # Lee los primeros 5 caracteres
    # print(archivoNuevo.read()) Lee todas las lineas
    # print(archivoNuevo.readlines()) # Lee linea por linea y las guarda en una lista
    # print(archivoNuevo.readlines()[1]) # Lee linea por linea y las guarda en una lista
    
except Exception as ex:
    print(f'En el nuevo codigo, Sucedio un error: {ex}')
finally:
    # archivoNuevo.close()
    # Una vez cerrado ya no se puede hacer nada más
    print('Fin del archivo')

try:
    archivoNuevo2 = open('C:\\Users\\PC\\Desktop\\Programacion Alejo\\Python\\Programacion basica\\CopiaTextoPrueba.txt','a', encoding='utf8')
    
    archivoNuevo2.write(archivoNuevo.read())

    print(archivoNuevo2.readable()) # Pregunta si el archivo se puede leer
    
except Exception as ex:
    print(f'En el nuevo codigo, Sucedio un error: {ex}')
finally:
    archivoNuevo.close()
    archivoNuevo2.close()
    # Una vez cerrado ya no se puede hacer nada más
    print('Fin del archivo')

# Cada vez que se ejecuta el código se escribe en el archivo