# Diccionarios: diccionario = {'llave1':'Valor,'llave2':12,45:'texto'}

# La llave debe ser algo inmutable
diccionario = {
    'IDE': 'Integrated Development Enviroment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}

print(diccionario)
print(f'Largo del diccionario: {len(diccionario)}')
print(diccionario['DBMS'])

# Modificar elemntos del diccionario
diccionario['DBMS'] = 'datab mana sys'
print(diccionario)

# Obtener elementos del diccionario

variable = diccionario.get('OOP')
variable += ' Texto Agregado'
print(variable)

# Acceder a llave del diccionario
for termino in diccionario:
    print(termino)
    print(type(termino))

# Acceder por separado a la llave y al valor

#Este metodo genera el error de que son muchos valores que desempacar
#for llave, valor in diccionario:
#    print(f'La llave: {llave} y el valor de {valor}')

# Este es el metodo correcto
for llave, valor in diccionario.items():
    print(f'La llave: {llave} y el valor de: {valor}')

# Para recuperar solo llaves del diccionario
for llave in diccionario.keys():
    print(llave)

# Para recuperar solo valores del diccionario
for valores in diccionario.values():
    print(valores)

# Comprobar existencia de algo en el diccionario
print('IDE' in diccionario)

# Agregar elementos
diccionario['PK'] = 'Primary Key'
print(diccionario)

# Eliminar elemento
cosa = diccionario.pop('DBMS') # Elimina el elemento del diccionario y devuelve el valor
print(cosa)
print(diccionario)

# Vaciar el diccionario
diccionario.clear()
print(diccionario)

# Eliminar el diccionario
del diccionario
#print(diccionario)

