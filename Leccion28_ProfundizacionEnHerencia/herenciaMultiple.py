# Ejemplo

class ListaSimple:
    def __init__(self, elementos):
        self._elementos = list(elementos)

    def agregar(self, elemento):
        self._elementos.append(elemento)

    def __getitem__(self, indice):
        return self._elementos[indice]

    def ordenar(self):
        self._elementos.sort()

    def __len__(self):
        return len(self._elementos)
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self._elementos!r})'

class ListaOrdenada(ListaSimple):
    def __init__(self, elementos=[]):
        super().__init__(elementos)

        # Ordenamos los elementos una vez inicializados
        self.ordenar()
    
    def agregar(self, elemento):
        super().agregar(elemento) # Se usa el super() ya que se esta sobrescribiendo el metodo agregar
        self.ordenar()

class ListaEnteros(ListaSimple):
    # Solo acepta numeros enteros
    def __init__(self, elementos=[]):
        for elemento in elementos:
            self._validar(elemento) # Metodo protegido
        # Si no tiene ningun error, se incializa la lista
        super().__init__(elementos)

    def _validar(self, elemento):
        # Validamos si el elemento es de tipo entero
        if not isinstance(elemento, int):
            raise ValueError(f'No es un valor entero {elemento}')

    #Sobreescribir el metodo agregar
    def agregar(self, elemento):
        self._validar(elemento)
        super().agregar(elemento)

# Lista de enteros ordenada
class ListaEnterosOrdenada(ListaEnteros, ListaOrdenada): # La primer clase tiene mayor prioridad, el orden es importante
    pass


if __name__ == '__main__':

    lista_simple = ListaSimple([5, 3, 6, 8])
    print(lista_simple) # Imprime: ListaSimple([5, 3, 6, 8])
    lista_ordenada = ListaOrdenada([11, 3, 5, 6])
    print(lista_ordenada) # Imprime: listaOrdenada([3, 5, 6, 11])
    lista_ordenada.agregar(-10)
    print(lista_ordenada)
    print(len(lista_ordenada))
    lista_entera = ListaEnteros([1, 2, 3, 4, 11, 6, 9])
    print(lista_entera)
    # lista_entera2 = listaEnteros([1, 2, 3, 4, 11, 6, 9.3])
    # print(lista_entera2)
    lista_entera.agregar(11)
    print(lista_entera)

    lista_entera_ordenada = ListaEnterosOrdenada([11, 4, 7, 12, 102, -3])
    print(lista_entera_ordenada)
    lista_entera_ordenada.agregar(-20)
    print(lista_entera_ordenada)
    # Saber el orden de ejecución de los elementos de la clase
    print(ListaEnterosOrdenada.mro())
    #Imprime:
    #[<class '__main__.ListaEnterosOrdenada'>, <class '__main__.listaEnteros'>, <class '__main__.listaOrdenada'>, <class '__main__.ListaSimple'>, <class 'object'>]

    #*****************************************************************************************

    # Se va a usar el isintance
    print('Es entero? ',isinstance(10, int))
    print('Es entero? ',isinstance('cadena', int))

    print('Es una cadena? ',isinstance('cadena', str))
    print('Es una cadena? ',isinstance('11', str))

    print('Es una lista de enteros ordenada? ', isinstance(lista_entera_ordenada, ListaEnterosOrdenada))

    # Cuando la lista tiene el objeto con el que se esta evaluando en el mro, este arroja True
    #[<class '__main__.ListaEnterosOrdenada'>, <class '__main__.ListaEnteros'>, <class '__main__.ListaOrdenada'>, <class '__main__.ListaSimple'>, <class 'object'>] 
    print('Es una lista de enteros? ', isinstance(lista_entera_ordenada, ListaEnteros))
    print('Es una lista de ordenada? ', isinstance(lista_entera_ordenada, ListaOrdenada))
    print('Es una lista de simple? ', isinstance(lista_entera_ordenada, ListaSimple))
    print('Es una lista de objeto? ', isinstance(lista_entera_ordenada, object))
    
    # Si de la tupla 1 coincide, ya todo es verdadero
    print('Es una lista de objeto? ', isinstance(lista_entera_ordenada, (object, ListaSimple)))







