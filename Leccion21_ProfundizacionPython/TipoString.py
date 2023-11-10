
# # Concatenación automatica en python

# palabra = 'Hola' + 'Persona'
# print(palabra)
 
# # No sirve con variables

# palabra = 'Holas' ' Personas'
# print(palabra)

# palabra += 'Del' ' Mundo'
# print(palabra)

# # Ayudas

# # help(str)

# help(str.capitalize)

# Uso del docstring en python

# La documentación que ingresemos debe ser la minima necesaria
class MiClase:
    '''
    Este es un ejemplo
    de
    documentación
    de
    la clase
    '''
    def __init__(self):
        '''
        Metodo de inicio de
        la clase
        '''
        
    def miMetodo(self, param1, param2):
        '''
        Esta es la documentación del metodo

        param1: parametro 1
        param2: parametro 2
        
        Regresa la uma de los 2 datos ingresados
        '''
        return param1 + param2
    
if __name__ == '__main__':
    # help(MiClase)
    # help(MiClase.miMetodo)
    # print(MiClase.__doc__) # Imprime solo la documentación de la clase
    # print(MiClase.__init__.__doc__) # Imprime solo la documentación del metodo __init__

    # Una cadena es inmutable

    # help(str.capitalize)

    texto = 'Mensaje Con Un motOn de MayusculAS'
    texto2 = texto.capitalize()
    print(f'Texto 1: {texto}, id: {id(texto)}')
    print(f'Texto 2: {texto2}, id: {id(texto2)}')
    texto += ' Agregado' # Como es inmutable, crea un nuevo objeto en memoria
    print(f'Texto 1: {texto}, id: {id(texto)}')

    # Metodo join

    help(str.join)
    cadena = ['a','b','c']
    mensaje = str.join(', ', cadena)
    print(f'Cadena: {cadena}')
    print(f'Mensaje: {mensaje}')

    tupla = ('Mensaje', 'En', 'Tupla')
    mensaje = str.join(' ', tupla)
    print(f'Tupla: {tupla}')
    print(f'Mensaje: {mensaje.capitalize()}')

    enSet = set(['letras', 'Numeros', 'variables', '123'])
    #print(enSet)
    #enSet = {'cosas', 'variables', 'idioma'}
    #print(enSet)
    mensaje = str.join(' | ', enSet)
    print(f'Set: {enSet}')
    print(f'Mensaje: {mensaje}')

    diccionario = {'Nombre':'Catalina', 'Apellido':'Duque', 'Edad':'30'}
    llaves = '-'.join(diccionario.keys())
    valores = '*'.join(diccionario.values())
    print(f'Set: {diccionario}')
    print(f'Llaves: {llaves}, tipo: {type(llaves)}')
    print(f'Valores: {valores}, tipo: {type(valores)}')

    # Metodo split
    print('\n'+'*'*70+'\n')
    cadenaTexto = 'Un mensaje con muchos caracteres y numeros 12345'
    listaCreada = cadenaTexto.split() # Seapara con respecto a los espacios " "
    print(f'Mensaje: {cadenaTexto}')
    print(f'Lista: {listaCreada}, Elementos: {len(listaCreada)}')

    # Metodo split separado limitado
    print('\n'+'*'*70+'\n')
    cadenaTexto = 'Un mensaje con muchos caracteres y numeros 12345'
    listaCreada = cadenaTexto.split(' ', 1) # Seapara con respecto a los espacios " "
    print(f'Mensaje: {cadenaTexto}')
    print(f'Lista: {listaCreada}, Elementos: {len(listaCreada)}')

    print('\n'+'*'*70+'\n')
    cadenaTexto = 'Un mensaje con muchos caracteres y numeros 12345'
    listaCreada = cadenaTexto.split('a') # Seapara con respecto a la letra "a"
    print(f'Mensaje: {cadenaTexto}')
    print(f'Lista: {listaCreada}, Elementos: {len(listaCreada)}')


    # Dar Formato a las cadenas STR

    nombre = 'Juan'
    edad = 59

    mensaje_con_formato = 'Mi nombre es %s y tengo %d años'%(nombre, edad)
    print(mensaje_con_formato)

    persona = ('Camila', 'Restrepo', 23, 320.5)
    mensaje_con_formato = 'Hola %s %s tienes %d años y %.2f de dinero'%persona
    print(mensaje_con_formato)

    mensaje_con_formato = 'Hola %s %s tienes %d años y %.2f de dinero'
    persona2 = ('Luisa', 'Gomez', 25, 2340.8)
    print(mensaje_con_formato%persona2)

    # Metodo Format

    nombre = 'Pedro'
    edad = 35
    sueldo = 3500000.2249
    mensaje_con_formato = 'Nombre {}, Edad {}, Sueldo {:.2f}'.format(nombre, edad, sueldo)
    print(mensaje_con_formato)

    mensaje_con_formato = 'Nombre {0}, Edad {1}, Sueldo {2:.2f}'.format(nombre, edad, sueldo)
    print(mensaje_con_formato)

    mensaje_con_formato = 'Edad {1}, Sueldo {2:.2f}, Nombre {0}'.format(nombre, edad, sueldo)
    print(mensaje_con_formato)

    mensaje_con_formato = 'Nombre {n}, Edad {e}, Sueldo {s:.2f}'.format(n=nombre, e = edad, s = sueldo)
    print(mensaje_con_formato)

    diccionario = {'nombre':'Ana','apellido':'Alvarez','edad':31,'sueldo':5630.1986}

    mensaje_con_formato = 'Nombre {persona[nombre]}, Apellido {persona[apellido]}, Edad {persona[edad]}, Sueldo {persona[sueldo]:.2f}'.format(persona=diccionario)
    print(mensaje_con_formato)


    # Mas recomendada
    mensaje_con_formato = f'Nombre {nombre}, Edad {edad}, Sueldo {sueldo:.2f}'
    print(mensaje_con_formato)
    print(nombre, edad, sueldo, sep=', ') # Separarlos por coma y espacio


