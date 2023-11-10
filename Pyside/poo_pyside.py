import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction

class VentanaPySide(QMainWindow):
    def __init__(self):
        # Meotod init de la clase QMainWindow
        super().__init__()
        
        self.setWindowTitle('POO con PySide')

        # Ventana de tamaño fijo
        self.setFixedSize(QSize(600, 500))

        # Algunos componentes
        self._agregar_componentes()

    def _agregar_componentes(self):
        # Agregar Menú (pestañas como File, Edit, Selection, View, Go ...)
        menu = self.menuBar()
        menu_archivo = menu.addMenu('Archivo')
        opciones = menu.addMenu('Opciones')

        # Agregar opciones al menú (como nuevo, abrir, guardar, guardar como, cerrar)
        accion_nuevo = QAction('Nuevo', self)
        menu_archivo.addAction(accion_nuevo)

        # Agregar un texto a la barra de estado
        # Se muestra al poner el clic sobre "Nuevo"
        accion_nuevo.setStatusTip('Nuevo Archivo')
        
        # Agregamos un mensaje en la barra de estado
        # Se muestra al abrir la ventana
        self.statusBar().showMessage('Información de la barra de estado')

        # Botón
        boton = QPushButton('Nuevo botón')
        # Publicar el botón en la ventana
        self.setCentralWidget(boton)

if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # sys.argv = Es para recibir argumentos de la líne ade comandos
    app = QApplication([]) # Vacio
    
    # Objeto tipo ventana
    ventana1 = VentanaPySide()
    ventana1.show()

    # Ejecutamos la ventana
    sys.exit(app.exec())
