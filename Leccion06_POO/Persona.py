from unicodedata import name

# La primer letra de la clase debe ser mayuscula
# la primer letra de los metodos debe ser minuscula

# F2 sobre el nombre de una variable para renombrarlas todas

class Persona:
    def __init__(self, nombre = None, apellido = None, edad = None, *valores, **diccionario):
        # Es un metodo inicializardor
        self._name = nombre
        self.__lastname = apellido
        self._age = edad
        self._valores = valores
        self._diccionario = diccionario

        self._ciudad = None

    # Property permite que cuando se llame el metodo no sea necesario usar () se llama como atributo
    @property
    def nombre(self):
        return self._name

    # Al usar nombre.setter ya no es necesario modificar con persona.nombre('valor'), se hace persona.nombre = 'valor'
    @nombre.setter
    def nombre(self, nombre):
        self._name = nombre

    @property
    def apellido(self):
        return self.__lastname
    
    @apellido.setter
    def apellido(self, apellido):
        self.__lastname = apellido

    @property
    def edad(self):
        return self._age
    
    @edad.setter
    def edad(self, edad):
        self._age = edad

    @property
    def valores(self):
        return self._valores
    
    @valores.setter
    def valores(self, *valores):
        self._valores = valores

    @property
    def diccionario(self):
        return self._diccionario
    
    @diccionario.setter
    def diccionario(self, **diccionario):
        self._diccionario = diccionario

    def mostar_mensaje(self):
        print(f'Mensaje que {self.nombre} pide')

    def edad_menos(self):
        return self.edad - 30
        
    def __str__(self):
        return f'''
        La persona tiene:
        Nombre: {self._name}
        Apellido: {self.__lastname} 
        Edad: {self._age}
        Valores: {self.valores}
        Diccionario {self.diccionario}
        '''
    def __repr__ (self):
        return f'Es un metodo de representar la clase de otro modo'

    # Metodo destructor
    def __del__(self):
        print(f'Eliminando el objeto: Nombre: {self._name}, Apellido:  {self.__lastname}')
        


if __name__ == '__main__':

    print(type(Persona))
    civil = Persona('Juan', 'Molinello', 59, 310123123, m = 'manzana', p = 'pera', n = 123456)
    print(civil)
    print(repr(civil))
    print(civil.nombre)
    print(civil.apellido)
    print(civil.edad)
    print(civil.valores)
    print(civil.diccionario)

    civil.set_apellido = 'Molinello Arrieta'
    civil.set_nombre = 'Juan Carlos'
    civil.set_edad = 58
    print(civil)
    print(repr(civil))
    print(civil.nombre)
    print(civil.apellido)
    print(civil.edad)
    print(civil.valores)
    print(civil.diccionario)

    lista = [1, 2, 3, 4, 5, True, False, 'Letras', 2.5]
    diccionario = {
        'letra' : 'palabra',
        123 : 'Emergencia',
        True : False
    }

    # Revisar el caso del diccionario, pues al ingresarlo no veo forma de hacerlo entrar normal
    otra_persona = Persona('Ana', 'Perez', 33, *lista, diccionario= diccionario)
    print(otra_persona)
    otra_persona.mostar_mensaje()

    # Usar el _ indicamos que esta encapsulado, no lo restringe, lo pueden cambiar por fuera, simplemente es sugerencia

    otra_persona._age = 34
    print(otra_persona)

    # Para que no sea modificable es con 2 -> __ , el ejemplo se hace con apellido "lastname"
    otra_persona.__lastname = 'Ospina'
    print(otra_persona) # No se accede, simplemente no cambia el valor, salta este valor


    # No es buena practica ingresar asi a los atributos
    otra_persona.nombre = 'Ana Maria'
    print(otra_persona)

    print(civil.nombre)
    print(civil.apellido)

    # Para los atributos de solo lectura, es quitar el setter
