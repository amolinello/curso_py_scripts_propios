
# Las funciones lambda, son funciones anonimas y son pequeñas
# Anonimas = No tienen un nombre asignado, es solo 1 linea de codigo

def sumar(a,b):
    return a + b

# No necesita agregar parentesis para los parametros y no necesita la palabra return, pero debe regresar una expresion valida

mi_funcion = lambda a, b: a + b

print('1. ', mi_funcion(1, 2))
print(type(mi_funcion))

# Funcion lambda que no recibe argumentos

funcion_lambda = lambda : 'Texto a entregar'

print('2. ', funcion_lambda())


# Funcion lambda con parametros por default
lambdafuncion = lambda a = 5, b = 3: a * b
print('3. ', lambdafuncion())

# uso de *args y **kwargs

listalambda = lambda *args, **kwargs: len(args) + len(kwargs)

lista1 = (1,2,3,4)
diccionario1 = {'a': 2, 'b': 5, 'c': 3}

print('4. ', listalambda(lista1, diccionario1)) # Lo toma como: 1 lista y 1 diccionario, por eso el resultado es 2

print('5. ', listalambda(1,2,3,4, a=2, b=5, c=3))

# Con variables

listalambda = lambda a, b, c= 3, *args, **kwargs: len(args) + len(kwargs) + a + b + c
print('6. ', listalambda(10, 9, 8, 71,2,3,4, e=2, f=5, g=3))

