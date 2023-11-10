
from ast import Try
from logging import exception


estacion = None

try:
    mes = int(input('Ingrese el mes 1 - 12: '))
    if (mes == 1 or mes == 2 or mes == 12):
        estacion = 'invierno'
    elif (mes == 3 or mes == 4 or mes == 5):
        estacion = 'primavera'
    elif (mes == 6 or mes == 7 or mes == 8):
        estacion = 'verano'
    elif (mes == 9 or mes == 10 or mes == 11):
        estacion = 'otoño'
    else:
        print('Mes incorrecto')
    print(f'La estación es {estacion}')
except:
    print(f'Salio la excepción: {exception}')
finally:
    print('Continuo el proceso')

lista = [10, 20, 30]
caracter = 'z'
if(1 in lista):
    print('Esta en la lista')
if(caracter in 'letras con todo'):
    print('Tiene el caracter')