
from re import X
from unittest import case


bandera = 1
condicion = False

while (bandera <= 10):
    print(f'La bandera va en el valor: {bandera} no pasa de 11')
    bandera+=1

lista = [10, 12, 3, 5, 9, 100, 30000,'texto', True, 12.5, 11]

for x in lista:
    print(x)
    if condicion == True:
        print('Sale del ciclo')
        break
    elif condicion == 'texto':
        print('imprime antes de repetir el ciclo')
        continue
    else:
        print('por llenar')
    print('No entro a las comparaciones')

# No existe un switch como tal en python, pero este es mas rapido que usar solo if
# Es mejor usar los diccionarios para estos casos

diccionario = {
    0:'texto 0',
    1:'texto 1',
    2:'texto 2',
    3:'texto 3',
    4:'texto 4',
    5:'texto 5',
}

print('Resultado: '+diccionario[2])

# El break se usa cuando se encuentra el elemento que se busca en el ciclo

# Continue se usa para saltar algún paso en el ciclo

for i in range(6):
    # Imprime del 0 al 5, son 6 elementos, pero comienzan por 0
    print(i)

for j in range(2, 20, 4):
    # Inicia con el valor 2, se suma 4, queda en 6 y sigue así hasta el 18 y no toma mas valores
    print(j)
print(j)
