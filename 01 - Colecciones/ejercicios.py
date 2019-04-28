""" 
======================================================================
    Ejercicio 1
======================================================================
"""

#Realiza un programa que siga las siguientes instrucciones

# 1) Crea un conjunto llamado usuarios con los usuarios: Marta, David, Elvira, Juan y Marcos

    usuarios = {'Marta', 'David', 'Elvira', 'Juan', 'Marcos'}

# 2) Crea un conjunto llamado aministradores con los administadores Juan y Marta

    administradores = {'Juan', 'Marta'} 

# 3) Borra al administrador Juan del conjunto Administradores

    administradores.discard('Juan')

# 4) Añade a marcos como un nuevo administrador pero no lo borres del conjunto usuarios
    administadores.add('Marcos')

# 5) Muestra todos los usuarios por pantalla, de forma dinamica, ademas debes indicar si cada usuario es administrador o no

    for usuario in usuarios:
        if(usuario in administradores):
            print(usuario,' Administrador')
        else:
            print(usuario,' Usuario')
            
""" 
======================================================================
    Ejercicio 2
======================================================================
"""

# Durante el desarrollo de un pequeño video juego se te encarga configurar y balancear cada clase de personaje jugable. Partiendo que la estadistica base es 2, debes cumplir las siguientes condiciones:

# 1) El caballero tiene el doble de de vida y defensa que un guerrero
# 2) El guerrero tiene el doble de ataque y alcance que un caballero
# 3) EL arquero tiene la misma vida y ataque que un guerrero, pero la mitad de su defensa y el doble de su alcance
# 4) Muestra como quedan las propiedades de los tres personajes

caballero = { 
    'vida': 2, 
    'ataque':2, 
    'defensa':2, 
    'alcance':2 
}

guerrero = { 
    'vida': 2, 
    'ataque':2, 
    'defensa':2, 
    'alcance':2 
}

arquero = { 
    'vida': 2, 
    'ataque':2, 
    'defensa':2, 
    'alcance':2 
}

# El caballero tiene el doble de de vida y defensa que un guerrero

    caballero['vida'] = guerrero['vida']*2
    caballero['defensa'] = guerrero['defensa']*2

# El guerrero tiene el doble de ataque y alcance que un caballero
    guerrero['ataque'] = caballero['ataque']*2
    guerrero['alcance'] = caballero['alcance']*2

# EL arquero tiene la misma vida y ataque que un guerrero, pero la mitad de su defensa y el doble de su alcance

    arquero['vida'] = guerrero['vida']
    arquero['ataque'] = guerrero['ataque']
    arquero['defensa'] = guerrero['defensa']/2
    arquero['alcance'] = guerrero['alcance']*2

# Muestra como quedan las propiedades de los tres personajes
  
  caballero = {'vida': 4, 'ataque': 2, 'defensa': 4, 'alcance': 2}
  guerrero = {'vida': 2, 'ataque': 4, 'defensa': 2, 'alcance': 4}
  arquero = {'vida': 2, 'ataque': 4, 'defensa': 1.0, 'alcance': 8}
  
  
""" 
======================================================================
    Ejercicio 3
======================================================================
"""

# Durante la planificacion de un proyecto se han acordado una lista de tareas. Para cada una de estas tareas se ha asignado un orden de prioridad (cuanto menor es el numero de orden, mas prioridad)

#¿Eres capaz de crear una estructura de tipo cola con todas las tareas ordenadas pero sin los numeros de orden?

# Utilizar metodo sort para ordenar una lista

# Importamos deque que nos sirve para crear una cola
from collections import deque

tareas = [
    [6, "Distribucion"],
    [2, "Diseño"],
    [1, "Concepcion"],
    [7, "Mantenimiento"],
    [4, "Produccion"],
    [3, "Planificacion"],
    [5, "Prueba"],
]

# Ordenamos la lista
tareas.sort()

# Cola vacia
cola_tareas = deque([])

# Recorremos la lista, y vamos agregando cada elemento al final de la cola

for tarea in tareas:
    cola_tareas.append(tarea[1])