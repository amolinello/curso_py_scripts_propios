from Producto import Producto
class Orden:
    contador_ordenes = 0
    
    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self._id_orden = Orden. contador_ordenes
        self._productos = list(productos)

    def agregar_productos(self, producto):
        self._productos.append(producto)
    
    def eliminar_producto(self, producto):
        self._productos.remove(producto)
    
    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio # llamar el metodo get, nunca la variable privada

        return total
    
    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__() + '\n\t'
        return f'''
        ID de Orden: {self._id_orden}
        Productos: 
        {productos_str}
        Total: {self.calcular_total()}
        '''

if __name__ == '__main__':

    producto1 = Producto('Leche',2000)
    producto2 = Producto('Harina', 4000)
    producto3 = Producto('Gaseosa', 5000)
    producto4 = Producto('Sal',2400)
    producto5 = Producto('Azucar', 3000)

    orden1 = []
    orden1.append(producto1)
    orden1.append(producto2)
    orden1.append(producto3)

    nueva_orden = Orden(orden1)
    print(nueva_orden)
    nueva_orden.agregar_productos(producto4)
    print(nueva_orden)

    
    orden2 = []
    orden2.append(producto4)
    orden2.append(producto5)

    otra_orden = Orden(orden2)
    print(otra_orden)
    otra_orden.eliminar_producto(producto4)
    print(otra_orden)