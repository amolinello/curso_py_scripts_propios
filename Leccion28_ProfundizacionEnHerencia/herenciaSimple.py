# Ejemplo

class ListaSimple:
    def __init__(self, elementos):
        self._elementos = list(elementos)

    def agregarElemento(self, elemento):
        self._elementos.append(elemento)

    def __getitem__(self, indice):
        return self._elementos[indice]

    def ordenar(self):
        self._elementos.sort()

    def __len__(self):
        return len(self._elementos)
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self._elementos!r})'

class listaOrdenada(ListaSimple):
    def __init__(self, elementos=[]):
        super().__init__(elementos)

        # Ordenamos los elementos una vez inicializados
        self.ordenar()
    
    def agregar(self, elemento):
        super().agregarElemento(elemento) # Se usa el super() ya que se esta sobrescribiendo el metodo agregar
        self.ordenar()

class listaEnteros(ListaSimple):
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
        super().agregarElemento(elemento)

if __name__ == '__main__':

    lista_simple = ListaSimple([5, 3, 6, 8])
    print(lista_simple) # Imprime: ListaSimple([5, 3, 6, 8])
    lista_ordenada = listaOrdenada([11, 3, 5, 6])
    print(lista_ordenada) # Imprime: listaOrdenada([3, 5, 6, 11])
    lista_ordenada.agregar(-10)
    print(lista_ordenada)
    print(len(lista_ordenada))
    lista_entera = listaEnteros([1, 2, 3, 4, 11, 6, 9])
    print(lista_entera)
    # lista_entera2 = listaEnteros([1, 2, 3, 4, 11, 6, 9.3])
    # print(lista_entera2)
    lista_entera.agregar(11)
    print(lista_entera)

