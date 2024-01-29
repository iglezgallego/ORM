# Importar la biblioteca tkinter y usar el alias tk
import tkinter as tk

# Crear una instancia de la ventana principal
raiz = tk.Tk()

lienzo = tk.Canvas(raiz,width=1024,height=1024)
lienzo.pack()

raiz.mainloop()

