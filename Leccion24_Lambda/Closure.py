
# Funcion Closure es una funcion que encapsula otra funcion y mantiene un estado

def operacion(a, b):
    
    # Denifimos una funcion interna
    def sumar():
        return a + b

    return sumar

vfuncion = operacion(1,3)
print(vfuncion())
print(operacion(5,4)())
