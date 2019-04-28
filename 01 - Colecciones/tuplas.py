
""" 
======================================================================
    Que es una tupla
======================================================================
"""

# Una tupla es una colección de elementos, parecidas a las listas, con la diferencia de que estas son inmutables, se utilizan para asegurarse que los datos no se pueden modificar


""" 
======================================================================
    Declaración de una tupla
======================================================================
"""

tupla = (100,"hola",[1,2,3,4],50)

""" 
======================================================================
    Una tupla no se puede modificar
======================================================================
"""

# Cabe destacar que una tupla no puede ser modificada mediante la asignacion de un valor en una posicion cualquiera, es decir, no se puede hacer lo siguiente

tupla[i] = valor

""" 
======================================================================
    Obtener el ultimo elemento de una tupla
======================================================================
"""
tupla[-1]

""" 
======================================================================
    Obtener el valor dentro de una coleccion presente en una tupla
======================================================================
"""

#Obtener el valor de una coleccion dentro de una tupla, en este caso nuestra tupla contiene un array en una de sus posiciones, para obtener dichos valores de la tupla se hace de la siguiente manera

tupla[2][1]

""" 
======================================================================
    Longitud de una tupla
======================================================================
"""

len(tupla[i]) 

#donde i representa la posicion donde se encuentra la coleccion a la cual queremos obtener la longitud 

len(tupla)

""" 
======================================================================
    Obtener valor de un elemento de una tupla
======================================================================
"""

# Como obtener la posicion de un elemento especifico de la tupla, esta funcion arroja un error si el elemento a buscar no existe en la tupla, si el elemento a buscar esta varias veces en la tupla el resultado sera la posicion del primer elemento

tupla.index(elemento)

""" 
======================================================================
    Contar la cantidad de elementos de una tupla
======================================================================
"""

# Si el elemento no esta en la tupla el resultado sera 0

tupla.count(elemento)

""" 
======================================================================
    No esta disponible la funcion append
======================================================================
"""

# Al no poder modificarse una tupla, no existe la funcion append, que en otros lenguajes es agregar un elemento mas a la colección