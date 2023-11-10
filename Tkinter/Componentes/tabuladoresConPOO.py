from time import sleep
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

class ComponentesVentana(tk.Tk):
    def __init__(self):
        super().__init__() # Inicializar el componente de la clase padre
        self.geometry('650x400+450+200') # Lo que esta en mas es para especificar donde debe aparecer
        self.title('Componenetes')
        self.iconbitmap('icono.ico')
        self._crear_tabs()

    def _crear_componentes_tabulador1(self, tabulador):
        #Agregar una etiqueta y un componente de entrada
        etiqueta1 = ttk.Label(tabulador, text='Esta es la prueba de tabuladores')
        etiqueta1.grid(row=0, column=0, sticky=tk.E)
        entrada1 = ttk.Entry(tabulador, width=30)
        entrada1.grid(row=0, column=1, padx=5, pady=5)

        # Agregar un botón

        def enviar():
            messagebox.showinfo('Mensaje', f'Texto ingresado: {entrada1.get()}')

        boton1 = ttk.Button(tabulador, text='Enviar', command=enviar)
        boton1.grid(row=1, column=0, columnspan=2)

    def _crear_componentes_tabulador2(self, tabulador):
        contenido = 'Este es mi texto con el contenido'
        # Componente de scroll
        scroll = scrolledtext.ScrolledText(tabulador, width=50, height=10, wrap=tk.WORD)
        # WORD es para que lleve la palabra completa

        scroll.insert(tk.INSERT, contenido)
        # Mostramos el componente
        scroll.grid(row=0, column=0)

    def _crear_componentes_tabulador3(self, tabulador):
        # Creamos una lista usando data list comprehension
        datos = [x+1 for x in range(10)] # Muestra datos de 1 a 10 (range da de 0 a 9)
        combobox = ttk.Combobox(tabulador, width=15, values=datos)
        combobox.grid(row=0, column=0, padx=10, pady=10)

        # Seleccionar un elemento por default a mostrar
        combobox.current(6)
        # Agregar un botón para sabe la opción seleccionada por el usuario
        def mostrarValor():
            messagebox.showinfo('Valor seleccionado', f' Valor seleccionado: {combobox.get()}')

        boton1 = ttk.Button(tabulador, text='Mostrar valor seleccionado', command=mostrarValor)
        boton1.grid(row=0, column=1)

    def _crear_componentes_tabulador4(self, tabulador):
        imagen = tk.PhotoImage(file='python-logo.png')
        def mostrar_titulo():
            messagebox.showinfo('Mas info de la imagen',f'Nombre de la imagen: {imagen.cget("file")}')

        boton_imagen = ttk.Button(tabulador, image=imagen, command=mostrar_titulo)
        boton_imagen.grid(row=0, column=0)

    def _crear_componentes_tabulador5(self, tabulador):
        # Creamos el componente de barra de progreso
        barra_progreso = ttk.Progressbar(tabulador, orient='horizontal', length=550)
        barra_progreso.grid(row=0, column=0, padx=10, pady=10, columnspan=4)
        # Metodos para controlar los eventos de la barra de progreso
        def ejecutar_barra():
            barra_progreso['maximum'] = 100
            for valor in range(101):
                # Mandamos a esperar un tiempo
                sleep(1)
                barra_progreso['value'] = valor
                # Actualizar la barra de progreso
                barra_progreso.update()

            barra_progreso['value'] = 0

        def ejecutar_ciclo():
            barra_progreso.start()

        def detener_ejecucion():
            barra_progreso.stop()

        def detener_despues():
            esperar_ms = 2000
            self.after(esperar_ms, barra_progreso.stop) # espues de 1 segundo, parar

        # Botones para controlar los eventos de la barra de progreso
        boton_inicio = ttk.Button(tabulador, text='Ejecutar Barra de progreso', command=ejecutar_barra)
        boton_inicio.grid(row=1, column=0)

        boton_ciclo = ttk.Button(tabulador, text='Ejecutar ciclo', command=ejecutar_ciclo)
        boton_ciclo.grid(row=1, column=1)

        boton_detener = ttk.Button(tabulador, text='Detener ejecución', command=detener_ejecucion)
        boton_detener.grid(row=1, column=2)

        boton_despues = ttk.Button(tabulador, text='Detener ejecución Despues', command=detener_despues)
        boton_despues.grid(row=1, column=3)

    def _crear_tabs(self):
        # Creamos un tab control (se usa la clase Notebook)
        control_tabulador = ttk.Notebook(self)

        # Agregar un marco (Frame) para agregar dentro del tab y organizar
        # Los elementos que se agreguen

        tabulador1 = ttk.Frame(control_tabulador)
        # Agregamos el tabulador al control de tabuladores
        control_tabulador.add(tabulador1, text='TABULADOR 1')
        # Mostramos el tabulador
        control_tabulador.pack(fill='both')
        self._crear_componentes_tabulador1(tabulador1)


        # Creamos un segundo tabulador
        tabulador2 = ttk.LabelFrame(control_tabulador, text='Contenido') # Contenido titulo interno del frame
        control_tabulador.add(tabulador2, text='Tabulador 2')

        # Componente del tabulador 2
        self._crear_componentes_tabulador2(tabulador2)

        # Creamos un tercer tabulador 
        tabulador3 = ttk.LabelFrame(control_tabulador) # Contenido titulo interno del frame
        control_tabulador.add(tabulador3, text='Tabulador 3')

        # Componente del tabulador 3
        self._crear_componentes_tabulador3(tabulador3)

        # Creamos un cuarto tabulador 
        tabulador4 = ttk.LabelFrame(control_tabulador, text='Imagen') # Contenido titulo interno del frame
        control_tabulador.add(tabulador4, text='Tabulador 4 Imagen')

        # Componente del tabulador 4
        self._crear_componentes_tabulador4(tabulador4)

        # Creamos un quinto tabulador 
        tabulador5 = ttk.LabelFrame(control_tabulador, text='Progess Bar') # Contenido titulo interno del frame
        control_tabulador.add(tabulador5, text='Tabulador 5')

        # Componente del tabulador 4
        self._crear_componentes_tabulador5(tabulador5)


if __name__ == '__main__':

    componentes_ventana = ComponentesVentana()
    componentes_ventana.mainloop()

