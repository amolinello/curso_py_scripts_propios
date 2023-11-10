class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad
    
    def __add__(self, otro):
        return self._nombre + ' y ' + otro._nombre

    def __sub__(self, other):
        return f'La resta de las edades en valor absoluto es: {abs(self._edad - other._edad)}, donde las edades son_ {self._edad} y {other._edad}'




if __name__ == '__main__':

    # objeto1 + objeto2 es lo mismo que objeto1.__add__(objeto2)
    juan_carlos = Persona('Juan Carlos', 60)
    catalina = Persona('Catalina', 68)

    print(juan_carlos + catalina)
    print(juan_carlos - catalina)
    print(catalina - juan_carlos)