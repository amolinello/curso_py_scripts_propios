# Las listas son mutables = se pueden modificar

from copy import copy


nombres = ['Juan', 'David', 'Camila']
nombres2 = 'Ana Sebastian Jorge Fabian'.split()

print(f'Suma de listas: {nombres + nombres2}')

agregar = 'Flor Mariana Lina'.split()
nombres.extend(agregar)
print(f'Lista extendida: {nombres} con lista 2: {agregar}')

# Obtener el indice de un elemento (empieza contando desde la posición 0)

numeros = [1, 4, 5, 7, 33, 44, 57, 8, 9, 10, 44]

posicion = numeros.index(44)

print(f'Lista: {numeros}')
print(f'Posicion del numero 44: {posicion}')

posicion_palabra = nombres.index('Flor')

print(f'Posicion de Flor en los nombres: {posicion_palabra}')

# invertir el orden
numeros.reverse()
print(f'Lista invertida: {numeros}')

# Ordenar los elementos
# Ascendente
numeros.sort()
print(f'Lista ordenada ascendente: {numeros}')

# Descendente
numeros.sort(reverse=True)
print(f'Lista ordenada descendente: {numeros}')


# Valores máximos y mínimos
original = [1, 2, 3, 4, 5, 11, 59, 14]
print(f'Valor minimo: {min(original)}')
print(f'Valor maximo: {max(original)}')

# Copiar listas

copia = copy(original)
print(f'Original: {original} Memoria: {id(original)}')
print(f'Copia: {copia} Memoria: {id(copia)}')
print(f'Misma referencia?: {original is copia}')

original.append(100)
print(f'Original: {original} Memoria: {id(original)}')
print(f'Copia: {copia} Memoria: {id(copia)}') # Al modificar, como no son iguales, no cambia la copia

# Otra forma de copiar
copia2 = list(original)

print(f'Original: {original} Memoria: {id(original)}')
print(f'Copia: {copia} Memoria: {id(copia)}')
print(f'Copia2: {copia2} Memoria: {id(copia2)}')
print(f'Misma referencia?: {original is copia2}')

# Otra forma de copiar
copia3 = original[:]
print(f'Original: {original} Memoria: {id(original)}')
print(f'Copia: {copia} Memoria: {id(copia)}')
print(f'Copia2: {copia2} Memoria: {id(copia2)}')
print(f'Copia3: {copia3} Memoria: {id(copia3)}')
print(f'Misma referencia?: {original is copia3}')
print(f'Mismo contenido?: {original == copia3}')

# Lista de listas

listaMultiplicacion = 5*[[2, 5]]
print(f'Lista original: {listaMultiplicacion}')
print(f'Misma referencia?: {listaMultiplicacion[0] is listaMultiplicacion[1]}')
print(f'Mismo contenido?: {listaMultiplicacion[0] == listaMultiplicacion[1]}')

# Modificando individualmente el objeto
listaMultiplicacion[0] = [1, 3]
print(f'Lista modificada: {listaMultiplicacion}')

# Usando append
# Modifica todos los objetos iguales
listaMultiplicacion[2].append(12)
print(f'Lista modificada 2: {listaMultiplicacion}')

# Matrices

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1], 'Mensaje', 99]
print(f'Matriz original: {matriz}')
print(f'Renglón 1, Columna 1: {matriz[1][1]}')
matriz[0] = 87
matriz[5] = [10, 13, 77]
matriz[1][1] = 3000
# matriz[6] = 'texto' # No deja modificar un elemento que no existe para la matriz
print(f'Matriz cambiada: {matriz}')


# Ordenamiento de funciones de tipo Built-in
listaDeListas = [[65,88,99,73],[87,99,101],[100,300,655,9,7,3,1],[1]]
listaDeListas.sort(key=len) # Ordenar por cantidad de elementos
print(f'Lista de listas Ordenada: {listaDeListas}')

# Sorted built-in
listaDeCaracteres = ['Carla','Jorge','Ana','Alejandro','Luis','Luis1', 'Luis2','Luisa','Rodrigo']
listaDeCaracteres = sorted(listaDeCaracteres)
print(f'Lista de caracteres ordenado: {listaDeCaracteres}')

# Ordenado descendente
listaDeCaracteres = sorted(listaDeCaracteres, reverse=True)
print(f'Lista de caracteres ordenado descendente: {listaDeCaracteres}')

# Ordenado por cantidad de caracteres
listaDeCaracteres = sorted(listaDeCaracteres, key=len)
print(f'Lista de caracteres ordenado por cantidad de caracteres: {listaDeCaracteres}')

# Ordenado por cantidad de caracteres al reves
listaDeCaracteres = sorted(listaDeCaracteres, key=len, reverse=True)
print(f'Lista de caracteres ordenado por cantidad de caracteres al revés: {listaDeCaracteres}')

# Lista reversada desde un inicio
letras = ['a','b', 'c','d', 'e', 'f', 'Y muchos mas']
listaReversada = reversed(letras)
print(listaReversada)
# Opcion 1: La mas facil y mejor
print(list(listaReversada))


# Opcion 2: La complicada
# reversada = []
# for item in listaReversada:
#     reversada.append(item)

# print(reversada)
lista = [1,2,3,3,4,3,3,4,5]
caracteres = 'asbccdadadadsaa'

s = '12:00:00AM'
tiempo = tiempo = s.split(':')

if tiempo[2][2:] == 'PM':
    if int(tiempo[0]) < 12:
        hora = int(tiempo[0])+12
        tiempo[0] = str(hora)
    tiempo = str.join(':',tiempo)
    tiempo = tiempo.replace('PM','')
else:
    if int(tiempo[0]) >= 12:
        hora = int(tiempo[0])-12
        if hora == 0:
            tiempo[0] = '00'
        else:    
            tiempo[0] = str(hora)
    tiempo = str.join(':',tiempo)
    tiempo = tiempo.replace('AM','')

print(tiempo)
