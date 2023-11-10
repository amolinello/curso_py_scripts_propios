

class Persona():
    sistema = True

    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombreNuevo):
        self._nombre = nombreNuevo

    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edadNueva):
        self._edad = edadNueva
    
    # No puede acceder a los metodos ni atributos de instancia
    # No puede recibir la palabra self, ya que esta se asocia a la instancia
    @staticmethod # Este metodo se asocia con la clase, no con el objeto
    def estadoDelSistema():
        if Persona.sistema == True:
            return '-El sistema esta: Activo'
        else:
            return '-El sistema esta: Inactivo'

    # El metodo de clase si recibe un contexto de clase
    # Solo se puede usar en metodos dentro de esta clase
    @classmethod 
    def metodoDeClase(cls):
        print(cls.sistema)
        # print(cls.edad)  # Entrega la direccion de memoria de este atributo  
        # print(cls.nombre)  # Entrega la direccion de memoria de este atributo
        if cls.sistema == True:
            return '+El sistema esta: Activo'
        else:
            return '+El sistema esta: Inactivo'

    def metodoInstancia(self):
        print('Este es el metodo de instancia')
        print(self.metodoDeClase())
        print(self.estadoDelSistema())
        print(self.sistema)

if __name__ == '__main__':
    # Estatico = Lo comparte todo objeto Persona
    juanito = Persona('Juanito', 23)
    Juanito = Persona('Juanito', 33)

    print(juanito.edad)
    print(Juanito.edad)

    print(juanito.estadoDelSistema())
    print(Juanito.estadoDelSistema())

    Juanito.sistema = False # No toma el dato de sistema que ingresa Juanito

    print(juanito.estadoDelSistema())
    print(Juanito.estadoDelSistema())

    Persona.sistema = False

    print(juanito.estadoDelSistema())
    print(Juanito.estadoDelSistema())

    Persona.sistema = True

    print('********************************************************************************')
    print(juanito.metodoDeClase())
    print(Juanito.metodoDeClase())

    Juanito.sistema = False # No toma este dato como referencia en ningun momento, el valor no cambia
    print(Juanito.sistema) # False: Almacena el valor, pero al llamar el metodo de clase no lo toma en cuenta
    print(Persona.sistema) # True:

    print(juanito.metodoDeClase())
    print(Juanito.metodoDeClase())

    Persona.sistema = False

    print(juanito.metodoDeClase())
    print(Juanito.metodoDeClase())

    juanito.metodoInstancia()
    Juanito.metodoInstancia()