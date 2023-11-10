
# Aserción (Afirmación) = Condición booleana para revisar que no se tenga errores
# Si el programa encuentra un error irrecuperable, debe
# arrojar un Assertion (ayuda a depurar el programa de errores)


def dividir(a,b):
    assert b != 0, 'División entre cero'
    # Si no tiene errores
    print(f'El resultado de la división es: {a/b:0.2f}')

# Calculo promedio de lista de calificaciones
def obtener_promedio(calificaciones):

    assert len(calificaciones) != 0, "Lista de calificaciones vacia"

    print(f'El promedio de calificaciones es: {sum(calificaciones)/len(calificaciones)}')

# Descuento al producto
def aplicar_descuento(productos, descuento):
    precio_con_descuento = productos['precio'] * (1.0-descuento)
    print(f"Nuevo precio del producto: {precio_con_descuento:.1f}")
    assert 0 <= precio_con_descuento < productos['precio'], f'Descuento invalido: {precio_con_descuento:.2f}'
    print('Descuento valido')



if __name__ == "__main__":

    print('*'*50)
    # 1. Prueba división con aserción en división por 0
    dividir(5, 2)
    dividir(933, 37)
    # dividir(305, 0)
    print('*'*50)
    # 2. Prueba en promedio de calificaciones
    obtener_promedio((1,2,3,4,5,6))
    obtener_promedio([2,2,2,2,2,2])
    #obtener_promedio([])
    print('*'*50)
    # 3. Prueba descuento a productos
    producto = {'nombre':'Camisa', 'precio':2500}
    aplicar_descuento(producto, 0.2)
    
    print('*'*50)
