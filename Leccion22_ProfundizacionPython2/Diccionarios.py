
# Profundizando en diccionarios

# a partir de la versión 3.7 los diccionarios guardan un orden

diccionario = {12:'a', 13:'b','letras': 11, 'Numeros': 1, 1:'primero', 3:1}

# Los diccionarios son mutables pero las llaves son inmutables
print(diccionario)

# No puede tener llaves duplicadas, en caso de ingresar una llave no existente, la agrega

diccionario['llave'] = 1234
print(diccionario)

# Las llaves también son sensibles a mayúsculas
diccionario['Llave'] = 12344567
print(diccionario)

# Con el metodo get no envia excepción y puede enviar algo mas cuando no la encuentra
print(diccionario.get("cosas", 'No se encontro la llave'))

# Agrega valor por default cuando no encuentra el nombre
print(diccionario.setdefault('nombres','Valor no encontrado'))
print(diccionario)

# si se quiere imprimir un valor del diccionario y no encuentra la llave, envia una excepcion
#print(diccionario['cosas'])

# Se puede importar pprint para poder usar la funcion de imprimir mejor las llaves
