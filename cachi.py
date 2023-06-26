import tkinter as tk

# Función para manejar el evento del botón
def boton_presionado():
    texto1 = campo_texto1.get()
    texto2 = campo_texto2.get()
    etiqueta_resultado.config(text=f"Campo 1: {texto1}\nCampo 2: {texto2}")

# Crear la ventana principal
ventana = tk.Tk()

# Crear un campo de entrada 1
etiqueta1 = tk.Label(ventana, text="Campo 1:")
etiqueta1.place(x= 20, y=160)
#etiqueta1.pack()
campo_texto1 = tk.Entry(ventana)
campo_texto1.pack()

# Crear un campo de entrada 2
etiqueta2 = tk.Label(ventana, text="Campo 2:")
etiqueta2.place(x=10, y=150)
#etiqueta2.pack()
campo_texto2 = tk.Entry(ventana)
campo_texto2.pack()

# Crear un widget de botón
boton = tk.Button(ventana, text="Mostrar", command=boton_presionado)
boton.pack()

# Crear un widget de etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
