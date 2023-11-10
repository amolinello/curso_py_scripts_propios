valores = 1, 2, 3
print(valores)
print(type(valores))

# Es asignar una tupla o lista en variables de manera independiente

# Unpacking - Desempaqutado

valor1, valor2, valor3, valor4 = 1, 2, 3, 'Texto'
print(valor1, valor2, valor3, valor4)

# Se usa _ para el valor que no queramos usar 
# 
# valor1, _, valor3, valor4 = 1, 2, 3, 'Texto'

valor1, valor2, *valor3 = 1,2,3,4,5,6,7,8
# Los valores del 3 al 8 se almacenan en valor3 como lista

print(valor1, valor2, valor3)

valor1, valor2, *valor3, valor4, valor5 = 1,2,3,4,5,6,7,8
print(valor1, valor2, valor3, valor4, valor5)
# Valor3 muestra del 3 al 6

valor1, valor2, *valor3, valor4, valor5 = [1,2,3,4,5,6,7,8]
print(valor1, valor2, valor3, valor4, valor5)
# Valor3 muestra del 3 al 6

def regresa_varios_datos():
    return 1, 2, 3

valor1, *valor2 = regresa_varios_datos()
print(valor1, valor2)

vari = '14:33'.partition(':')
print(vari)
print(type(vari))

hora, _, minutos = vari
print(hora)
print(minutos)

# * sirve para desempaquetar

numeros = [1,2,3,4,5,6]
print('Numeros: ',numeros)
print('Desempacado:', *numeros)

diccionarios = {'letra':'a', 'numero': 3, 4:'numero'}
print(diccionarios)
print(*diccionarios) # imprime las llaves

def imprimir(a, b, c, d, e, f):
    print(a+b+c+d+e+f)

imprimir(*numeros)

a, *b, c = numeros
print(f'a: {a}, b: {b}, c: {c}')

ejemplo = [11, 56, 23, 98, 66]
lista_unida = [*numeros, *ejemplo]
print(lista_unida)

ejemplodic = {'aa': 'A', 'bc': 'B', 'de': 'C'}
dic3 = {**diccionarios, **ejemplodic}
print(dic3)

stringo = 'mucho texto'
listaString = [*stringo]
print(listaString)
