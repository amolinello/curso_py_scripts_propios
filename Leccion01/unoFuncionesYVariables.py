from array import array


variable = []
for x in range(2, 20, 4):
    variable.append(x)

# X toma valor del 2 hasta llegar al monto 20 o lo mas cercano por debajo.
# Tiene pasos de 4

print(variable)

# Ejercicio

nombre = "Cadena de texto"
telefono = 1234567892030
email = "correo@mail.com"

# email : int = "Valores" el int solo es para indicar que tipo de dato tiene
# pero es solo como aviso, no es obligatorio

print(f"Información: {nombre}, Telefono: {telefono}, email: {email}")

y = True
print(y)
print(type(y))

y = 'c'
print(y)
print(type(y))

y = 12.32
print(y)
print(type(y))

y = 11
print(y)
print(type(y))

y = "Mensaje"
print(y)
print(type(y))
print("mensaje" " aje" " aje")

print("Union: ", y)
x = '1'
y = '2'
print("Mensaje", x+y)
print(int(x+y))
print(int(x)+int(y))

if int(x) > 0:
    print("True")
elif int(x) < 0:
    print(f'Mensaje con x {x}')
else:
    print("False")

mensaje = input('Ingresar Mensaje ')
print("Usted ingreso: ", mensaje)
print(f'O escrito con f es: {mensaje}')

if __name__ == "__main__":
    print("Esto se esta ejecutando acá")