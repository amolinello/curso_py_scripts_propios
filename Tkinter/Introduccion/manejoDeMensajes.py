import tkinter as tk
from tkinter import ttk, messagebox
# Etiquetas, permite mostrar texto en la interfaz gráfica

ventana = tk.Tk()
ventana.geometry('1000x500')
ventana.title('Manejo de Componentes')
ventana.iconbitmap('icono.ico')


# Etiquetas (label)
etiqueta1 = tk.Label(ventana, text='Este es el contenido de la caja de texto')

entrada1 = ttk.Entry(
    ventana, 
    width=30
    )

entrada1.grid(row=0, column=0)

#entrada1.insert(0, 'Ingrese los datos: ') # si uso esto, sale como primer texto y luego el de entrada_var1
#entrada1.insert(tk.END, '.')

def enviar():
    etiqueta1.config(text=entrada1.get())
    # Se pueden crear algunos mensaje Messagebox (caja de mensajes)
    mensaje1 = entrada1.get()
    if mensaje1: # Si se escribe algo muestra el mensaje
        messagebox.showinfo('Titulo del Mensaje Informativo para ti',
        f'''Contenido del mensaje
        que se le quiere dar a 
        conocer al usuario:
        {mensaje1}''')
        messagebox.showwarning('Titulo del mensaje de alerta', 'Cuidado!!')
        messagebox.showerror('Titulo del error', 'Error o eso creo')
    

boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)
etiqueta1.grid(row=1, column=0, columnspan=2)

ventana.mainloop()