# No mantiene un Orden, y no almacena elementos duplicados
# Se define con llaves

valorSet = {1, 2, 11, 3, 4, 5, 6, 7, 8, 9,'Texto', True, 2.66, False, 10, 0}

print(valorSet)
valorSeteado = set('Un texto largo')
print(valorSeteado)
print(type(valorSet))

print(f'''
    Saber si un elemento esta en el set:
    {'Texto' in valorSet}
''')

# Agregar elementos
valorSet.add('Otro texto')
print(valorSet)

# Remover un elemento
# valorSet.remove('monto') # Envia el error Key Errorm - No encuentra la llave
valorSet.remove(2)
print(f'''
    Al eliminar el valor 2, queda:
    {valorSet}
''')

# Eliminar los elementos del set
valorSet.clear()
print('Despues de eliminar el set: ')
print(valorSet)

# Eliminar el set
del valorSet
# print(valorSet)

# El set toma el True como 1 y el False como 0

pruebaSet = {1, True, False, 0, 0.22, 1.33}
print(pruebaSet)