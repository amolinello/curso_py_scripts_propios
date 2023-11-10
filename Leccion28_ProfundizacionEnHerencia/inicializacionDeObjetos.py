# Orden de inicialización de objetos

class Padre:
    def __init__(self) :
        print('Inicializador padre')

    def metodo(self):
        print('Metodo padre')

class Hijo(Padre):
    #pass # Si tiene pass la clase hija trae el metodo Init del padre
    
    def __init__(self):
        print('Metodo inicializador de la clase hija')
        print(f'El metodo de la clase padre es: ')
        super().__init__() # Init de la clase padre

    # Sobrescribir el metodo heredado de la clase padre

    def metodo(self):
        print('Metodo sobrescrito por parte del hijo')
        super().metodo() # metodo de la clase padre

if __name__ == '__main__':
    # Creación de objetos padre
    padre1 = Padre()
    padre1.metodo()

    # Creación de objetos hijo
    print('\nObjetos Hijo\n')
    #hijo1 = Hijo() # Si tiene pass, la clase hija trae el metodo Init del padre
    hijo1 = Hijo()
    
    # hijo1.metodo() # llama al metodo del padre que hereda, si no se hace sobrescritura de este
    hijo1.metodo()
