
""" 
======================================================================
    Que es un diccionario
======================================================================
"""

# Son junto a las listas las colecciones mas usadas en python, se basa en una estructura mapeada del ingles mapping, donde cada elemento de la coleccion se encuentra identificado con una clave unica


""" 
======================================================================
    Como crear un diccionario vacio
======================================================================
"""
    d = {}

""" 
======================================================================
    Como verificar que es un diccionario
======================================================================
"""
    d = {}
    type(d)
    
    # El resultado sera  <class 'dict'>


""" 
======================================================================
    Como crear un diccionario con valores
======================================================================
"""


""" 
======================================================================
    Como crear un diccionario con valores
======================================================================
"""

# Con indice de texto
    colores = {
        "amarillo": "yellow",
        "azul": "blue",
        "verde": "green",
        "rojo": "red"
    }

# Con indice numerico
    numeros = {
        10: "Diez",
        3: "Tres",
        6: "Seis",
        8: "Ocho"
    }


""" 
======================================================================
    Como acceder a los elementos de un diccionario
======================================================================
"""

colores = {
    "amarillo": "yellow",
    "azul": "blue",
    "verde": "green",
    "rojo": "red"
}

colores["amarillo"]

""" 
======================================================================
    Como modificar el valor de un elemento del diccionario
======================================================================
"""

    numeros = {
        10: "Diez",
        3: "Tres",
        6: "Seis",
        8: "Ocho"
    }
    
    numeros[10] = "nulo"
    
""" 
======================================================================
    Como eliminar un elemento y su valor
======================================================================
"""

    colores = {
        "amarillo": "yellow",
        "azul": "blue",
        "verde": "green",
        "rojo": "red"
    }

    del(colores["amarillo"])
    
    
""" 
======================================================================
    Como recorrer un diccionario
======================================================================
"""

    colores = {
        "amarillo": "yellow",
        "azul": "blue",
        "verde": "green",
        "rojo": "red"
    }
    
    for color in colores:
        print(color)
        
        
""" 
======================================================================
    Como recorrer un diccionario y obtener los valores
======================================================================
"""

    colores = {
        "amarillo": "yellow",
        "azul": "blue",
        "verde": "green",
        "rojo": "red"
    }
    
    for color in colores:
        print(colores[color])
        
    # Ahora imprimiendo la clave con su valor
    
    for color in colores:
        print(color, colores[color])
        
""" 
======================================================================
    Segunda forma de como recorrer un diccionario y obtener los valores
======================================================================
"""

    colores = {
        "amarillo": "yellow",
        "azul": "blue",
        "verde": "green",
        "rojo": "red"
    }
    
    # De esta forma se obtiene automaticamente la clave con su valor, es decir, "clave": "valor"
    
    for c, v in colores.items():
        print(c,v)
        
""" 
======================================================================
    Como crear una lista de diccionarios
======================================================================
"""

    personajes = []
    
    personaje = {
        "nombre": "Gndalf",
        "clase": "Mago",
        "raza": "Humano"
    }
    
    #Agregar el personaje a la lista, con la funcion append
    
    personajes.append(personaje)
    
    #Agregando otro personaje
    
    personaje = {
        "nombre": "Legolas",
        "clase": "Arquero",
        "raza": "Elfo"
    }
    
    personajes.append(personaje)
    
    personaje = {
        "nombre": "Gimli",
        "clase": "Guerrero",
        "raza": "Enano"
    }
    
    personajes.append(personaje)
    
    # Ahora recorremos la lista de personajes
    
    for p in personajes:
        print(p['nombre'], p['clase'],p['raza'])