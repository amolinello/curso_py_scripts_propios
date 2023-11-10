from logging import exception


if __name__ == "__main__":
    respuesta = input('Califica de 0 a 10 como estuvo tu día: ')

    try:
        if(0 <= float(respuesta) <= 10):
            print(f'Su día fue un {respuesta}')
        else:
            print('Ingreso un numero fuera del rango')
    except:
        print('Error, dato ingresado no es un numero...')
        print(exception)