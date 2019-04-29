"""
==============================================================================================
                            FUNCION LAMBDA
==============================================================================================
"""

# Sirven para crear funciones anonimas, es decir, una funcion sin nombre, es similar a la funcion normal, pero con una diferencia fundamental y es que el contenido de una funcion lambda debe ser una unica expresion en lugar de un bloque de acciones

# Funcion normal
def doblar(numero):
    resultado = numero * 2
    return resultado

print(doblar(5))

# Funcion doblar en menos lineas de codigo

def doblar(numero): return numero * 2

print(doblar(5))

# Funcion doblar usando la funcion anonima lambda, esta funcion es creado anteponiendo la palabra reservada lambda, seguido de los parametros mas dos puntos, luego de esto lo que se quiere retornar, esta funcion para usarla se recomienda asignarla a una variable, para luego usar la variable como una funcion, como en el sigueinte ejemplo

doblar = lambda num: num*2
print(doblar(5))

# Funcion lambda que devuelve un booleano, en este caso se va a verificar si un numero es impar

impar = lambda num: num%2 != 0 
print(impar(3))
print(impar(4))

# Funcion lambda para revertir una cadena 

# para revertir una cadena se puede utiliar [::-1]
revertir = lambda cadena: cadena[::-1]
print(revertir("Hola mundo"))
print(revertir("odnum aloH"))

# Enviando varios valores a una funcion lambda

sumar = lambda x,y: x + y
print(sumar(3,2))