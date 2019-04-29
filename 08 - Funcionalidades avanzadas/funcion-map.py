# encoding: utf-8

"""
==============================================================================================
                            FUNCION MAP
==============================================================================================
"""

# Trabaja de forma similar a filter, a diferencia de que en lugar de aplicar una condicion a un elemento de una lista o secuencia, aplica una funcion sobre todo los elementos y como resultado se devuelve un iterable de tipo map

# Ejemplo
numeros = [2,5,10,23,50,33]

# Funcion para doblar todos los elementos de la lista

def doblar(numero):
    return numero*2

m = map(doblar, numeros)
print(m)

# El mismo ejemplo se puede crear usando la funcion anonima lambda

m = map(lambda numero: numero*2, numeros)
print(m)

# Se puede utilizar para operar sobre listas de misma longitud

a = [1,2,3,4,5]
b = [6,7,8,9,10]
c = [11,12,13,14,15]

print(map( lambda a,b,c: a*b*c, a,b,c ))

# utilizando map con objetos

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


# funcion normal

def incrementar(persona):
    persona.edad +=1
    return persona

personas = map(incrementar, personas)

for persona in personas:
    print(persona)
    
# Tambien es posible hacer el ejemplo anterior utilizando la funcion lambda

personas = map( lambda persona: Persona(persona.nombre, persona.edad+1), personas )

for persona in personas:
    print(persona)