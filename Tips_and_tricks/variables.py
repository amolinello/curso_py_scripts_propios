
class Perro:
    no_patas = 4 # Variable de clase

    def __init__(self, name):
        # Variable de instancia
        self.name = name

mascota1 = Perro('Katara')
mascota2 = Perro("Chon")
print(mascota1.name) 
print(mascota1.no_patas) # 4
print(mascota2.name)
print(mascota2.no_patas) # 4
print(Perro.no_patas) # 4

Perro.no_patas = 10
print(' Cambio!!! '.center(50, '*'))
print(mascota1.name)
print(mascota1.no_patas) # 10
print(mascota2.name)
print(mascota2.no_patas) # 10
print(Perro.no_patas) # 10

print(' Cambio!!! '.center(50, '*'))
mascota1.no_patas = 4
print(mascota1.name)
print(mascota1.no_patas) # 4
print(mascota2.name)
print(mascota2.no_patas) # 10
print(Perro.no_patas) # 10

print(' Cambio!!! '.center(50, '*'))
Perro.no_orejas = 2
print(mascota1.name)
print(mascota1.no_orejas) # 2
print(mascota2.name)
print(mascota2.no_orejas) # 2
print(Perro.no_orejas) # 2

# Contador de objetos de una clase

class ContadorObjetos:
    no_instancias = 0

    def __init__(self):
        # incrementar la variable de clase
        self.__class__.no_instancias += 1

print('Contador de instancias:')
print(ContadorObjetos.no_instancias)
print(ContadorObjetos().no_instancias) # Crea objeto y llama la variable
print(ContadorObjetos().no_instancias) # Crea objeto y llama la variable
print(ContadorObjetos().no_instancias) # Crea objeto y llama la variable
print(ContadorObjetos().no_instancias) # Crea objeto y llama la variable
print(ContadorObjetos.no_instancias)



class MiClase:
    
    def metodo_instancia(self):
        return 'Metodo de instancia ejecutado', self

    @classmethod
    def metodo_clase(cls):
        return 'Metodo de clase ejecutado', cls
    
    @staticmethod
    def metodo_estatico():
        return 'Metodo estatico'
    # No tiene información a los objetos o a la clase
    # Para utilería o realizar calculos
    
# Caso 1. Meotodo de instancia de manera implicita
objeto = MiClase()
print(' 1. '.center(50, '-'))
print(objeto.metodo_instancia()) # Llama al objeto
print(objeto.metodo_clase()) # Llama a la clase

# Caso 2. Ejecutamos el metodo de instancia de manera explicita
print(' 2. '.center(50, '-'))
print(MiClase.metodo_instancia(objeto))

# Caso 3. Ejecutamos el metodo de instancia desde la clase
print(' 3. '.center(50, '-'))
print(MiClase.metodo_instancia(MiClase))

# Caso 4. Ejecutamos el metodo de la clase
print(' 4. '.center(50, '-'))
print(MiClase.metodo_clase())

# Caso 5. Ejecutamos el metodo estatico
print(' 5. '.center(50, '-'))
print(MiClase.metodo_estatico())

# Caso 6. Ejecutamos el metodo estatico desde la instancia
print(' 6. '.center(50, '-'))
print(objeto.metodo_estatico())
