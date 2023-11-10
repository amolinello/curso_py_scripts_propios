# Se pueden crear clases de excepcion, es crear la excepción que queramos 
class numeroExcepcion(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

if __name__ == '__main__':  

    a = 10
    b = 0
    c = 0

    # try:
    #     a = 10
    #     b = 0
    #     c = 0
    #     c = a / b
    #     print(c) # No ejecuta esta linea ya que el error esta arriba
    # finally:
    #     print(c)
    #     print('Siempre se ejecuta')
    #     # Se ejecuta y hace el finally, luego arroja la excepcion

    try:
        c = a / b
        d = {a:1,b:2,c:3}
        z = int(input('Ingrese un numero entero: ')) # Si no es entero, entrega error
        print(z)
        y = int(float(input('Ingrese otro numero entero: '))) # Redondea el numero por debajo. 2.5 ó 2.2 ó 2.7 ó 2.9 = 2
        print(y)
        #print(d[1])
        if z == y:
            raise numeroExcepcion('Numeros Identicos')

    except  ZeroDivisionError as excep:
        print(f'El error dio: {excep}')
        raise Exception('Grave ERROR!! NO SE DIVIDE POR 0')

    except TypeError as excep:
        print(f'El error dio: {excep}')

    except Exception as ex:
        print(f'Otro tipo de error {ex}, {type(ex)}')

    else:
        print('Tambien hace esto si no tiene excepcion y si no completa la condición del raise')

    finally:
        print('cerrar archivos o hacer otra cosa')

    print('hacer cosas a parte') # Si da el error de dividir por 0 NO imprime esto (tiene el raise), los otros si imprime

