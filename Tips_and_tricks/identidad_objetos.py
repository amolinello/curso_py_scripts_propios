
# El operador == Compara el contenido de 2 objetos, 
# sin tener que ser el mismo

# Operador "is" revisa si los 2 objetos son identicos
# Ambos apuntan a la misma dirección de memoria



import copy
from re import split


lista_a = [1, 2, 3,]
lista_b = lista_a

print(f'1. a == b?: {lista_a==lista_b}')
print(f'1. a is b?: {lista_a is lista_b}',end='\n\n')

lista_c = list(lista_a)
print(f'2. a == c?: {lista_a==lista_c}')
print(f'2. a is c?: {lista_a is lista_c}',end='\n\n')

lista_c.append(4)
print(f'3. a == c?: {lista_a==lista_c}')
print(f'3. a is c?: {lista_a is lista_c}',end='\n\n')

# Representación de objetos:
# __str__ su objetivo es información legible para el usuario
# __repr__ su objetivo es que la información no sea ambigua
# se utiliza para hacer debugging

# Es mas recomendable usar __repr__ que __str__

# En repr, se imprime con el formato que tiene la función u objeto
# ejm: '{self.__class__.__name__}({valorNombre}, {valorApellido}, {ValorCedula})'


# Errores personalizados

def validar(nombre):
    if len(nombre) < 3:
        raise ValueError
    else:
        print('Validación correcta')

nombre = 'Maria'
validar(nombre)

class NombreDemasiadoCorto(ValueError):
    pass

def validar_mejorado(nombre_completo):
    if len(nombre_completo) < 3:
        raise NombreDemasiadoCorto(nombre_completo)
    else:
        print('Validación correcta')

nombre = 'Maria'
validar_mejorado(nombre)

# Copia superficial, en la lista externa es distinto y en la interna es igual

lista_a = [[1, 2, 3,],[4,5,6]]
lista_b = list(lista_a)

print(f'1. a == b?: {lista_a==lista_b}, {lista_a}')
print(f'1. a is b?: {lista_a is lista_b}, {lista_b}',end='\n\n')
# Modificando internos
lista_a[0][0] = 1100

# Agregando
lista_a.append([7,8])
print(f'2. a == b?: {lista_a==lista_b}, {lista_a}')
print(f'2. a is b?: {lista_a is lista_b}, {lista_b}',end='\n\n')

# Resultado
# 2. a == b?: False, [[1100, 2, 3], [4, 5, 6], [7, 8]]      
# 2. a is b?: False, [[1100, 2, 3], [4, 5, 6]]

# Copia superficial, en la lista externa es distinto y en la interna es igual

# Copias profundas
lista_a = [[1, 2, 3,],[4,5,6]]
lista_b = copy.deepcopy(lista_a)

print(f'1. a == b?: {lista_a==lista_b}, {lista_a}')
print(f'1. a is b?: {lista_a is lista_b}, {lista_b}',end='\n\n')
# Modificando internos
lista_a[0][0] = 1100

# Agregando
lista_a.append([7,8])
print(f'2. a == b?: {lista_a==lista_b}, {lista_a}')
print(f'2. a is b?: {lista_a is lista_b}, {lista_b}',end='\n\n')

# Resultado
# 2. a == b?: False, [[1100, 2, 3], [4, 5, 6], [7, 8]]      
# 2. a is b?: False, [[1, 2, 3], [4, 5, 6]]

print(split(' ','un texto largo'))
