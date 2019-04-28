""" 
======================================================================
    Ejercicios
======================================================================
"""

# 1) Localiza el error en el siguiente bloque. Crea una excepcion para evitar que el programa se bloquee y ademas explica en un mensaje al usuario la causa y/o solucion

try:
  resultado = 10/0
except ZeroDivisionError:
  print('Error, no se puede dividir por cero')
  
# 2) Localiza el error en el siguiente bloque. Crea una excepcion para evitar que el programa se bloquee y ademas explica en un mensaje al usuario la causa y/o solucion

lista = [1,2,3,4,5]
try:
    lista[10]
except IndexError:
    print("Error, indice fuera de rango, solicite una posicion entre [0-{}]".format(len(lista)-1))

# 3) Localiza el error en el siguiente bloque. Crea una excepcion para evitar que el programa se bloquee y ademas explica en un mensaje al usuario la causa y/o solucion

colores = {
    "amarillo": "yellow",
    "azul": "blue",
    "verde": "green",
    "rojo": "red"
}

try:
  colores['blanco']
except KeyError:
  print("Error, no esta disponible el color indicado")

# 4) Localiza el error en el siguiente bloque. Crea una excepcion para evitar que el programa se bloquee y ademas explica en un mensaje al usuario la causa y/o solucion

try:
 resultado = "20" + 15
except TypeError:
  print("Error, no se pueden realizar operaciones matematicas con caracteres de tipo cadena")
  
# 5) Realiza una funcion llamada agregar_una_vez() que reciba una lista y un elemento. La funcion debe añadir el elemento al final de la lista con ña condicion de no repetir ningun elemento. Ademas si este elemento se encuentra en la lista debe invocar un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar 

# Error: imposible añadir elementos duplicas => [Elemento]

elementos = [1,5,-2]

def agregar_una_vez(list, elemento): 
    try:
        if( elemento in list):
            raise ValueError("Error: imposible añadir elementos duplicados => {}".format(elemento))
        else:
            list.append(elementos)
    except ValueError as e:
        print(e)
    else:
        print("Elemento agregado con exito")

agregar_una_vez(elementos, 10)
agregar_una_vez(elementos, -2)
agregar_una_vez(elementos, "Hola")