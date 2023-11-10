
# Generar numeros del 1 al 5

def generador_numeros():
    for num in range(1, 6):
        yield num
        print(f'Reanuda la operacion')

generador = generador_numeros()
print(f'Objeto: {generador}')
print(f'Tipo: {type(generador)}')

for valor in generador:
    print(valor)

generador = generador_numeros()
try:
    print(f'Valor: {next(generador)}')
    print(f'Valor: {next(generador)}')
    print(f'Valor: {next(generador)}')
    print(f'Valor: {next(generador)}')
    print(f'Valor: {next(generador)}')
    print(f'Valor: {next(generador)}')

except StopIteration as ex:
    
    print(f'errorrrrr: {ex}')

finally:
    print('El error puede o no ocurrir y de todos modos ejecuta esto')

generador = generador_numeros()

while True:
    try:
        valor = next(generador)
        print(f'El valor es: {valor}')
    except StopIteration as ex:
        print('Termino de iterar')
        break
    except Exception as ex:
        print('Ocurrió un error')
        break