""" 
======================================================================
    Funciones
======================================================================
"""

# Son fregmentos de codigo que se pueden ejecutar multiples veces, pueden recibir y devolver informacion para comunicarse con el proceso principal

""" 
======================================================================
    Como definir una funcion
======================================================================
"""
# para definir una funcion se debe empezar con un def seguido del nombre con sus respectivos (): debajo de esto se coloca la logica de la funcion

# funcion saludar() que imprime una cadena de texto
def saludar():
    print("Hola, este print se llama desde la funcion saludar")

# funcion que ejecuta un ciclo for, para imprimir la tabla del multiplicar del 5
def dibujar_tabla_5():
    for i in range(11):
     print("5 * ", i, " = ", 5*i)


""" 
======================================================================
    Ambito de las variables en las funciones
======================================================================
"""

# Si se define una variable dentro de una funcion, esta solo podra ser usada dentro de dicha funcion, y no fuera de esta, en cso contrario si una variable esta declarada globalmente esta puede ser usada dentro de la funcion, pero si se cambia el valor de dicha variable dentro de una funcion, este valor solo estara disponible en la funcion

def test():
    n = 10
    print(n)
#test()

""" 
======================================================================
    Retorno de valores
======================================================================
"""

# funcion que retorna una cadena de texto
def prueba():
    return "una cadena retornada"


# funcion que retorna una pila de numeros

def valor():
    return [1,2,3,4]

# funcion que retorna varios valores
def cadena():
    return "una cadena", 20, [1,2,3]

# Si una funcion retorna varios valores, estos valores se pueden asignar individualmente a una variable, es decir, si una funcion retora tres valores, cada valor se puede asignar a una variable distinta, por ejemplo

cadena, numero, pila = cadena()

# La funcion cadena devuelve tres valores, estos valores son asignados cada uno en las tres variables definidas, el primer valor es asignado en la variable cadena, y asi sucesivamente

""" 
======================================================================
    Envio de valores
======================================================================
"""

def suma(a,b):
    return a + b

result = suma(1,2)

""" 
======================================================================
    Argumentos y parametros
======================================================================
"""

def resta(a = None,b = None):
    if( a == None or b == None ):
        print("Por favor, introduzca dos valores numericos")
        return
    else:
        return a - b

# argumentos por posición
result = resta(2,1)

# argumentos por valor
print(resta(b = 2, a = 1))

""" 
======================================================================
    Argumentos por valor y referencia
======================================================================
"""

# Al pasar argumentos por valor, en la funcion se crea una cpopia de dichas variables, que permiten que sean manipuladas en el ambito donde se encuentra la funcion


# Al pasar argumentos por referencia, se modifican los datos originales, que son refencias externas

#Ejemplo de argumentos por valor

def doblar_valor(numero):
     n = numero*2
     print(n)

n = 10
doblar_valor(n)


# Como se puede observar, la funcion recibe una variable, que ya ha sido declara fuera de la funcion, en este caso es "n", con un valor inicial de 10, al ejecutar la funcion se tiene que el valor de n duplica, pero solo dentro de la funcion, despues de llamar a la funcion, fuera de sta el valor de n sigue siendo 10

#Ejemplo de argumento por referencia

def doblar_valores(numeros):
    for i,n in enumerate(numeros):
      numeros[i] *= 2

ns = [10, 50, 10]
#doblar_valores(ns)


# Las listas, pilas, colas, conjuntos se pasan por referencia en python, no hay alguna manera de indicar en python si el argumentos es por valor o por referencia, a diferencia de otros lenguajes, en este caso, los argumentos por referencia son cambiado en la funcion, y estos son afectados externamente tambien

# Se puede simular un argumento por referencia con un numero, cadena, cualquiera, veamos un ejemplo

def doblar_valor(numero):
     return numero*2

n = 10
n = doblar_valor(n)
print(n)

# Tambien se uede evitar un argumento por referencia creando una copia del argumento que se esta pasando y asi evitar que este sea modificado

def doblar_valores(numeros):
    for i,n in enumerate(numeros):
      numeros[i] *= 2

ns = [10, 50, 10]
doblar_valores(ns[:])
print(ns)

# En este caso se crea una copia de ns y se pasa como argumento, asi se evita que el ns original no se vea afectado

""" 
======================================================================
    Argumentos indeterminados
======================================================================
"""

