
# Signals y slots
# Eventos y funciones que procesan los eventos

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals and Slots')
        self.setMinimumSize(400, 400)

        # Botón
        self.boton = QPushButton('Clic aquí')

        # Componente para escribir (QLineEdit)
        self.entrada_texto = QLineEdit()

        # Etiqueta para ver lo escrito (QLabel)
        self.etiqueta = QLabel()

        # Conectar el widget de entrada de texto con la etiqueta
        # La señal es textChanged y el slot es setText
        self.entrada_texto.textChanged.connect(self.etiqueta.setText)

        # Layout: Manera de agregar varios elementos a la ventana
        disposicion = QVBoxLayout() # Vertical
        disposicion.addWidget(self.entrada_texto)
        disposicion.addWidget(self.etiqueta)
        disposicion.addWidget(self.boton)

        # Crear contenedor para publicar el layout
        contenedor = QWidget()
        contenedor.setLayout(disposicion)

        # Asociar la señal de click al slot evento_click
        self.boton.clicked.connect(self.evento_clickeado)
        
        # Conectar a la señal de cambio de titulo
        self.windowTitleChanged.connect(self.cambio_titulo_ventana)

        '''

        # Conectar el evento checado (para saber si fue oprimido, es False por default)
        # Muestra el botón como oprimido al dar clic una vez, la 2da lo quita
        self.boton.setCheckable(True)
        
        # Conectar otro slot al evento checar
        self.boton.clicked.connect(self.evento_checar)

        # Conectar el evento (signal) click con el slot (evento_click)
        self.boton.clicked.connect(self.evento_click)
        
        

        # Publicar el botón
        self.setCentralWidget(self.boton)
        '''

        self.setCentralWidget(contenedor)

    def evento_click(self):
        print('Se hizo clic', self.boton_checado)

    def evento_checar(self, checar):
        self.boton_checado = checar
        # Checar es el estado del botón, True o False
        print('Cheked?:',self.boton_checado)

    def evento_clickeado(self):
        self.boton.setText('Nuevo Texto del botón')
        self.boton.setEnabled(False) # Desabilitar el botón
        self.setWindowTitle('Nuevo titulo de la app')
        self.resize(500,500)
        print('Evento click')

    def cambio_titulo_ventana(self, nuevoTitulo):
        print('Cambio el titulo .-. por: ', nuevoTitulo)


if __name__ == "__main__":
    # Crear el objeto de aplicación
    app = QApplication()

    # Crear una instancia de la clase
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())

