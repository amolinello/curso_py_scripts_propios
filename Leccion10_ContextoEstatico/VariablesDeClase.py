class MiClase:
    # Las variables de clase se comparte desde todos los objetos que se hagan a partir de esta clase

    variable_clase = 12.5
    string_clase = 'Texto random'

    def __init__(self, variable_instancia):
        self._variable_instancia = variable_instancia
    

if __name__ == '__main__':

    var1 = MiClase(2)
    var2 = MiClase(3)
    var3 = MiClase(7.5)

    print(var1._variable_instancia)
    print(var2._variable_instancia)
    print(var3._variable_instancia)

    print(var1.variable_clase)
    print(var2.variable_clase)
    print(var3.variable_clase)

    print(var1.string_clase)
    print(var2.string_clase)
    print(var3.string_clase)

    var1.string_clase = 'Nuevo Texto' # Modifica este objeto y ya no vuelve a tener esa variable como variable de clase (MiClase)
    var1.variable_clase = 10 # Modifica este objeto y ya no vuelve a tener esa variable como variable de clase (MiClase)

    print(var1._variable_instancia)
    print(var2._variable_instancia)
    print(var3._variable_instancia)

    print(var1.variable_clase)
    print(var2.variable_clase)
    print(var3.variable_clase)

    print(var1.string_clase)
    print(var2.string_clase)
    print(var3.string_clase)

    MiClase.variable_clase = 5 # Modifica todas los objetos que tengan la misma variable de clase
    MiClase.string_clase = 'Nada' # Modifica todas los objetos que tengan la misma variable de clase
    MiClase.variable_clase_nueva = 'texto' # Creando variables de clase al vuelo, de repente

    print(MiClase.variable_clase_nueva)

    print(var1._variable_instancia)
    print(var2._variable_instancia)
    print(var3._variable_instancia)

    print(var1.variable_clase)
    print(var2.variable_clase)
    print(var3.variable_clase)

    print(var1.string_clase)
    print(var2.string_clase)
    print(var3.string_clase)


