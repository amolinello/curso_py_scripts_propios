class DispositivoEntrada:
    def __init__(self, tipo_entrada, marca): # Solo un _ significa que es de tipo protegido
        self._tipo_entrada = tipo_entrada
        self._marca = marca

    @property
    def tipo_entrada(self):
        return self._tipo_entrada
    
    @tipo_entrada.setter
    def tipo_entrada(self, tipo_entrada):
        self._tipo_entrada = tipo_entrada

    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, marca):
        self._marca = marca
    
    def __str__(self):
        return f'''Tipo de Entrada: {self._tipo_entrada} / Marca: {self._marca}'''
    
if __name__ == '__main__':
    objetoPrueba = DispositivoEntrada('USB', 'HP')
    print(objetoPrueba)
    objetoPrueba.marca = 'Inter'
    objetoPrueba.tipo_entrada = 'USB C'
    print(objetoPrueba)