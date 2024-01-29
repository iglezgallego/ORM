# Importar la biblioteca tkinter y usar el alias tk
import tkinter as tk

class Persona:
    # Crear metodo constructor
    def __init__(self):
        #Propiedades de un objeto que voy a querer guardar en una bbdd
        self.posx = 512
        self.posy = 512
    def dibuja(self):
        lienzo.create_oval(30,30,60,60,fill="red")

# Crear una instancia de la ventana principal
raiz = tk.Tk()

lienzo = tk.Canvas(raiz,width=1024,height=1024)
lienzo.pack()

#Creo una instancia de la clase
persona = Persona()
persona.dibuja()

raiz.mainloop()

