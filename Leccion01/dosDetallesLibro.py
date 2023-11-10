from logging import exception


if __name__ == "__main__":
    titulo = input('Ingrese el titulo: ')
    autor = input('Ingrese el autor: ')

    try:
        
        print(f'El titulo del libro {titulo} fue ingresado')
        print(f'El autor {autor} del libro {titulo} fue ingresado')
    except:
        print('Error, dato ingresado erroneo...')
        print(exception)