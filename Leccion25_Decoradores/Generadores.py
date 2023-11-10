# Generadores

# Es una función especial en python que regresa una secuencia de valores
# Por medio de Yield devuelve los valores poco a poco de una secuencia (Yield = Producir)
# No se usa Return


def generador():
    yield 1
    yield 2
    yield 3
    yield 'Texto'

# Consumir el generador a demanda

gen = generador()

# Con cada llamada consumimos un valor

print(gen) # Imprime el tipo y la dirección en memoria
print(next(gen)) # Imprime 1
print(next(gen)) # Imprime 2
print(next(gen)) # Imprime 3
print(next(gen)) # Imprime 'Texto'
# print(next(gen)) # como no tiene mas para imprimir, arroja el mensaje StopIteration

# con el ciclo for
print()
print(' En el For '.center(50,'x'))
for valor in generador():
    print(valor)



