import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfilename

class EditorDeTexto(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.geometry('1000x800')
        self.resizable(1920,1080)
        self.title('Editor de texto propio')
        self.iconbitmap('icono.ico')
        self.rowconfigure(0, minsize=600, weight=1)
        self.columnconfigure(1, minsize=600, weight=1)

        self.campo_texto = tk.Text(self, wrap=tk.WORD) # Sirve para tener palabras completas
        self.archivo = None
        # Self variable para saber si se abrió un archivo
        self.archivo_abierto = False

        self._creacion_componentes()
        self._crear_menu()

    def _creacion_componentes(self):
        frame_botones = tk.Frame(self, relief=tk.RAISED, bd=2)
        boton_abrir = tk.Button(frame_botones, text='Abrir', font=('arial',10), command=self._abrir_archivo)
        boton_guardar = tk.Button(frame_botones, text='Guardar', font=('arial',10), command=self._guardar)
        boton_guardar_como = tk.Button(frame_botones, text='Guardar como...', font=('arial',10), command=self._guardar_como)

        # Se expanden los botones de manera horizontal (sticky = 'we')
        boton_abrir.grid(row=0, column=0, sticky='WE', padx=5, pady=5)
        boton_guardar.grid(row=1, column=0, sticky='WE', padx=5, pady=5)
        boton_guardar_como.grid(row=2, column=0, sticky='WE', padx=5, pady=5)

        # Se coloca el frame de manera vertical
        frame_botones.grid(row=0, column=0, sticky='ns')

        # Agregamos el campo de texto
        # Expande por completo el espacio disponible que le resta
        self.campo_texto.grid(row=0, column=1, sticky='nsew')

    def _crear_menu(self):

        # Se crea el menú de la APP
        menu_app = tk.Menu(self)
        self.config(menu=menu_app)
        # Agregamos las opciones al menú
        menu_archivo = tk.Menu(menu_app, tearoff=False)
        menu_app.add_cascade(label='Archivo' ,menu= menu_archivo, font=('arial',12))

        # Agregamos las opciones del menu archivo
        menu_archivo.add_command(label='Abrir', command=self._abrir_archivo)
        menu_archivo.add_command(label='Guardar', command=self._guardar)
        menu_archivo.add_command(label='Guardar como...', command=self._guardar_como)
        menu_archivo.add_separator()
        menu_archivo.add_command(label='Salir', command=self.quit)

    def _abrir_archivo(self):
            # Abrimos el archivo para edición Lectura/Escritura
            self.archivo_abierto  = askopenfile(mode='r+')
            # Eliminamos el texto anterior
            self.campo_texto.delete(1.0, tk.END)
            # Revisamos si hay un archivo
            if not self.archivo_abierto:
                # Regresa el control a la aplicación
                return

            # Abrimos el archivo en modo lectura y escritura como un recurso
            with open(self.archivo_abierto.name, 'r') as self.archivo:
                # Leemos el contenido del archivo
                texto = self.archivo.read()
                # Insertamos el contenido al archivo en el campo de texto
                self.campo_texto.insert(1.0, texto)
                self.title(f'*Editor texto - {self.archivo.name}')
            
    def _guardar(self):
            # Si se abrió anteriormente un archivo se sobreescribe
            if self.archivo_abierto:
                # Salvamos el archivo, lo abrimos en modo escritura
                with open(self.archivo_abierto.name, 'w') as self.archivo:
                    # Leer el contenido de la caja de texto
                    texto = self.campo_texto.get(1.0, tk.END)
                    # Escribir el contenido en el mismo archivo
                    self.archivo.write(texto)
                    # Cambiar el nombre del titulo de la app
                    self.title(f'Editor texto - {self.archivo.name}')

            else:
                self._guardar_como()

    def _guardar_como(self):
            # Guardar el archivo actual como un nuevo archivo
            self.archivo = asksaveasfilename(
                defaultextension='txt',
                filetypes=[('Archivos de Texto', '*.txt'), ('Todos los Archivos', '*.*')]
            )
            if not self.archivo:
                return
            
            # Abrir el archivo en mod escritura
            
            with open(self.archivo, 'w') as self.archivo:
                # Leemos el contenido de la caja de texto
                texto = self.campo_texto.get(1.0, tk.END)
                self.archivo.write(texto)
                self.title(f'Editor texto - {self.archivo.name}')
                # Indicamos que ya se abrio el archivo
                self.archivo_abierto = self.archivo

if __name__ == '__main__':
    editorT = EditorDeTexto()
    editorT.mainloop()