import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('1000x500')
ventana.title('Manejo de Grid')
ventana.iconbitmap('icono.ico')

# Definición de metodos de eventos

def evento1():
    boton1.config(text='Botón 1 Presionado')

def evento2():
    boton2.config(text='Botón 2 Presionado')
    
def evento3():
    boton3.config(text='Botón 3 Presionado')

def evento4():
    boton4.config(text='Botón 4 Presionado', fg= 'blue', relief= tk.GROOVE, bg= 'green') # El fg solo sirve en el tk, en el ttk no
    # relief = relieve, bg = background (fondo)
    # Esto solo funciona en tk, pero el que comunmente se usa es el ttk

# Definición de botones
boton1 = ttk.Button(ventana, text='Botón 1', command=evento1) 
boton2 = ttk.Button(ventana, text='Botón 2', command=evento2)
boton3 = ttk.Button(ventana, text='Botón 3', command=evento3)
boton4 = tk.Button(ventana, text='Botón 4', command=evento4) # Se puede usar tk o ttk, cambia la presentación del botón

# sticky = Mueve los botones en la columna o fila según se indique
# Ejemplo, si se amplia el texto en un botón en la misma columna, puedo pedir que el otro botón siga alineado a la izquierda
# N (arriba), E(derecha), S(abajo), W(izquierda) direcciones de texto, Se puede indicar por separado o todo junto 'NESW'

ventana.rowconfigure(0, weight=2)
ventana.rowconfigure(1, weight=10)
ventana.columnconfigure(0, weight=2)
ventana.columnconfigure(1, weight=5)

boton1.grid(row=0, column=0, sticky='NESW', padx=50, ipady=90, columnspan=2, rowspan=2)
boton2.grid(row=1, column=0, sticky='NESW')
boton3.grid(row=0, column=1, sticky='NESW')
boton4.grid(row=1, column=1, sticky='NESW', pady=100, ipadx=90)

ventana.mainloop()

# Padding = Espacio entre los elementos, se tiene padx y pady para lo externo
# ipadx y ipady es para la parte interna del cuadro

# Con columnspan se puede ocupar mas de una columna
# Con rowspan se puede ocupar mas de una fila


