""" 
======================================================================
    Que es una pila
======================================================================
"""

# Python no tiene pilas y colas, estas se pueden crear a traves de listas

# una pila es una coleccion de elementos ordenados, permite solamente dos opciones, añadir un elemento a la pila o saar un elemento de la pila, el ultimo en entrar es el primero en salir (LIFO - last in first out)


""" 
======================================================================
    Como crear una pila
======================================================================
"""

pila = [3,4,5]

""" 
======================================================================
    Como agregar elementos a una pila
======================================================================
"""
pila = [3,4,5]

pila.append(6)

""" 
======================================================================
    Como sacar el ultimo elemento de la pila
======================================================================
"""
pila = [3,4,5]

pila.pop()

# tambien podemos obtener el elemento a sacar

n = pila.pop()



""" 
======================================================================
    Que es una cola
======================================================================
"""

# Es una coleccion donde el primer elemento en entrar es el primero en salir, usando FIFO (first in first out)

""" 
======================================================================
    Como importar y crear una cola vacia
======================================================================
"""

from collections import deque

cola = deque()

""" 
======================================================================
    Como crear una cola con elementos
======================================================================
"""
    cola = deque(['Ana', 'Juan', 'Andres'])

""" 
======================================================================
    Coma introducir elementos en la cola
======================================================================
"""

# En este caso el elemento a agregar sera colocado al final de la cola, y este deberia ser el ultimo en ser extraido de la cola

cola.append('Cecilia')
cola.append('Jose')

""" 
======================================================================
    Como sacar elementos en la cola
======================================================================
"""

#popleft() permite sacar el primer elemento de la cola, es decir, el que este mas a la izquierda

cola.popleft()

