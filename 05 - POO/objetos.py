""" 
======================================================================
    Objetos dentro de objetos
======================================================================
"""

class Pelicula:
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula:", self.titulo)
        
    def __str__(self):
        return "{} lanzada en {} con una duración de {} minutos".format(self.titulo, self.lanzamiento, self.duracion)

class Catalogo:
    peliculas = []
    def __init__(self, peliculas=[]):
        self.peliculas = peliculas
        
    def agregar(self, pelicula):
        self.peliculas.append(pelicula)
    
    def mostrar(self):
        for p in self.peliculas:
            print(p)
            
p = Pelicula("El padrino", 175, 1972)
c = Catalogo([p])

c.agregar(Pelicula("El padrino 2", 202, 1974))
c.agregar(Pelicula("La cita perfercta", 90, 2019))
c.mostrar()