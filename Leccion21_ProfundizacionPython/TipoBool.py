# Profundizando en tipo Bool

# Tipos Númericos, False para 0 y True para el resto

print(f'Resultado: {bool(0)}')
print(f'Resultado: {bool(57)}')
print(f'Resultado: {bool(0.0)}')
print(f'Resultado: {bool(86.02)}')

# Tipor STR, False para cadena vacia y True pasa el resto

print(f'Resultado: {bool("")}')
print(f'Resultado: {bool("A")}')
valor = ''
print(f'Resultado: {bool(valor)}')
valor = 'Texto'
print(f'Resultado: {bool(valor)}')

# Tipo colecciones, False para colecciones, True para todas las demas colecciones
lista = []
print(f'+ Resultado: {bool(lista)}')
lista = ['a']
print(f'+ Resultado: {bool(lista)}')

tupla = ()
print(f'- Resultado: {bool(tupla)}')
tupla = ('a','b', 'c')
print(f'- Resultado: {bool(tupla)}')

diccionario = {}

diccionario = ()
print(f'* Resultado: {bool(diccionario)}')
diccionario = {123:'Numeros', 'Letras':456}
print(f'* Resultado: {bool(diccionario)}')


if '':
    print('Verdadero')
else:
    print('Falso')

if 3:
    print('Verdadero')
else:
    print('Falso')

while 'texto':
    print('Entro al While')
    break
