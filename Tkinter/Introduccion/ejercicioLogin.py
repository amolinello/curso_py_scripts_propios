
# Todo este codigo se puede usar con el ttk en vez del tk, para tener mas opciones y
# que todo sea mas estetico
import tkinter as tk
from tkinter import ttk, messagebox
# Etiquetas, permite mostrar texto en la interfaz gráfica

ventana = tk.Tk()
ventana.geometry('225x100')
ventana.title('Login')
ventana.resizable(0, 0) # Para que no se pueda aumentar o disminuir la ventana

ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=3)

cuenta = tk.StringVar(value='')
contrasena = tk.StringVar(value='')
textoUsuario = tk.Label(ventana, text='Usuario:', justify=tk.RIGHT)
textoPassword = tk.Label(ventana, text='Password:', justify=tk.RIGHT)

cuadroUsuario = ttk.Entry(
    ventana, 
    width=20,
    textvariable=cuenta
    )
cuadroPassword = ttk.Entry(
    ventana, 
    width=20,
    textvariable=contrasena,
    show='*'
    )

def login():
    if cuenta.get() and contrasena.get():
        tituloCliente = textoUsuario.cget('text')
        tituloContrasena = textoPassword.cget('text')
        
        messagebox.showinfo('Datos Login', f'{tituloCliente} {cuenta.get()}, {tituloContrasena} {contrasena.get()}')

botonLogin = ttk.Button(ventana, text='Login', command=login)

textoUsuario.grid(row=0, column=0, sticky='E', pady= 5)
textoPassword.grid(row=1, column=0, sticky='E')
cuadroUsuario.grid(row=0, column=1, sticky='WE', padx=10)
cuadroPassword.grid(row=1, column=1, sticky='WE', padx=10)
botonLogin.grid(row=3, column=1, sticky= 'W', padx=15, pady=5)



ventana.mainloop()