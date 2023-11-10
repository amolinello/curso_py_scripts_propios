from logging import exception


if __name__ == '__main__':

    def sumaTexto (textos):
        textos += 'Letras extras'
        return textos

    valorA = 3
    valorB = 5
    suma = valorA + valorB
    # Este metodo de impresión se le llama interpolación, unir el texto con la variable
    print(f'Suma = {suma}')
    resta = valorA - valorB
    print(f'Resta = {resta}')
    multiplicacion = valorA * valorB
    print(f'Multiplicación = {multiplicacion}')
    division = valorA / valorB
    print(f'Division = {division}')
    print(f'Division en entero = {int(division)}')
    modulo = valorB % valorA
    print(f'Modulo = {modulo}')
    exponente = valorA ** valorB
    print(f'Exponente = {exponente}')

    valorA += 1
    valorB -= 2
    valorA *= 2
    valorB /= 3
    valorA %= 2

    comparacion = valorA == valorB

    comparacion = valorA != valorB

    comparacion = valorA < valorB

    comparacion = valorA > valorB

    comparacion = valorA <= valorB

    comparacion = valorA >= valorB

    comparacion = valorA == 0 and valorB < 0

    comparacion = valorA != 0 or valorB > 0
    
    comparacion = not (valorA == 3)

    try:
        if (valorA < valorB or valorA/2 < valorB/3):
            print(f'El valor {valorA} o el {valorA/2} cumple la condición de {valorB} ó {valorB/3}')
        elif (valorA > valorB*5):
            print('Entro al elif')
            texto = input('Ingrese un texto que va a ser String: ')
            print(f'El texto ingresado es: {texto} en String')
        else:
            print('Entro al else')
    except:
        print('Presenta el error\n',exception)
    finally:
        print('Que hace finally?')
    try:
        tituloLibro = input('Ingrese el titulo del libro: ')
        precio = float(input('Precio: '))
        idLibro = int(input('Ingrese el ID del libro: '))
        envioGratuito = input('Envio Gratuito?: Yes = Y, No = N \t')

        if(envioGratuito.capitalize() == 'Y' or envioGratuito.capitalize() == 'YES'):
            print(f'''Información
            Libro {tituloLibro}
            ID {idLibro} 
            Precio {precio} COP
            Tiene envio gratuito''')

        elif (envioGratuito == 'N' or envioGratuito == 'NO'):
            print(f'''Libro {tituloLibro}
             ID {idLibro} 
             Precio {precio} COP 
             No tiene envio gratuito''')

        else:

            print('Ingreso un dato erroneo de envio Gratuito')

    except:
        print('Problemas...')
        print(exception)

    print('Impresión de numero como texto',str(valorA)+' texto')

    # Llamado de funcion
    resultados = sumaTexto('MENSAJE ')
    print(f'Al llamar la función tiene el resultado: {resultados} y FUNCIONA!!')


    # IF y ELSE simplificado, el ELIF no funciona con esta estructura
    opcion = True
    print(('Mensaje que salio verdadero') if opcion else ('Mensaje de que salio falso'))


    print(2 * 5 / 2 + 1) # Divide, multiplica y de último suma
