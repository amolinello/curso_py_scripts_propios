
contador = 0

def mostrarContador():
    print(contador)

def modificarContador(valor):
    global contador
    contador = valor

modificarContador(9)
mostrarContador()

print(contador)

# Funciones como variables

def sumar(a,b):
    return a+b

miFuncion = sumar
print(type(miFuncion))
resultado = miFuncion(3,4)
print(resultado)

# Funcion como argumento

def multipli(a,b, sumarrr):
    return a * b * sumarrr(a,b)

multiplicacion = multipli
print(type(multiplicacion))
print(multiplicacion(1,2,sumar))

# Retornar funciones 

def retornarFuncion():
    return sumar

recibido = retornarFuncion()
print(recibido(3,2))

