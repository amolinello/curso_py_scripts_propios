import sys
import tkinter as tk
from tkinter import ttk, messagebox, Menu
# Etiquetas, permite mostrar texto en la interfaz gráfica

ventana = tk.Tk()
ventana.geometry('1000x500')
ventana.title('Manejo de Componentes')
ventana.iconbitmap('icono.ico')

etiqueta1 = tk.Label(ventana, text='Este es el contenido de la caja de texto')

entrada1 = ttk.Entry(
    ventana, 
    width=30
    )

entrada1.grid(row=0, column=0)

def enviar():
    etiqueta1.config(text=entrada1.get())
    mensaje1 = entrada1.get()
    if mensaje1:
        messagebox.showinfo('Titulo del Mensaje Informativo para ti',
        f'''Contenido del mensaje
        que se le quiere dar a 
        conocer al usuario:
        {mensaje1}''')

def salir():
    ventana.quit() # Cierra ventana
    ventana.destroy() # Destruye el objeto ventana
    print('Salimos de la aplicación')
    sys.exit() # Sale de ejecución
    
def crear_menu():
    # Configurar el menú principal
    menu_principal = Menu(ventana)
    
    # Tearoff = False -> para que no se separe el menú de la interfaz gráfica
    menu_archivo = Menu(menu_principal, tearoff=False)
    # Agregamos una nueva opción al menú de archivo
    menu_archivo.add_command(label='Nuevo')
    menu_archivo.add_command(label='Salir', command=salir)

    # Otra opción
    menu_editar = Menu(menu_principal, tearoff=False)
    menu_editar.add_command(label='Copiar')
    menu_editar.add_command(label='Pegar')

    # Otra opción
    menu_vista = Menu(menu_principal, tearoff=True) # Puedo desplegar las 3 opciones por separado
    menu_vista.add_command(label='Tamaño')
    menu_vista.add_separator()
    menu_vista.add_command(label='Apariencia')

    # Agregamos el submenú al menú principal
    menu_principal.add_cascade(menu=menu_archivo, label='Archivo')
    menu_principal.add_cascade(menu=menu_editar, label='Editar')
    menu_principal.add_cascade(menu=menu_vista, label='Ver')

    # Mostramos el menú en la ventan principal
    ventana.config(menu=menu_principal)
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)

boton1.grid(row=0, column=1)
etiqueta1.grid(row=1, column=0, columnspan=2)

crear_menu()

ventana.mainloop()