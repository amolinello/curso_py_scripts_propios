lista = [1, 2, 3, 4, True, False, 'Texto', 2.22]
for i in lista:
    print(i)
    print(type(i))

print(f'Imprimir por indice {lista[0]} y al reves {lista[-1]}')

# Toma las posiciones desde el 0 hasta...
print(lista[:3])  # imprime el 1, 2, 3
print(lista[1:4]) # imprime el 2, 3, 4
print(lista[3:]) # imprime 4, True, False, 'Texto', 2.22
print(lista[5:11]) # Tiene hasta el dato 7 (0 a 7) y  deja imprimir con un valor de mas
# imprime False, 'Texto', 2.22

# Longitud del arrego - Cantidad de elementos = 8
print(len(lista))

# Agregar elemento
lista.append('Nuevo')
print(lista)

# Insertar elemento en un indice especifico
lista.insert(1, 1.5) # insertar en (la posicion, el valor)
print(lista)

# Remover un elemento
lista.remove('Texto')
print(lista)

# Remover el ultimo elemento y lo retorna
valor = lista.pop()
print(lista)
print(valor)

# Eliminar elemento por indice
del lista[3]
print(lista)

# Limpiar todos los elementos de la lista
lista.clear()
print(lista)

# Borrar la lista por completo
#del lista
#print(lista) #Envia error ya que no existe la variable lista

otros = [1,2,3,4,5]

minVal = min(otros)
maxVal = max(otros)
mayor = list(otros)
menor = list(otros)
mayor.remove(minVal)
menor.remove(maxVal)
maxVal = 0
minVal = 0
for i in mayor:
    maxVal += i
for j in menor:
    minVal += j

print(minVal, maxVal)
