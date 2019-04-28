""" 
======================================================================
    Herencia
======================================================================
"""

# Es la capacidad de una clase de heredar atributos y metodos de otra, ademas de agregar nuevos o modificar los heredados

class Producto():
    def __init__(self, referencia, nombre, pvp, descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion
    
    def __str__(self):
        return """\
Referencia:\t{}
Nombre:\t\t{}
PVP:\t\t{}
Descripcion:\t{}
        """.format(self.referencia, self.nombre, self.pvp, self.descripcion)
        
class Adorno(Producto):
    pass

class Alimento(Producto):
    productor = ""
    distribuidor = ""
    
    def __str__(self):
        return """\
Referencia:\t{}
Nombre:\t\t{}
PVP:\t\t{}
Descripcion:\t{}
Productor:\t{}
Distribuidor:\t{}
        """.format(self.referencia, self.nombre, self.pvp, self.descripcion, self.productor, self.distribuidor)
        
class Libro(Producto):
    isbn = ""
    autor = ""
    
    def __str__(self):
        return """\
Referencia:\t{}
Nombre:\t\t{}
PVP:\t\t{}
Descripcion:\t{}
Isbn:\t\t{}
Autor:\t\t{}
        """.format(self.referencia, self.nombre, self.pvp, self.descripcion, self.isbn, self.autor)
        

# Creando objetos que heredan de producto

ad = Adorno("2034", 'Vaso adornado', 15, "Vaso de porcelana adornado con arboles")
    
al = Alimento("2035", "Aceite de oliva", 5, "250 ml")
al.productor = "La aceitera"
al.distribuidor = "Distribuidoras SA"

li = Libro("2036", "Cocina Mediterránea", 9, "Recetas sanas y buenas")
li.isbn = "0-123456" 
li.autor = "Doña Juana"

# Nota: Los objetos se pasan por referencia, es decir, si se pasa un objeto coo argumento en una funcion, este se vera afectado tanto interno como externamente

def rebajar_producto(prod, rebaja):
    # Devuelve con una rebaja en u porcenaje de su precio
    prod.pvp = prod.pvp - (prod.pvp/100 * rebaja)
    return prod

print("producto sin rebaja")
print(al)
al_rebajado = rebajar_producto(al, 10)
print(al_rebajado)
print("Producto con la rebaja")
print(al)
 

# Como verificar que un objeto es una instancia de una clase
    # se utiliza la funcion isinstance que recibe como primer argumento el objeto a verificar, y como segundo argumento la clase con la que se verificara el objeto

productos = [ad, al]
productos.append(li)

for p in productos:
    if( isinstance(p, Adorno)):
        print(p.referencia,p.nombre)
    elif( isinstance(p, Alimento)):
        print(p.referencia, p.nombre, p.productor)
    elif(isinstance(p, Libro)):
        print(p.referencia, p.nombre, p.isbn)
        
# A los objetos no se le puede hacer una copia, es decir, no se puede asignar un objeto en una variable y cambiar los valores, porque el objeto original tambien se vera afectado

# Se asigna a una variable el objeto al
copia = al

# Se modifica un atributo de dicha copia
copia.referencia = 2038

# En este caso, si se muestra el objeto copia, y el objeto "al" se podra observar que en ambos cambio el atributo referencia, esto por lo dicho anteriormente, que en python no se le realizan copias a los objetos

# Para poder copiar un objeto en python, se debe usar una libreria externa llamada copy, y se utiliza de la siguiente manera

import copy

copia = copy.copy(al)

copia.referencia = 2034

print(al)
print(copia)


""" 
======================================================================
    Polimorfia
======================================================================
"""
# Propiedad de la herencia en que objetos de distintas subclases pueden responder una misma accion

# En python todas las clases son a su vez subclases de la superclase Object, es decir, son polimorficas por defecto

""" 
======================================================================
    Herencia multiple
======================================================================
"""

# Para la herencia multiple se le da prioridad a las superclases que esten mas a la izquierda, es decir, si una clase hereda de multiples clases, ejemplo SubClase(sp1,sp2) en este caso tendra mas prioridad sp1 porque es la que esta mas a la izquierda

class A():
    def __init__(self):
        print("Soy de clase A")
    
    def a(self):
        print("Este metodo lo heredo de la clase A")
        
class B():
    def __init__(self):
        print("Soy de clase B")
    def b(self):
        print("Este metodo lo heredo de la clase B")
        
class C(B,A):
    def c(self):
        print("Este metodo es de C")
    
c = C()
c.a()
c.b()
c.c()
    