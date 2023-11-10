# Las funciones son de primer clase
# Se pueden definir en todas partes y se pueden usar como objetos

def mayusculas(texto):
    return texto.upper()


if __name__ == "__main__":

    # Uso normal
    print(mayusculas('Un texto que quiero hacer'))
    
    fobjeto = mayusculas
    print(fobjeto('Otro texto distinto'))
    print(mayusculas) # son iguales
    print(fobjeto) # son iguales

    # eliminar la referencia original
    #del mayusculas

    print(fobjeto('Otro texto distinto por otro lado'))
    # print(mayusculas) # son distintos y este da error
    print(fobjeto) # son distintos

    # Nombre por default de una funcion:
    print(f'Nombre por default {fobjeto.__name__}')

    # Almacenar función en lista
    lista_funciones = [mayusculas, fobjeto, str.lower]
    
    print(lista_funciones)

    for funcion in lista_funciones:
        print(funcion, funcion('texto en la funcion'))

    print(lista_funciones[1]('mas pruebas de mayúsculas'))

    # Se puede pasar una función a otra función
    # Funciones de mayor orden
    def saludar(argumento):
        referencia = argumento('Saludos desde la función') + ', Cosas'
        print(referencia)

    # Llamar la función
    saludar(mayusculas)

    # Closure las funciones internas pueden capturar y guardar el estado de 
    # la funcion externa / padre

    def hablar(texto, volumen):
        def minusculas():
            return texto.lower()
        def mayusculas():
            return texto.upper()
        
        if volumen > 0.5:
            return mayusculas()
        else:
            return minusculas()
        
    print(hablar('Hablando en un tono raro', 0.9))
    print(hablar('Hablando en un tono bajo', 0.2))

    print((lambda a, b: a + b)(11,12))

    lista_tuplas = [(1, 'a'),(3, 'd'),(2, 'h'), (4,'z'),(0, 'b')]
    lista_tuplas_ordenadas = sorted(lista_tuplas, key=lambda tupla: tupla[0]) # En 0 ordenar por numero, en 1 por letra
    print(lista_tuplas_ordenadas)

    def mostrar(titulo):
        return lambda mensaje: titulo + ' - ' + mensaje

    mostrar_persona = mostrar('El titulo dado')
    mostrar_texto = mostrar('Que mas escribir')
    print(mostrar_persona('Otro mensaje'))
    print(mostrar_texto("Mensaje para continuar con el texto",))


    # CUANDO UNA FUNCIÓN NO TIENE QUE RETORNAR, RETORNA -> None