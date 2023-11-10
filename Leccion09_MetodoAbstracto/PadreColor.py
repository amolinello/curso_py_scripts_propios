
class PadreColor():
    def __init__(self, color):
        self._color = color
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, NuevoColor):
        self._color = NuevoColor
    
    def __str__(self):
        return f'El color es: {self._color}'