
# Todo este codigo se puede usar con el ttk en vez del tk, para tener mas opciones y
# que todo sea mas estetico
import tkinter as tk
from tkinter import ttk, messagebox


class LoginVentana(tk.Tk):
    def __init__(self):
        super().__init__() # Crea el objeto a partir de la clase
        self.geometry('225x100')
        self.title('Login')
        self.resizable(0, 0) # Para que no se pueda aumentar o disminuir la ventana

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self._crear_componentes()

        # Definir el metodo crear componentes
    def _crear_componentes(self):

        # Texto para informar de que es cada casilla de ingreso de datos
        self.textoUsuario = ttk.Label(self, text='Usuario:', justify=tk.RIGHT)
        self.textoPassword = ttk.Label(self, text='Password:', justify=tk.RIGHT)
        self.textoUsuario.grid(row=0, column=0, sticky='E', pady= 5)
        self.textoPassword.grid(row=1, column=0, sticky='E')

        # Casilla de ingreso de usuario
        self.cuadroUsuario = ttk.Entry(self)
        self.cuadroUsuario.grid(row=0, column=1, sticky='WE', padx=10)

        # Casilla de ingreso de contraseña
        self.cuadroPassword = ttk.Entry(self, show='*')
        self.cuadroPassword.grid(row=1, column=1, sticky='WE', padx=10)

        # Creación del botón
        botonLogin = ttk.Button(self, text='Login', command=self._login)
        botonLogin.grid(row=3, column=1, sticky= 'W', padx=15, pady=5)

    def _login(self):
            
        messagebox.showinfo('Datos Login', f'Usuario: {self.cuadroUsuario.get()}, Password {self.cuadroPassword.get()}')


if __name__ == '__main__':
    login_ventana = LoginVentana()
    login_ventana.mainloop()