# QAplication = Permite procesar los eventos de la
# aplicación (clic, mover, disminuir, etc)

import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

# Clase base de Qt (PySide) solo debe tener 1 por aplicación
# Se encarga de procesar los eventos (event loop)
app = QApplication()
# Se puede acceder a algunas caracteristicas y su configuración
# La clase esta orientada a crear objetos tipo ventana
ventana = QMainWindow()

'''
# Usando un botón en lugar de una ventana
ventana = QPushButton('Boton de PySide')
# Cualquier componente puede ser una ventana en PySide
'''
# Cambiar el título
ventana.setWindowTitle('Hola Mundo con PySide')
# Modificar el ancho y alto de la ventan (tamaño)
ventana.resize(1000, 680)
# Mostrar la ventana
ventana.show()

# Se ejecuta la aplicación
sys.exit(app.exec())
