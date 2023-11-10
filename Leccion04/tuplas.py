# Las tuplas son valores que no se pueden cambiar

x = (1, 2, 3, 4, 5, True, False, 'letras', 11.5)
print(x)
print(x[3])
# x[5] = 'pase' # Mensaje de error porque no se puede cambiar el valor
# print(x)

# Las tuplas no son mutables = no modificable

print(len(x))
print(x[1:6]) # imprime (2, 3, 4, 5, True)
print(x[0:1]) # imprime (1, =)
print(x[::2]) # imprime todo cada 2 posiciones empezando por la 0.                                  (1, 3, 5, False, 11.5)
print(x[2::]) # imprime todo desde la posición 2                                                    (3, 4, 5, True, False, 'letras', 11.5)
print(x[1::2]) # Imprime todo cada 2 posiciones, empezando por la 1.                                (2, 4, True, 'letras')
print(x[::-1]) # Imprime toda la tupla al revés.                                                    (11.5, 'letras', False, True, 5, 4, 3, 2, 1)
print(x[::-2]) # Imprime todo al revés cada 2 posiciones hacia atras.                               (11.5, False, 5, 3, 1)
print(x[-2::-3]) # Imprime todo al revés cada 3 posiciones empezando por posicion -2.               ('letras', 5, 2)
print(x[2::-2]) # Imprime todo al revés cada 2 posiciones hacia atras empezando por la posicion 2.  (3, 1)

for elemento in x:
    # CTRL + ESPACIO para ver mas opciones, en este caso del print
    print(elemento,end=' ') # Separa los elementos por 1 espacio
print('')
#***********************************************************************************************************************************************#

# Cambiar elementos de una tupla
x = list(x)
x.append('Nuevo valor')
print(x)
print(type(x))
x = tuple(x)
print(x)
print(type(x))

#***********************************************************************************************************************************************#

# Eliminar la tupla
del x
print(x)
