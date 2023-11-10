
lista = [11,20,30,45,54,60,]

# Enumerate

for contar, valor in enumerate(lista):
    print(contar, valor)

print(f'''
{'*'*50}
''')

# Se puede especificar por que valor empezar

for contar, valor in enumerate(lista, start=100):
    print(contar, valor)

# Funcion números pares

def pares(iterable):
    return [i for i, valor in enumerate(iterable, start=1) if not valor%2]

print(pares(lista))
# Devuelve el indice de los valores pares de la lista
