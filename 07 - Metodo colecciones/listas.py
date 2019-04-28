"""
===============================================================================================================
                            METODOS DISPONIBLES PARA LAS LISTAS
===============================================================================================================
"""

lista = [1,2,3,4,5]
lista2 = [6,7,8,9]
multiplos = [5,10,15,25]
numeros_d = [5,-10,35,0,-65,100]

lista_str = ["Hola", "Mundo", "Hola", "Mundo", "Hola"]

# añadir un nuevo elemento a una lista, usadno el metodo append()

lista.append(6)
print(lista)

# Como vaciar una lista completamente, es decir, vaciar toda la lista, esto se realiza utilizando el metodo clear()

#lista.clear()
#print(lista)

# Como extender (unir) dos listas, para esto se utiliza el metodo extend()
    # En este caso vamos a unir la lista con lista2

lista.extend(lista2)
print(lista)

# contar cuantas veces aparece un elemento en una lista, utilizando el metodo count()

print(lista_str.count("Hola"))

# tambien podemos encontrar el indice donde aparece un elemento, es decir, la posicion en la que esta en la lista, usando el metodo index()

print(lista_str.index("Hola"))

# Insertar un elemento en una lista, en cualquier posicion de la lista, esto se hace a traves del metodo insert, que recibe

    # El primer argumento representa la posicion en la lista, y el segundo el valor que sera asignado en la posicion
    
lista.insert(0, 0)
print(lista)

    # tambien se puede añadir un elemento en el penultimo lugar
    
multiplos.insert(-1, 20)
print(multiplos)

# metodo pop() permite borrar el ultimo elemento de una lista, tambien se puede indicar el indice que se desea sacar

multiplos.pop()
print(multiplos)

# Eliminando en una posicion en especifico
lista.pop(0)

# tambien podemos eliminar un elemento de acuerdo a su valor en la lista, esto se hace con el metodo remove(), que recibe como argumento el valor del elemento que queremos eliminar

lista.remove(8)
print(lista)

# Si el elemnto esta mas de una vez en la lista, este remove() solo elimina el primero, es decir, el que este mas a la izquierda

 # Como darle la vuelta a una lista, usando el metodo reverse()
 
lista.reverse()
print(lista)


# Este metodo no funciona para las cadenas de texto, pero si se puede simular con una lista, en este caso se agrega la cadena a una lista, se aplica el metodo reverse, y luego con un join se consigue el string volteado

list = list("Hola Mundo")
list.reverse()

cadena = "".join(list)
print(cadena)

# odenar una lista, metodo sort(), este metodo ordena la lista de menor a mayor, se recomienda usar solo para listas de numeros

print(numeros_d)
numeros_d.sort()
print(numeros_d)

# Existe la posibilidad de ordenar una lista de mayor a menor, para esto usamos el atributo reverse

numeros_d.sort(reverse=True)
print(numeros_d)









