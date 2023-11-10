# Ejemplo para ver como se reparten los metodos en herencia multiple

class Clase1:
    def __init__(self):
        print('Clase1.__init__')
    
    def metodo(self):
        print('Metodo clase1')

class Clase2(Clase1):
    def __init__(self):
        print('Clase2.__init__')

    def metodo(self):
        print('Metodo clase2')

class Clase3(Clase1):
    def __init__(self):
        print('Clase3.__init__')

    def metodo(self):
        print('Metodo clase3')

class Clase4(Clase2, Clase3):
    # va a tomar como metodo init el primero ingresado de las herencias
    # En este caso Clase2

    def metodo(self): # Si no se sobreescribe, toma el metodo de la clase2
        print('Metodo clase4')
        super().metodo() # Llama el metodo de la clase 2

if __name__ == '__main__':
    # Objeto de la clase 4
    clase4 = Clase4()
    clase4.metodo()

    # Clases padres de la clase 4 con: __bases__
    print(Clase4.__bases__)
    # Todas las clases
    print(Clase4.mro())