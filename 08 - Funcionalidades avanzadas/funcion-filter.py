# encoding: utf-8

"""
==============================================================================================
                            FUNCION FILTER
==============================================================================================
"""

# Tal como su nombre lo indica su funcion es filtrar, a partir de una lista o iterador y una funcion condicional es capaz de devolver una nueva coleccion con los elementos filtrados que cumplan la condicion

numeros = [2,5,10,23,50,33]

# Obtener numeros multiples de 5

# Esta funcion devuelve los elementos que son multiples de 5
def multiple(numero):
    if(numero % 5 == 0):
        return True

# la funcion filter de usa de la siguiente manera, el primer argumento debe ser la funcion que hara la logica, es decir, la funcion que devulve los elementos a filtrar, y el segundo argumento son los elementos que sera filtrados, en este caso se utiliza el cash list() para que el filtrado sea devuelto en una lista, por defecto la funcion filter devuelve un objeto iterable
print(list(filter(multiple, numeros)))

# Transformar el ejemplo anterior a una funcion anonima lambda, para reducir la cantidad de lineas de codigo
print( filter( lambda numero: numero%5 == 0, numeros ))


# Ejemplo con una lista de personas, para filtrar las personas menores de edad

class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return "Nombre: {} de {} años".format(self.nombre, self.edad)
    
personas = [
    Persona("Andres",22),
    Persona("Juan",35),
    Persona("Manuel",16),
    Persona("Eduardo",12),
    Persona("Jose",78),
]

# Comprabar las personas menores de edad

menores = filter( lambda persona: persona.edad < 18, personas)

for menor in menores:
    print(menor)
