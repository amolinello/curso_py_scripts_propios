
# Permite ampliar la funcionalidad, agregar mas caracteristicas sin tener que modificarla directamente

# Decorador: Funcion que recibe un funcion y entrega otra, se usa para extender la funcionalidad


# 1. Funcion decorador(a)
# 2. Funcion a decorar (b)
# 3. Funcion decorada (c)


#Decorador
def funcion_decorador_a(funicion_a_decorar_b):
    def funcion_decorada_c():
        print('Inicio')
        funicion_a_decorar_b()
        print('Final')

    return funcion_decorada_c


@funcion_decorador_a
def mostrar_mensaje():
    print('mensaje dado')

mostrar_mensaje()
print()
# Al llamar la función, llama al decorador y se pueden realizar cambios sobre la funcion ya creada

def imprimir():
    print('cosas')

imprimir()

print()

@funcion_decorador_a
def imprimirDos():
    print('cosas')

imprimirDos()