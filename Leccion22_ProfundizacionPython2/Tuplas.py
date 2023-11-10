
a, b = 'hola', 'adios'

print(f'a: {a}, b: {b}')

a, b = b, a

print(f'a: {a}, b: {b}')

def regresarMasValores():
    return 12, 15

c, d = regresarMasValores()
print(f'c: {c}, d: {d}')

# regresar la suma de una tupla

resultado = sum((1,2,3,5,6))
print(resultado)

def sumar(*tupla):
    return sum(tupla)

tup = sumar(2,5,68,7)
print(tup)