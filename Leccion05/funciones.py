
# Nombre de funcion => mi_funcion o miFuncion, igual que con las variables

# Solo se pueden llamar despues de crearlas


def miFuncionEnPython ():
    print('Mi funcion en python')

def otra_funcion_en_python(): #Se puede usar cualquier de las 2 pero definir con cual quedarse
    print('Mi otra funcion en python')

# Ejecuta este print cuando se ejecuta en este archivo o se importa el archivo y lo ejecutan alla
""" ejemplo:

    import funciones

    funciones
    
    # Acá mandará a llamar lo que no este en el if __name__ == '__main__'

"""
print('Fuera de la funcion')

def funcion_con_argumentos(texto, numero):
    return f'el texto ingresado {texto} y el numero ingresado {numero}'

def sumar(a, b):
    return a + b

# def restar_con_default(a: int = 0, b: int= 0) -> float: # -> float es un indicador para la ayuda, no hace nada
def restar_con_default(a= 0, b= 0):
    return a-b

def listar_nombres_y_diccionario(*nombres, **diccionario): # El asterisco es para los valores que vienen en una lista y lo obtiene como tupla
    # lo recorre si esta fuera del parentesis o los corchetes
    
    for i in nombres[0]:
        print(f'Nombre: {i}')
    for llave, valor in nombres[1].items():
        print(f'la llave: {llave} y el valor: {valor}')

# Funcion recursiva
def restar_hasta_cero(numero):
    resultado = numero

    if numero == 0:
        return 0
    return resultado - restar_hasta_cero(numero-1)

# Entrada de diccionario a la funcion
def diccionarios(**args):


    for llave, valor in args.items():
        print(f'llave: {llave}, valor: {valor}')


if __name__ == '__main__':

    miFuncionEnPython()

    otra_funcion_en_python()

    print(funcion_con_argumentos('Saludo', 25))

    resultado = sumar(1, 2)
    print(f'El resultado de sumar los numeros {1} y {2} es: {resultado}')
    print(f'Sumar con bool {True} y el numero {15}: resultado = {sumar(15, True)}')
    print(f'Usando el dato default {restar_con_default()} y con datos asignados {[5, 8]}: {restar_con_default(5,8)}')

    lista_de_nombres = ['Juan Carlos','Ana', 'Camila', 'Andres', 'Santiago']
    diccionario_direcciones = {
        'Cliente1' : 'Dirección x',
        'Cliente2' : 'Direccion Y',
        123 : 'Emergencias',
        'Emergencias' : 123,
        True : False,
        False : True
    }

    print(lista_de_nombres)
    print(*lista_de_nombres)

    listar_nombres_y_diccionario(lista_de_nombres, diccionario_direcciones)
    print(restar_hasta_cero(7))

    #Forma de ingresar datos para que se tomen como diccionario
    diccionarios(Cliente1 = 'Dirección x', Cliente2 = 'Direccion Y', unodostres = 'Emergencias', Emergencias = 123, verdadero = False, falso = True)

print(f'''

Para imprimir segun una cantidad de dijitos:
{3.1456789}
{3.1456789:.1f}
{3.1456789:.2f}
{3.1456789:.3f}

''')

lista = [1, 2, 3, 4, 5, True, False, 'Letras', 2.5]
dicciona = {
    'd' : 'Emergencias',
    'letra' : 'Palabra',
    'a' : 'False',
    'b' : 'True',
    'c' : 'Dos medios'
}
print(lista)
print(*lista)
print(dicciona)
print([dicciona])