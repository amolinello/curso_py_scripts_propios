from Empleado import Empleado
from Gerente import Gerente

# Polimorfismo: Multiples formas en tiempo de ejecución

def imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles()) # Se utiliza el metodo definido en ambas clases

    # Si queremos acceder a departamento - de gerente
    # Se usa el metodo isinstance para preguntar si el objeto que decimos pertenece a cierta clase
    if isinstance(objeto, Gerente):
        print(f'El gerente tiene departamento: {objeto.departamento}, que bueno!')
    else:
        print('Es tipo empleado y no tiene departamento')

if __name__ == '__main__':
    empleado = Empleado('Chon Lee', 20)
    gerente = Gerente('Katara ta', 9000000, 'Perruno')

    imprimir_detalles(empleado)
    imprimir_detalles(gerente)
