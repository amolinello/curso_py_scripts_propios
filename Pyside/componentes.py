
# Componentes = Widgets
# Existe el checkbox, combo box, dial o marcador, slide, etc

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

class Componentes(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Componentes')
        self.setFixedSize(1000,700)
        
        # Crear un nuevo checkbox
        checkbox = QCheckBox("Este es un checkbox")
        # Activar el 3er estado
        checkbox.setTristate(True)
        checkbox.stateChanged.connect(self.mostrar_estado)

        '''
        # Crear componente Label, etiqueta
        etiqueta = QLabel('Hola')
        # Modificar el valor inicial
        etiqueta.setText('Saludos')
        # Modificar la fuente
        fuente = etiqueta.font()
        fuente.setPointSize(25) # Por default es 12
        etiqueta.setFont(fuente)
        # Modificar la alineación de la etiqueta
        etiqueta.setAlignment(Qt.AlignCenter)
        etiqueta.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        #Mostrar una imagen con la etiqueta
        etiqueta.setPixmap(QPixmap("66138.jpg"))
        etiqueta.setScaledContents(True)
        # Publicar el componente
        self.setCentralWidget(etiqueta)
        '''
        
        self.setCentralWidget(checkbox)
        
    def mostrar_estado(self, estado):
        print('Estado del checkbox', estado)
        # 2 es check, 0 es sin check y el 1 es parcialmente, pero debe ser declarado
        # Trabajar con las constantes
        print(Qt.Checked)
        print(estado)

        # No funciona, revisar
        # if estado == Qt.Checked:
        #     print("Casilla marcada")
        # if estado == Qt.Unchecked:
        #     print("Casilla desmarcada")
        # if estado == Qt.PartiallyChecked:
        #     print("Casilla neutra")
        # else:
        #     print('Estado no valido')
        


if __name__ == "__main__":
    app = QApplication()
    ventana = Componentes()
    ventana.show()
    sys.exit(app.exec())


