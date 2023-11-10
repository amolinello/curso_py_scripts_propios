
import sys
from functools import partial
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QLineEdit, QGridLayout, QPushButton
from PySide6.QtCore import Qt

class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.setFixedSize(235,235)
        
        self.componente_general = QWidget(self)
        self.setCentralWidget(self.componente_general)
        # Creación del layout principal
        self.layout_principal = QVBoxLayout()
        self.componente_general.setLayout(self.layout_principal)
        # Metodo para crear la parte visual de la calculadora
        self._crear_area_captura()

        # Agregamos los botones
        self._crear_botones()
        
        # Conectamos las señales con los slots
        self._conectar_botones()

    def _crear_area_captura(self):
        self.linea_entrada = QLineEdit()
        # Modificar algunas propiedades
        self.linea_entrada.setFixedHeight(35)
        self.linea_entrada.setAlignment(Qt.AlignRight)
        self.linea_entrada.setReadOnly(True) # Modo solo lectura

        #Agregar al Layout principal
        self.layout_principal.addWidget(self.linea_entrada)

    def _crear_botones(self):
        # Diccionario para definir cada boton
        self.botones = {}
        layout_botones = QGridLayout()
        # Texto | Posición en el grid layout
        self.botones = {
            '7':(0,0), '8':(0,1), '9':(0,2), '/':(0,3),
            '4':(1,0), '5':(1,1), '6':(1,2), '*':(1,3),
            '1':(2,0), '2':(2,1), '3':(2,2), '-':(2,3),
            '0':(3,0), '.':(3,1), 'C':(3,2), '+':(3,3), '=':(3,4),
        }

        # Crear los botones y agregarlos al grid layout
        for text_boton, posicion in self.botones.items():
            self.botones[text_boton] = QPushButton(text_boton)
            self.botones[text_boton].setFixedSize(40, 40)

            # Publicar el botón en el grid Layout
            layout_botones.addWidget(self.botones[text_boton], posicion[0], posicion[1])

        # Agregar el Layout de botones al layout principal
        self.layout_principal.addLayout(layout_botones)

    def _conectar_botones(self):
        # Recorrer cada botón del diccionario
        for text_boton, boton in self.botones.items():
            if text_boton not in {'=','C'}:
                # boton.clicked.connect(lambda: self._construir_expresion(text_boton))
                boton.clicked.connect(partial(self._construir_expresion, text_boton))

            # Conectar el botón 'C'
            self.botones['C'].clicked.connect(self._limpiar_linea_entrada)
            # Conectar el botón igual '='
            self.botones['='].clicked.connect(self._calcular_resultado)
            self.linea_entrada.returnPressed.connect(self._calcular_resultado)

    def _construir_expresion(self, text_boton):
        expresion = self.obtener_texto() + text_boton
        # Actualizamos la expresión
        self.actualizar_texto(expresion)

    def obtener_texto(self):
        return self.linea_entrada.text()
    
    def actualizar_texto(self, texto):
        self.linea_entrada.setText(texto)
        self.linea_entrada.setFocus()

    def _limpiar_linea_entrada(self):
        self.actualizar_texto('')

    def _calcular_resultado(self,):
        resultado = self._evaluar_expresion(self.obtener_texto())
        self.actualizar_texto(resultado)

    def _evaluar_expresion(self, expresion):
        try:
            # Utilizar la funcion eval para evaluar la expresión
            resultado = str(eval(expresion))   
        except Exception as e:
            resultado = 'Ocurrio un error'

        return resultado

if __name__ == "__main__":
    app = QApplication()
    calculadora = Calculadora()
    calculadora.show()
    sys.exit(app.exec())