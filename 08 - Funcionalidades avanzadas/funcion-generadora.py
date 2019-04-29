"""
==============================================================================================
                            FUNCION GENERADORA E ITERADOR
==============================================================================================
"""

# Funcion generadora
    # Devuelven un objeto generador con caracteristicas particulares, por ejemplo, son iterables, a diferencia de las colecciones, un ejemplo de una funcion generadora es la funcion range, que itera una secuencia finita de numeros, cediendo el ultimo numero, es decir, si se tiene un rango de 0 a 9, este generaria un valor hasta el 8, estos objetos puedes ser iterados en un ciclo
    
def generador_pares(n):
    for numero in range(n+1):
        if( numero % 2 == 0):
            yield numero

# Como se observa, pueden ser usadas en un ciclo, para generar valores especificos          
for n in generador_pares(10):
    print(n)
    
# La funcion generadora puede ser utilizada tambien en una compresion de listas, de la siguiente manera

pares = [par for par in generador_pares(10)]
print(pares)

# Tambien podemos usar la funcion integrada next() que nos permite extraer elementos de un objeto iterable, esta funcion va extrayendo los elementos del objeto, y no puede ser accedido nuevamente, es decir, si se usa la funcion next() en un objeto iterable, y el primer elemento es un 0 y el segundo un 1, al llamar por primera vez la funcion next() el resultado sera 0, pero si lo ejecutamos de nuevo, ya el primer elemento no sera el 0, sino el 1

pares = generador_pares(10)

print(next(pares))
print(next(pares))
print(next(pares))

# Es de resaltar que la funcion next no funciona con una cadena de texto, ni con una coleccion, pero si se puede convertir dicho elemento es un objeto iterable, y asi poder usar la funcion integrada next, esto se hace con el iter()

cadena = "Hola mundo"
lista = [1,2,3,4,5,6]

cadena_iterable = iter(cadena)
lista_iterable = iter(lista)

print(next(cadena_iterable))
print(next(lista_iterable))
            



 
  