import tkinter as tk
from tkinter import ttk
# Etiquetas, permite mostrar texto en la interfaz gráfica

ventana = tk.Tk()
ventana.geometry('1000x500')
ventana.title('Manejo de Componentes')
ventana.iconbitmap('icono.ico')


# Etiquetas (label)
etiqueta1 = tk.Label(ventana, text='Este es el contenido de la caja de texto')

# Entry:
# Definimos una variable a modificar posteriormente (set), leer (get)
entrada_var1 = tk.StringVar(value='Valor por default')

entrada1 = ttk.Entry(
    ventana, 
    width=30, 
    textvariable=entrada_var1
    )

entrada1.grid(row=0, column=0)

#entrada1.insert(0, 'Ingrese los datos: ') # si uso esto, sale como primer texto y luego el de entrada_var1
#entrada1.insert(tk.END, '.')

def enviar():
    #Recuperamos la información a partir de la variable asociada a la caja de texto
    boton1.config(text=entrada_var1.get())
    # Modificación, utilizamos la variable de texto y el metodo set
    entrada_var1.set('Texto cambiado!')
    # Recuperamos la información ya modificada
    print(entrada_var1.get())
    # Cambiar la etiqueta
    etiqueta1.config(text=f'Se presiono el botón, el texto cambia: {entrada_var1.get()}')

boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)
etiqueta1.grid(row=1, column=0, columnspan=2)

ventana.mainloop()