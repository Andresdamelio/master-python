

class Pelicula:
  # Constructor de la clase
  def __init__(self, titulo, duracion, lanzamiento):
    self.titulo = titulo
    self.duracion = duracion
    self.lanzamiento = lanzamiento
    print("Se ha creado la pelicula:", self.titulo)
    
  # Destructor de clase
  def __del__(self):
      print("Se esta borrando la pelicula:",self.titulo)
    
  # Redefinir el metodo string
  def __str__(self):
      return "{} lanzada en {} con una duración de {} minutos".format(self.titulo, self.lanzamiento, self.duracion)
  
  # Redefinir el metodo len
  def __len__(self):
      return self.duracion
  
       
p = Pelicula("El padrino", 175, 1972)

# metodo string
str(p)

# metodo del
#del(p)

# metodo len

print(len(p))