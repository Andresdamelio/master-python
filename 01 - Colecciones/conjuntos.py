

""" 
======================================================================
    Que es un conjunto
======================================================================
"""

# Son colecciones desordenadas de elementos unicos, se utilizan normalmente para hacer pruebas de pertenencia a grupos, y elimiacion de elementos duplicados, tambien soportan operaciones atematicas avanzadas

""" 
======================================================================
    Como crear un conjunto vacio
======================================================================
"""

conjunto = set()

""" 
======================================================================
    Como crear un conjunto con valores
======================================================================
"""

conjunto = {1, 2, 3, 4}

""" 
======================================================================
    Agregar elementos a un conjunto
======================================================================
"""

# Como agregar elementos a un conjunto, al agregar un valor numerico este se agregara de acuerdo a su orden, es decir, se agregan de mayor a menor, si se agrega por ejemplo un numero 0 este se agregar en la primera posicion, si se agrega un string este se agregara despues de los valores numericos

#ejemplo

""" 
    >>> conjunto = {1,2,3}
    >>> conjunto.add(0)
    >>> conjunto
    {0, 1, 2, 3}
"""

conjunto.add(valor)

""" 
======================================================================
    Como verificar si un elemento esta en un conjunto
======================================================================
"""

# Como verificar si un elemento esta en un conjunto, para esto crearemos un conjunto de personas, y veremos como verificar si alguno esta en dicho conjunto

grupo_personas = {"Juan", "Maria", "Ana", "Andres"}

"Juan" in grupo_personas 

# Con esto estamos verificando si el nombre "Juan" esta dentro del conjunto, el resultado sera un booleano, True si se encuentra en el conjunto, y false en caso contrario

""" 
======================================================================
    Como verificar si un elemento no sta en un conjunto
======================================================================
"""

# Tambien se puede verificar si un elemento no esta en el conjunto, de forma similar al anterior pero agregando un "not"  antes del "in"

grupo_personas = {"Juan", "Maria", "Ana", "Andres"}

"Juan" not in grupo_personas 

# Ahora el resultado cambia, si es false, es porque el elemento se encuentra dentro del conjunto, en caso contrario, arroja True

""" 
======================================================================
    Los conjuntos no aceptan elementos repetidos
======================================================================
"""

#Los conjuntos no aceptan elementos repetidos, es decir, si se crear un conjunto que contiene un elemento varias veces el conjunto lo tomas como uno solo, sera asi

test = {"elemento", "elemento", "elemento"}

# Si consultamos el conjuto test nos mostrar un unico elemento, {"elemento"}

""" 
======================================================================
    Como convertir una lista en un conjunto
======================================================================
"""

# Si queremos eliminar los elementos repetidos de una lista, lo podemos transformar en un conjunto, y este automaticamente eliminara los elementos repetidos y luego podemos llevarlo nuevamente a una lista

lista = [1, 2, 3, 4, 5, 2, 4, 1, 3]

#llevar la lista a un conjutno, esto nos eliminara los elementos repetidos de la lista

conjunto = set(lista)

# Si consultamos el conjunto se obtiene el siguiente resultado

""" 
    >>> conjunto
    {1, 2, 3, 4, 5}
"""

# Ahora podemos transformar nuevamente el conjunto a una lista de la siguiente manera

lista = list(conjunto)

# Verificamos el valor de la lista

""" 
    >>> lista
    [1, 2, 3, 4, 5]
"""

# Como hacer todos los pasos anteriores en una sola linea, primero declaramos la lista, y efectuamos lo siguiente

lista = [1, 2, 3, 4, 5, 2, 4, 1, 3]

lista = list( set( lista ) )

# Las cadenas de texto tambien pueden ser convertidas en un conjunto

cadena = "Al pan pan y al vino vino"
c = set(cadena)

# El resultado de la conversion es el siguiente

#{'p', 'y', 'v', ' ', 'A', 'l', 'i', 'o', 'n', 'a'}

