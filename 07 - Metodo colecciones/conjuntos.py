"""
===============================================================================================================
                            METODOS DISPONIBLES PARA LOS CONJUNTOS
===============================================================================================================
"""

conjunto = set()

# Como añadir elementos a un conjunto, se utiliza el metodo add()

conjunto.add(1)
conjunto.add(2)
conjunto.add(3)

print(conjunto)

# Como eliminar un elemnto de un conjunto, utilizando el metodo discard

conjunto.discard(1)  
print(conjunto)

# Crear una copia de un conjunto, los conjuntos poseen un metodo copy, que permite crear una copia de un conjunto

conjunto2 =  conjunto.copy()
conjunto2.add(1)
print(conjunto)
print(conjunto2)

# Vaciar un conjunto, utilizando el metodo clear

conjunto2.clear()

# Conjuntos para pruebas
c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2, 3,4,5}

# Como verificar si dos conjuntos son disjuntos, es decir, si dos conjuntos no tienen nada en comun
    # Para verificar esto se utiliza el metodo isdistjoin()

# True, indica que c1 y c3 no tieien nada en comun 
print(c1.isdisjoint(c3))

# false, indica que c1 y c2 tienen al menos un elemento en comun, en este caso, el 3
print(c1.isdisjoint(c2))

# Como verificar si un conjunto es subconjunto de otro, es decir, que los elementos de un conjunto A estan dentro de un conjunto B

# True, todos los elementos de c1 estan incluidos en c4
print(c1.issubset(c4))

# False, todos los elementos de c1 no estan en c2
print(c1.isdisjoint(c2))

# Como verificar si un conjunto es un superconjunto de otro conjunto, es decir, seria lo contrario del issubset, verificar si el grande contiene un conjunto

# True, porque c4 contiene los elementos de c1
print(c4.issuperset(c1))

# False, c1 no contiene todos los elementos de c2
print(c1.issuperset(c2))


# Como unir dos conjuntos, y verificar si es igual a otro, con el emtodo union(), este metodo une dos conjuntos pero no los actualiza, es decir, se usa solo para hacer verificaciones, despues de realizar dicha operacion los conjuntos involucrados siguen siendo los mismos

print(c1.union(c2) == c4)

# La union de dos conjuntos si se puede realizar con el metodo update() que nos permite unir dos conjuntos

c1.update(c2)
print(c1)

# Como ver que elementos no tienen en comun dos conjuntos

c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2, 3,4,5}

# Este metodo nos devuelve, los elementos de c1 que no estan en c2
print(c1.difference(c2))

# Para actualizar el conjunto con la diferencia de un conjunto con otro se utiliza el metodo difference_update(), permite verificar las diferencias y actualizar el conjunto

# Aqui se verifica que elementos de c1 no estan en c2, y se actualizan los elementos de c1
c1.difference_update(c2)
print(c1)

# conjuntos de prueba

c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2, 3,4,5}

# Elementos en comun entre dos conjuntos, usando el metodo intersection()

print(c1.intersection(c2))

# Elementos en comun entre dos conjuntos, y actualizar el conjunto, usando el metodo intersection_update()
c1.intersection_update(c2)
print(c1)

# Como ver los elementos que no son en comun entre dos conjuntos, y sacar los que son comunes

# conjuntos de prueba

c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2, 3,4,5}

print(c1.symmetric_difference(c2))

# diferencia simetrica ya ctualizacion

c1.symmetric_difference_update(c2)
print(c1)