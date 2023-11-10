from logging import exception


if __name__ == '__main__':
    
    try:
        variable = int(input('Ingrese un número: '))
        if(variable%2 == 0):
            print(f'El valor {variable} es un número par')
        else:
            print(f'El valor {variable} es impar')
    except:
        print('Error en el ingreso de datos')
        print(exception)