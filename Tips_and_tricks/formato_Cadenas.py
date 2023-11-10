
a = 'Nombre'
b = 'Hola, %s' % a

print(b)

#conversión
error = 500
#cadena_hexa = 'Error en hexa: %i' %error # int
cadena_hexa = 'Error en hexa: %x' %error # Hexa
cadena_hexa2 = 'Hola %s, Error en hexa: %x' %(a,error) # Hexa

print(cadena_hexa)
print(cadena_hexa2)
