# 5. Imprimir cuales elementos tienen la misma longitud
import datetime
import re
import sys


def comparar(longitud_lista=0, longitud_tupla=0, longitud_set=0, longitud_dic=0):
    # Elementos permite saber a que elemento pertenece cada longitud
    elementos = {'lista':longitud_lista, 'tupla':longitud_tupla, 'set':longitud_set,'diccionario':longitud_dic}
    # Lista de longitudes
    valores = list(elementos.values())
    # Longitud máxima
    lmaximo = max(elementos.values())
    # Longitud mínima
    lminimo = min(elementos.values())

    maxima_cuenta = 1
    v_repetido = set()
    repite = dict()
    
    # Ciclo que permite saber que longitudes se repiten mas
    for elemento in valores:
        if valores.count(elemento) >= maxima_cuenta:
            v_repetido.add(elemento)
            maxima_cuenta = valores.count(elemento)

    # Ciclo que permite saber a que elementos pertenece la longitud que mas se repite
    for valor in v_repetido:
        lista_repetido = []
        for llave in elementos.keys():
            if elementos[llave] == valor:
                lista_repetido.append(llave)
        # Crea un diccionario con llave = longitud mas repetida y valores = nombre del elemento mas repetido
        repite[valor] = lista_repetido

    print(f'La longitud máxima es: {lmaximo}')
    print(f'La longitud mínima es: {lminimo}')

    # Verificación de que se tenga longitudes repetidas
    if maxima_cuenta >1:
        print(f'''Las longitudes repetidas son: {v_repetido} y se repite: {maxima_cuenta} veces.
        
        {repite}
        ''')
    else:
        print('Ninguna longitud se repite')

if __name__ == '__main__':
    # 1. Encontrar la longitud de la lista
    lista = [1, 2, '', 3, True, 'Algo', [1,2]]
    lista.append('abc')
    longitudl = len(lista)
    print(f'1. La longitud de la lista {lista} es: {longitudl} y es de tipo: {type(lista)}')

    # 2. Encontrar la longitud de la tupla
    tupla = (11, 15, 33, 99, 33, 15, 11, 'cosas diferentes', 1 == True, 1 is True)
    longitudt = len(tupla)
    print(f'2. La longitud de la tupla {tupla} es: {longitudt} y es de tipo: {type(tupla)}')

    # 3. Encontrar la longitud del elemento set
    #var_set = set([11, 33, 33, 15, 11, 1, 0])
    var_set = {11, 33, 33, 15, 11, 1, 0, 22, 17, 18, 19, 20}
    longituds = len(var_set)
    print(f'3. La longitud del set {var_set} es: {longituds} y es de tipo: {type(var_set)}')

    # 4. Encontrar la longitud del diccionario
    diccionario = {'a':'A', 'b':1, 2:'b', True:False, 3:'Un mensaje', 'lista':[11,12,13], 'numero':99}
    longitudd = len(diccionario)
    print(f'4. La longitud del diccionario {diccionario} es: {longitudd} y es de tipo: {type(diccionario)}')

    # 5. Imprimir cuales elementos tienen la misma longitud
    comparar(longitudl, longitudt, longituds, longitudd)

    # 6. Imprimir los números pares del 1 al 100
    pares = [x+2 for x in range(0, 100,2)]
    print(pares)

    # 7. Imprimir los números impares del 1 al 100
    impares = [x+1 for x in range(0, 100,2)]
    print(impares)
    
    # 8. Imprimir los números primos del 1 al 100
    primos = lambda num : all([ num % i for i in range(2, num)]) # REVISAR

    a = 11
    b = type(a)
    print(b)

    b = {1:2, 3:4, 5:6}
    print(b.get(6))
    c = 7
    #print(c.__str__())

    #print(set([1,2,3])==set([1,2]))
    print("hello"'world'*2)

    class test():
        id= 0
        def __init__(self, id):
            self.id = id
            id = 2

    g = 1,2,3,4,5,6
    m = re.search(r'(ab[cd]?)', '''acdeabdabcde''')
    print(m.groups())

    print(sys.path)

    print(type(datetime.date(2012, 1, 1)-datetime.date(2011,1,1)))
