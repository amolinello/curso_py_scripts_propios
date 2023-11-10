# QAplication = Permite procesar los eventos de la
# aplicación (clic, mover, disminuir, etc)

import sys
from PySide6.QtWidgets import QApplication, QWidget

# Clase base de Qt (PySide) solo debe tener 1 por aplicación
# Se encarga de procesar los eventos (event loop)
app = QApplication()

# Objeto ventana para visualizar la aplicación, puede tener
# varios objetos tipo ventana (Widget)
# La ventana no se muestra por default
ventana = QWidget()
# Cambiar el título
ventana.setWindowTitle('Hola Mundo con PySide')
# Modificar el ancho y alto de la ventan (tamaño)
ventana.resize(1920, 1080)
# Mostrar la ventana
ventana.show()

# Se ejecuta la aplicación
sys.exit(app.exec())
