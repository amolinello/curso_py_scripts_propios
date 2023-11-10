numeros = range(10)

lista_pares = []

# Creamos una lista con los valores pares multiplicados por si mismo

for numero in numeros:
    # Revisamos si es par
    if numero % 2 == 0:
        lista_pares.append(numero * numero)

print(lista_pares)

# con list comprehension
# [Expresion for variable in coleccion if condicion]

lista_pares = []
lista_pares = [numero*numero for numero in numeros if numero%2 == 0]
print(lista_pares)

# ejemplo con dos condiciones, que sea par y divisible por 6
numeros = range(51)
lista_pares = []
lista_pares = [numero for numero in numeros if numero%2 == 0 and numero%6 == 0]
print(lista_pares)

# ejemplo con if else

lista_pares = []
lista_impares = []

[lista_pares.append(numero) if numero%2 == 0 else lista_impares.append(numero) for numero in numeros]
print(f'Pares: {lista_pares}')
print(f'Impares: {lista_impares}')


# convertir lista de listas en una sola lista

lista_listas = [[1,2,3],[4,5,6],[7,8,9],[10]]
pares = []

pares = [valor for lista in lista_listas for valor in lista if valor%2 == 0]
print(pares)