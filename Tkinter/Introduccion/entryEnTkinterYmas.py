import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('1000x500')
ventana.title('Manejo de Grid')
ventana.iconbitmap('icono.ico')

entrada1 = ttk.Entry(
    ventana, 
    width=30, 
    justify=tk.RIGHT,
    state=tk.NORMAL
    #show='*'
    )   # Muestra máximo 30 caracteres, pero puede ingresar mas
        # Por defecto se justifica a la izquierda, pero se puede usar LEFT, RIGHT, CENTER
        # Show: Es el caracter a mostrar en vez del texto ingresado
        # State: Estado del elemento, Disabled (desabilitado), no muestra nada ni permite ingresar nada (DISABLED, NORMAL, ETC)

entrada1.grid(row=0, column=0)

# Insert: Agrega un texto a la caja de texto
entrada1.insert(0, 'Ingrese los datos: ')
entrada1.insert(tk.END, '.')
# entrada1.config(state='readonly') # Estado del elemento como solo lectura

# Metodo del botón
def enviar():
    print(entrada1.get())
    # Cambiar el texto del botón
    boton1.config(text=entrada1.get())

    # Eliminar el contenido
    #entrada1.delete(0, tk.END)

    # Seleccionar el texto de la caja
    entrada1.select_range(0, tk.END) # Toma la cantidad y no hace nada (sin seleccionarlo)
    entrada1.focus() # Selecciona todo el texto en la caja

    

# Botón de capturar información
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)

ventana.mainloop()