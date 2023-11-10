

varGlobal = 'Variable global'

def funcion():

    # Modificación de la variable global, global indica que se va a tener esa variable global y que se puede modificar

    global varGlobal
    varGlobal = 'texto de variable Global'
    print(varGlobal)

    variableLocal = 'Variable Local'
    print(variableLocal)

    # No se puede modificar la variable global desde la funcion como:
    # varGlobal = 'Texto'


funcion()

print(varGlobal)

# nonlocal: 


def funcion_externa():
    variable_local_externa = 'Variable local externa'

    def funcion_anidada():
        variable_local_anidada = 'variable local anidada'
        nonlocal variable_local_externa
        print(variable_local_externa+' '+ variable_local_anidada)

        variable_local_externa = 'Otro valor'
        print(variable_local_externa+' '+ variable_local_anidada)
        
    funcion_anidada()

    print(variable_local_externa)

funcion_externa()