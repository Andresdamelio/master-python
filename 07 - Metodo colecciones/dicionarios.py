"""
===============================================================================================================
                            METODOS DISPONIBLES PARA LOS DICCIONARIOS
===============================================================================================================
"""

colores = {
    "amarillo": "yellow",
    "blue": "blue",
    "rojo": "red",
    "blanco": "white",
}


# Como obtener el valor de una clave, con un mensaje por defecto, utilizando el metodo get

print(colores.get("amarillo", "No se encuentra el color"))

# Como verificar si una clave esta en un diccionario

print("amarillo" in colores)

# Obtener las claves de un diccionario

print(colores.keys())

# Obtener los valores de un diccionario

print(colores.values())

# Como obtener un diccionario con claves y valores

print(colores.items())

# Como mostrar las claves de un diccionario en un ciclo

for c in colores.keys():
    print(c)
    
# Como mostrar los valores de un diccionario en un ciclo

for c in colores.values():
    print(c)
    
for c, v in colores.items():
    print(c,":",v)
    
# Como eliminar elementos de un diccionario

print(colores.pop("negro", "No se ha encontrado en el diccionario de colores"))

# Como vaciar un diccionario

print(colores.clear())