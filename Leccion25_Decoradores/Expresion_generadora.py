
# Crear generador anonimo

cosa = 2

multiplicacion = (valor*cosa for valor in range(4))
print(type(multiplicacion))

for dato in multiplicacion:
    
    print(dato)

# Se puede usar una lista u otros iteradores

listas = ['Juan', 'Carlos']
generador = (valor for valor in listas)

print(next(generador))
print(next(generador))

# Los generadores son muy buenos cuando no sabemos cuantos datos hay que recuperar, sean miles o millones


# Crear string a través de generador
lista = ['Carla', 'Laura', 'Sofia', 'Ana']
contador = 0

def incrementar():
    global contador
    contador += 1
    return contador

# Primero el Yield del generador y luego el for

generador = (f'{incrementar()}. {nombre }' for nombre in lista)

lista = list(generador)
print(lista)

cadena = ', '.join(lista)
print(cadena)