# Python gestiona dos formas distintas de enviar argumentos indeterminado, por posicion y por nombre

# Si la funcion contiene argumentos indeterminados por posicion se le pone a la funcion como parametro *args

# Si la funcion contiene argumentos indeterminados por nombre se le pone a la funcion como parametro *kwargs



# Argumentos indeterminados por posicion

def indeterminados_posicion(*args):
    for arg in args:
        print(arg)

# Esta funcion retornara una tupla
indeterminados_posicion(5, "hola", [1,2,3])

# Argumentos indeterminados por nombre

# funcion que retorna un diccionario
def indeterminados_nombre(**kwargs):
    print(kwargs)
    
indeterminados_nombre(n=5, c="Hola", l=[1,2,3])

# funcion que imprime los argumetos indefinidos uno a uno
def indeterminados_nombre(**kwargs):
    for kwarg in kwargs:
        print(kwarg)
    
indeterminados_nombre(n=5, c="Hola", l=[1,2,3])

#funcion que imprimer los argumentos con clave y valor

def indeterminados_nombre(**kwargs):
    for kwarg in kwargs:
        print(kwarg,":",kwargs[kwarg])
    
indeterminados_nombre(n=5, c="Hola", l=[1,2,3])

def super_funcion(*args, **kwargs):
    suma = 0
    for arg in args:
        suma += arg
    print("La suma de los valores es: ", suma)
    for kwarg in kwargs:
        print(kwarg,":", kwargs[kwarg]) 

super_funcion(10,50,-1,1.56, nombre="Andres", edad=22)

""" 
======================================================================
    Funciones recursivas
======================================================================
"""

# La recursividad es una tecnica muy utilizada que basa en dividir un problema en partes mas pequeñas para poder solucionarlo de forma mas simple, una funcion recursiva se llama a si misma.

#Funcion recursiva sin retorno
def cuenta_atras(num):
    num -= 1
    if(num > 0):
        print(num)
        cuenta_atras(num)
    else:
        print("Boooooom!")
    print("fin de la funcion", num)

# Como calcular el factorial de un numero
def factorial(num):
    print("valor inicial", num)
    if( num > 1):
        num = num * factorial(num-1)
    print("valor final", num)
    return num

print(factorial(5))

""" 
======================================================================
    Funciones integradas
======================================================================
"""

# Como llevar un string a un entero
n = int("10")
print(n)

# Como llevar un string a un flotante
f = float("9")
print(f)

#Como llevar un flotante y un entero a un string
c = "Un numero entero " + str(n) + " y un numero flotante " + str(f)
print(c)

# Como llevar un numero a un binario
b = bin(n)
print(b)

# esto convertira a un numero similar a este 0b1010 donde "0b" indica que es un numero binario, y lo que esta a la derecha de este es el numero en binario, en este caso, transformamo 10 a binario, y su representacion es 1010

# Como llevar un numero a un hexadecimal

h = hex(n)
print(h)

# esto convertira a un numero similar a este 0xa donde "0x" indica que es un numero hexadecimal, y lo que esta a la derecha de este es el numero en hexadecimal, en este caso, transformamo 10 a hexadecimal, y su representacion es a

# Como llevar un binario a un entero

n = int(b,2)
print(n)

#En este caso, si queremos llevar un numero binario a entero, se requieren pasar dos argumentos a la funcion int, el primero de ellos es el numero en binario, y el segundo la base del numero, en este caso al ser un binario, la base es 2

# Como llevar un hexadecimal a un entero

n = int(h,16)
print(n)

#En este caso, si queremos llevar un numero hexadecimal a entero, se requieren pasar dos argumentos a la funcion int, el primero de ellos es el numero en hexadecimal, y el segundo la base del numero, en este caso al ser un hexadecimal, la base es 16

# Valor absoluto de un numero

ps = abs(10)
ng = abs(-10)

# redondear un numero

round(5.5) # en este caso lo redondea por encima, es decir, a 6
round(5.4) # en este caso lo redondea por debajo, es decir, a 5

# Evaluar una expresion de cadena

print(eval("2+5"))

# tambien soporta variable
n = 10
print(eval("n*10 - 5*10"))

# determinar la longitud de una cadena, una lista, ect

len("palabra")

# Si necesitas ayuda con algo que no sepas como usar, se puede utilizar la funcion 

help()
