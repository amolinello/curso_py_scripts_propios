
# Set coleccion de elementos unicos mutable
# Los elementos del set no pueden se mutables, es decir, una variable, una lista, etc.

conjunto = {(1,2,3), 3.75, True}
print(conjunto)

# set vacio
conjunto = set()
print(conjunto)

conjunto.add(1)
conjunto.add('letras')
print(conjunto)

cosas = (1, True, 96, 'letras', 1, False, 0)

conjunto = set(cosas)
print(conjunto)

conjunto2 = {100, 200, 300, 1, 0, 'le'}
conjunto.update(conjunto2)

print(conjunto)

# copiar referencias
copia = set(conjunto)
print(copia)
print(f'son iguales? {conjunto == copia}')
print(f'Misma referencia?: {conjunto is copia}')

# Se puede ver la union, intersección, diferencia y diferencia simetrica de los set, conjunto, subconjuento y conjuntos separados
