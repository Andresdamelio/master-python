""" 
======================================================================
    Ejercicio 1
======================================================================
"""

# Crear una clase llamada Punto con sus dos coordenadas, x, y

# Añadir un metodo constructor para crear puntos facilmente. Si no se reciben una coordenada, su valor sera 0

# Sobreescribe el metodo string, para que al imprimir por pantalla un punto aparezca en formato (x, y)

# Añade un metodo llamado cuadrante, que indique a que cuadrante pertenece el punto, o si es el origen

# Añade un metodo llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos

# Añade un metodo llamado distancia, que tome otro punto y calcule la distancia entre los dos puntos, la muestre por pantalla

import math

class Punto():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        print("Se ha creado el punto ({},{})".format(x,y))
        
    def __str__(self):
        return "Punto ({},{})".format(self.x,self.y)
    
    def cuadrante(self):
        if ( self.x > 0 and self.y > 0 ):
          return "Primer cuadrante"
        elif  (self.x < 0 and self.y > 0 ):
          return "Segundo cuadrante"
        elif (self.x < 0 and self.y < 0 ):
            return "Tercer cuadrante"
        elif  (self.x > 0 and self.y < 0 ):
            return "Cuarto cuadrante"
        else:
          return "El punto es el origen"
    
    def vector(self, punto):
        x = punto.x - self.x
        y = punto.y - self.y
        
        vector = Punto(x,y)
        return vector
    
    def distancia(self, punto):
        
        d = math.sqrt((punto.x - self.x)**2 + (punto.y - self.y)**2)
        return d
    
#A = Punto(2,3)
#B = Punto(5,5)
#C = Punto(-3,-1)
#D = Punto(0,0)

""" print(A.cuadrante())
print(B.cuadrante())
print(C.cuadrante())
print(D.cuadrante()) """

""" print(A.vector(B))
print(B.vector(A)) """

""" print(A.distancia(B))
print(B.distancia(A)) """

""" 
======================================================================
    Ejercicio 2
======================================================================
"""

# Crea una clase llamada Rectangulo, con puntos(inicial, final) que formaran la diagonal del rectangulo

# Añade un metodo constructor para crear ambos puntos facilmente, si no se envian se colocan cero por defecto.

# Añade al rectangulo el metodo llamado base que muestre la base.

# Añade al rectangulo un metodo llamado altura que muestre la altura.

# Añade al rectangulo un metodo llamado area que muestre el area.

class Rectangulo():
    def __init__(self, inicial = Punto(), final = Punto()):
        self.inicial = inicial
        self.final = final
        
    def base(self):
        punto = Punto(self.final.x, self.inicial.y)
        base = self.inicial.distancia(punto)
        return base
        
    def altura(self):
        punto = Punto(self.inicial.x, self.final.y)
        altura = self.inicial.distancia(punto)
        return altura

    def area(self):
        return self.base()*self.altura()
        
        
""" A = Punto(2,3)
B = Punto(5,5)

r = Rectangulo(A,B)

print(r.base())
print(r.altura())
print(r.area()) """

    
