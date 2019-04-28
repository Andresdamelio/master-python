""" 
======================================================================
    Salida de datos
======================================================================
"""

v = "otro texto"
n = 10

print("un texto", v, "y un numero", n)

# Para evitar escribir muchos print, e ir colocando variables separadas por una coma ("."), podemos usar el .format, veamos

c = "un texto {} y un numero {}".format(v,n)

# Con esto estamos indicando que la cadena va a recibir dos valores, uno en cada {}, con esto especificamos que vamos a introducir cualquier valor, estos valores son pasados como argumentos en el .format, y se iran colocando de acuerdo al orden en que aparecen en la cadena de texto

""" 
======================================================================
    Colocando los valores por posicion
======================================================================
"""

c = "un texto {0} y un numero {1}".format(v,n)
print(c)

#Al colocar un indice entre las llaves, estamos diciendo la posicion del elemento dentro del .format que mostraremos

""" 
======================================================================
    Colocando letras para los valores
======================================================================
"""

c = "un texto {texto} y un numero {numero}".format(texto=v,numero=n)
print(c)

""" 
======================================================================
    Alinear a la derecha
======================================================================
"""

print("{:>40}".format("Alineamiento derecha"))

#En este caso nos permite alinear a la derecha un string con 40 espacios a la derecha, incluyendo el texto

""" 
======================================================================
    Alinear a la izquierda
======================================================================
"""

print("{:40}".format("Alineamiento izquierda"))

""" 
======================================================================
    Alinear al centro
======================================================================
"""

print("{:^40}".format("Alineamiento central"))

""" 
======================================================================
    Truncar 
======================================================================
"""

#Como truncar una palabra de izquierda a derecha

print("{:.4}".format("Truncamiento"))


""" 
======================================================================
    Formateo de numeros enteros
======================================================================
"""

print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))

#salida por consola

""" 
    0010
    0100
    1000
"""


""" 
======================================================================
    Formateo de numeros flotantes 
======================================================================
"""

print("{:07.3f}".format(3.1415926))
print("{:07.3f}".format(153.21))

