
# Diccionarios - dicts - maps - hashmaps - lookup tables, etc
# (llave, valor)


# Ejecmplo directorio (llave, valor)


directorio = {
    'Carlos':123456,
    'Alicia':789123,
    'Ana':456789,
    }

print(directorio) # {'Carlos': 123456, 'Alicia': 789123, 'Ana': 456789}
print(directorio['Alicia']) # 789123
# print(directorio['inventado']) # KeyError: 'inventado'

# Se puede utilizar una expresión para crear el diccionario

valores_al_cuadrado = {x: x*x for x in range(5)}
# Llave el valor y valor al cuadrado el valor del diccionario
print(valores_al_cuadrado)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Se debe usar tuplas para modificar diccionarios (inmutable)
tupla = (1,2,3)
diccionario = {tupla:'A'}
print(diccionario)
# {(1, 2, 3): 'A'}
diccionario['a'] = 11


# Orden de inserción se hace con OrderedDict, se debe importar de collections

print(diccionario.get('cosa')) # None
print(diccionario.get('a')) # 11

# Se pueden crear diccionarios de solo lectura con:
# MappingProxyType -> se debe importar de types
