# Importar la biblioteca tkinter y usar el alias tk
import tkinter as tk
import random
import math
import json
import sqlite3

personas = []
numeropersonas = 20

class Persona:
    # Crear metodo constructor
    def __init__(self):
        #Propiedades de un objeto que voy a querer guardar en una bbdd
        #Cada vez que se ejecute el programa la posición será aletoria
        self.posx = random.randint(0,1024)
        self.posy = random.randint(0,1024)
        self.radio = 30
        self.direccion = random.randint(0,360)
        self.color = "blue"
        self.entidad = ""
        
    def dibuja(self):
        self.entidad = lienzo.create_oval(
            self.posx-self.radio/2,
            self.posy-self.radio/2,
            self.posx+self.radio/2,
            self.posy+self.radio/2,
            fill=self.color)
        
    def mueve(self):
        self.colisiona()
        lienzo.move(
            self.entidad,
            math.cos(self.direccion),
            math.sin(self.direccion))
        #Actualizo las posiciones
        self.posx += math.cos(self.direccion)
        self.posy += math.sin(self.direccion)
        
    def colisiona(self):
        if self.posx < 0 or self.posx > 1024 or self.posy < 0 or self.posy > 1024:
            self.direccion += math.pi

# Creo la ventana principal
raiz = tk.Tk()
#En la ventana creo un lienzo
lienzo = tk.Canvas(raiz,width=1024,height=1024)
lienzo.pack()

#En la coleccion introduzco instancias de personas
for i in range(0,numeropersonas):
    personas.append(Persona())
    
#Dibuja cada una de las instancias de personas
for persona in personas:
    persona.dibuja()
    
#Creo un bucle repetitivo    
def bucle():
    #Mover las personas en el bucle
    for persona in personas:
        persona.mueve()
    #En 1s quiero ejecutar de nuevo el bucle
    raiz.after(10,bucle)
    
#Ejecuto el bucle    
bucle()

raiz.mainloop()

