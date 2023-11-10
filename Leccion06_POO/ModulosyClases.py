from Persona import *

print('Imprimir un mensaje centrado y con algo en los espacios vacios')
print('Creacion de objetos'.center(50,'+'))

# Crear el objeto vacio
objetoCreado = Persona()
print(objetoCreado)

# Crear el objeto con elementos seleccionados
otroObjetoCreadoUno = Persona('Santiago', 'Molinello', 22)
print(otroObjetoCreadoUno)

print('Eliminacion de objetos'.center(40,'-'))

del otroObjetoCreadoUno

# Es raro, imprime el objeto: objetoCreado también y ese no se elimina...