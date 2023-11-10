# Uso de interfaces gráficas (tkinterface)
# Es un GUI = Graphical User Interface
'''
La ventana sigue procesando los eventos de los botones continuamente, es como estar en un bucle infinito
'''


import tkinter as tk
from tkinter import ttk # Modulo de componentes de tkinter

# 1. Creamos un objeto usando la clase tk
# 2. Modificamos el tamaño de la ventana (Pixeles) (Si no se especifica esto, la crea chiquita)
# 3. Cambiar el nombre de la ventana (Si no se especifica esto, pone como titulo tk)
# 4. Se puede cambiar el icono de la ventana
# 5 Creamos el metodo que va a utilizar el botón
# 6 Agregar un botón
# 7. Utilizar el pack layout manager para que muestre el botón

# x. Iniciamos la ventana mainloop (se ejecuta hasta el final para que se muestre la ventana)


ventana = tk.Tk()                                                                                       # 1.
ventana.geometry('600x400')                                                                             # 2.
ventana.title('Nueva Ventana')                                                                          # 3.
ventana.iconbitmap('icono.ico')                                                                         # 4.
def eventoClic():                                                                                       # 5.
    boton1.config(text='Acción Realizada') # Cambia el texto al oprimir el botón
    print('Se dio Clic en el botón')
    # Crear un nuevo botón para mostrar
    boton2 = ttk.Button(ventana, text='Acción2')
    boton2.pack()
boton1 = ttk.Button(ventana, text='Acción', command=eventoClic)                                         # 6.
boton1.pack()                                                                                           # 7.



ventana.mainloop()                                                                                      # x.



