# Funciones anidadas

def calculadora(a, b, operacion = 'sumar'):

    def sumar(a, b):
        return a+b

    def restar(a, b):
        return a-b

    if operacion.lower() == 'sumar':
        print(sumar(a, b))

    elif operacion.lower() == 'restar':
        print(restar(a, b))

    else:
        print('Operacion no valida')

calculadora(17,3, 'Restar')


