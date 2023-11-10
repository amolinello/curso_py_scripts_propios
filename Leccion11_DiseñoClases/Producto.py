
class Producto:

    contador_productos = 0

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1
        self._id_producto = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    def __str__(self):
        return f'ID: {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio}'
    

if __name__ == '__main__':
    nuevo1 = Producto('leche',2000)
    nuevo2 = Producto('harina', 4000)
    print(nuevo1)
    print(nuevo1.contador_productos)
    print(nuevo2)
    print(nuevo2.contador_productos)
