
# Multiplicación STR

mensaje = 'Texto'*5
print(f'El mensaje es: {mensaje}')

lista = [1,2,3,4]
listados = ['a','bc','d']
tupla = (1,2,3,4,5)
tupla2 = ('hola','mundo','dos')

# Comparten la misma dirección de la información
lista3 = lista
lista3[1] = 9
# El cambio se ve en las 2 variables

# Esta es una forma de copiar ************************************************
lista4 = list(lista)
lista4[3] = 10
print(f'El lista 4 es: {lista4}')
# ****************************************************************************

print(f'El mensaje 1 es: {lista*2}')
print(f'El mensaje 2 es: {listados*2}')
print(f'El mensaje 3 es: {tupla*2}')
print(f'El mensaje 4 es: {tupla2*2}')

listanumero = 10*[0]
print(f'La lista numero es: {listanumero} de largo: {len(listanumero)}')

# Caracteres de Escape, pueden causar problemas a la hora de usarlos

resultado = 'Hola \' Mundo'
print(f'Resultado: {resultado}')

resultado = 'Hola Mundo, eliminando el punto.\b'
print(f'Resultado: {resultado}')

resultado = 'Hola Mundo, sin eliminar el punto y dejando el diagonal b.\\b'
print(f'Resultado: {resultado}')


# Raw string = cadena simple

resultado = r'Cadena con \n salto de linea'
print(f'Resultado: {resultado}')

# Caracteres Unicode - Todos los caracteres de python se representan con este juego de caracteres

print('Hola\u0020Mundo')
print('Hola\u0040Mundo')
print('\u2766')

# ASCII

print(f'Mensaje con ASCII: {chr(65)}')


# Caracteres tipo bytes

caracteres_en_bytes = b'Mensaje escrito'
print(f'Respuesta: {caracteres_en_bytes}, tipo: {type(caracteres_en_bytes)}')
print(f'Respuesta: {caracteres_en_bytes[0]}, tipo: {type(caracteres_en_bytes[0])}') 
# El decimal se basa en typo ASCII
print(f'Como caracter: {chr(caracteres_en_bytes[0])}')

lista_caracteres = caracteres_en_bytes.split()
print(f'Lista: {lista_caracteres}')

# Convertir STR a Bytes
texto = 'Un texto muy raro terminación'
print(f'String: {texto}')

byte = texto.encode('UTF-8')
print(f'Bytes codificado: {byte}')

# Convertir Bytes a STR
texto2 = byte.decode('UTF-8')
print(f'STR decodificado: {texto2}')

print(texto == texto2)


# Contar veces que se repite una palabra en una cadena

cadena = '''
    Un texto con datos y
    largo para probar
    cuantas veces
    se repite la palabra texto
    en el texto 
'''

# Cuenta las veces que se repite 'texto' en la cadena
print('Numero de veces que se repite:', cadena.count('texto')) 
print(cadena.upper())
print(cadena)
print(cadena.lower())
print(cadena)

print(' TEXTO '.lower() in cadena.lower())
print(' texto '.upper() in cadena.upper())

print(cadena.startswith('\n\tUn'))
print(cadena.endswith('\n'))
print(cadena.islower())
print(cadena.isupper())

# Centrar Strings

print('mensaje'.center(30, 'U'))
cuadroTexto = '     Un mensaje dedicado para hacer pruebas     U'
print(len(cuadroTexto))
print(cuadroTexto.ljust(len(cuadroTexto)+10,'+'))
print(cuadroTexto.rjust(len(cuadroTexto)+13,'*'))

# Metodo de replace

print(cuadroTexto.replace('a', 'i'), len(cuadroTexto))

# Metodo de strip
conStrip = cuadroTexto.strip() # Borra todos los espacios " " al inicio y final del texto
print(conStrip, len(conStrip))

conStrip = cuadroTexto.strip(' U') # Borra todos los espacios " " al inicio y final del texto y la U
print(conStrip, len(conStrip))

# Se tiene lstrip() y rstrip() para quitar los elementos de lado izquierdo o derecho

conStrip = cuadroTexto.strip().strip('U').strip('n')
print(conStrip, len(conStrip))