# Ejemplo atributos publicos, protegidos y privados

class Miclase:
    def __init__ (self, publico, protegido, privado):
        self.publico = publico
        self._protegido = protegido
        self.__privado = privado

objeto = Miclase('Valor publico', 'Valor protegido', 'Valor privado')

print(objeto.publico)

# Modificar el valor publico

objeto.publico = 'Nuevo valor publico'
print(objeto.publico)

#print(objeto._protegido) # No deberiamos accederlo, solo para utilizar en la clase o en las clases hijas

# print(objeto.__privado) # Entrega un error, ya que python oculta el atributo
# Python lo convierte como: objeto._nombreClase__atributo_privado
print(objeto._Miclase__privado)