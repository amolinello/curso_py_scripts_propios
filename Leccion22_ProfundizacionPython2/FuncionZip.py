# Permite unir uno o mas iterables

#print(dir(__builtins__)) # Muestra las clases y metodos automaticos disponibles en python
#help(zip)

numero = [1, 2, 3, 5] # puedeen ser tuplas tambien
letras = ['a', 'b', 'c']
identificadores = 200, 201, 202, 230

mezcla = zip(numero, letras, identificadores)
print(mezcla) # imprime segun la cantidad minima de los elementos, en este caso son 3
print(list(mezcla)) # une de la manera: [(1, 'a', 200), (2, 'b', 201), (3, 'c', 202)]
print(list(mezcla)) # los elementos del Zip se consumen, es decir, una vez se usan ya se borra la información, en este caso da: []
print(type(mezcla)) # Zip

conjuntoSet = {1, 5, 8, 9, 10, 13, 5}
mezcla2 = zip(numero, letras, identificadores, conjuntoSet)
#print(list(mezcla2))

for a, b, c, d in mezcla2:
    print(f'a: {a}, b: {b}, c: {c} y d: {d}')

vacia = []
for a, b, c, d in zip(numero, letras, identificadores, conjuntoSet):
    
    vacia.append(f'a: {a}, b: {b}, c: {c} y d: {d}')

print('Esta es la Variable (vacia): ',vacia)

# Unzip

mezclados = [(1,'a'),(2,'b'),(3,'c'),(4,'d'),(5,'e')]

numeros, letras = zip(*mezclados)

print(f'Los numeros: {numeros} Las letras: {letras}')

# se pueden ordenar los zip con la función sorted(variable del zip), si se hace sorted(zip(letras,numeros)) solo ordena por las letras
# si se hace al revés ordena por los numeros

variable = dict([('a',12),(11,'b')])
print(variable)

unido = zip([1,2,3,4],['a','b','c'])
variable = dict(unido)
print(variable)
