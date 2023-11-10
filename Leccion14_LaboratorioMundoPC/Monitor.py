
class Monitor:
    contador_monitor = 0
    def __init__(self, marca, tamaño):
        Monitor.contador_monitor += 1
        self.__id_monitor = Monitor.contador_monitor
        self.__marca = marca
        self.__tamaño = tamaño
    
    @property
    def id_monitor(self):
        return self.__id_monitor

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def tamaño(self):
        return self.__tamaño

    @tamaño.setter
    def tamaño(self, tamaño):
        self.__tamaño = tamaño

    def __str__(self):
        return f'''
        {' Monitor: '.center(60, '-')}
        ID: {self.__id_monitor} / Marca: {self.__marca} / Tamaño: {self.__tamaño}'''

if __name__ == '__main__':
    monitorPrueba = Monitor('USB', '1500')
    print(monitorPrueba)
    monitorPrueba.marca = 'Otra Marca'
    monitorPrueba.tamaño = '1800'
    print(monitorPrueba)

    monitorPrueba2 = Monitor('HDMI', '1800')
    print(monitorPrueba2)